from __future__ import annotations as _annotations

from dataclasses import dataclass
from dotenv import load_dotenv
import logfire
import asyncio
import httpx
import os
import sys
import json
from typing import List, Optional
from pydantic import BaseModel
from pydantic_ai import Agent, ModelRetry, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from pydantic_ai.models.openai import OpenAIModel
from openai import AsyncOpenAI
from supabase import Client

# Add the parent directory to sys.path to allow importing from the parent directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.utils import get_env_var
from archon.agent_prompts import tools_refiner_prompt
from archon.agent_tools import (
    retrieve_relevant_documentation_tool,
    list_documentation_pages_tool,
    get_page_content_tool
)

load_dotenv()

provider = get_env_var('LLM_PROVIDER') or 'OpenAI'
llm = get_env_var('PRIMARY_MODEL') or 'gpt-4o-mini'
base_url = get_env_var('BASE_URL') or 'https://api.openai.com/v1'
api_key = get_env_var('LLM_API_KEY') or 'no-llm-api-key-provided'

model = AnthropicModel(llm, api_key=api_key) if provider == "Anthropic" else OpenAIModel(llm, base_url=base_url, api_key=api_key)
embedding_model = get_env_var('EMBEDDING_MODEL') or 'text-embedding-3-small'

logfire.configure(send_to_logfire='if-token-present')

@dataclass
class ToolsRefinerDeps:
    supabase: Client
    embedding_client: AsyncOpenAI

tools_refiner_agent = Agent(
    model,
    system_prompt=tools_refiner_prompt,
    deps_type=ToolsRefinerDeps,
    retries=2
)

@tools_refiner_agent.tool
async def retrieve_relevant_documentation(ctx: RunContext[ToolsRefinerDeps], query: str, sources: Optional[List[str]] = None) -> str:
    """
    Retrieve relevant documentation chunks based on the query with RAG.
    Make sure your searches always focus on implementing tools.
    
    Args:
        ctx: The context including the Supabase client and OpenAI client
        query: Your query to retrieve relevant documentation for implementing tools
        sources: Optional list of documentation sources to search in. Available sources: 
                'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
                If None, searches all available sources.
        
    Returns:
        A formatted string containing the most relevant documentation chunks
    """
    return await retrieve_relevant_documentation_tool(ctx.deps.supabase, ctx.deps.embedding_client, query, sources)

@tools_refiner_agent.tool
async def list_documentation_pages(ctx: RunContext[ToolsRefinerDeps], source: Optional[str] = None) -> List[str]:
    """
    Retrieve a list of all available documentation pages.
    This will give you all pages available, but focus on the ones related to tools.
    
    Args:
        ctx: The context including the Supabase client
        source: Optional documentation source to filter by. Available sources:
               'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
               If None, returns pages from all sources.
    
    Returns:
        List[str]: List of unique URLs for all documentation pages with source prefixes
    """
    return await list_documentation_pages_tool(ctx.deps.supabase, source)

@tools_refiner_agent.tool
async def get_page_content(ctx: RunContext[ToolsRefinerDeps], url: str, source: Optional[str] = None) -> str:
    """
    Retrieve the full content of a specific documentation page by combining all its chunks.
    Use this tool to get pages related to using tools with Pydantic AI, Crawl4AI and Langchain Python.
    
    Args:
        ctx: The context including the Supabase client
        url: The URL of the page to retrieve (can include source prefix like '[Pydantic AI] url')
        source: Optional documentation source to use. Available sources:
               'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
               If None, attempts to determine the source from the URL or find the page without filtering.
        
    Returns:
        str: The complete page content with all chunks combined in order
    """
    return await get_page_content_tool(ctx.deps.supabase, url, source)