from typing import Dict, Any, List, Optional, Union
from openai import AsyncOpenAI
from supabase import Client
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.utils import get_env_var

embedding_model = get_env_var('EMBEDDING_MODEL') or 'text-embedding-3-small'

async def get_embedding(text: str, embedding_client: AsyncOpenAI) -> List[float]:
    """Get embedding vector from OpenAI."""
    try:
        response = await embedding_client.embeddings.create(
            model=embedding_model,
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error getting embedding: {e}")
        return [0] * 1536  # Return zero vector on error

async def retrieve_relevant_documentation_tool(
    supabase: Client, 
    embedding_client: AsyncOpenAI, 
    user_query: str, 
    sources: Optional[List[str]] = None
) -> str:
    """
    Retrieve relevant documentation chunks based on the query with RAG.
    
    Args:
        supabase: The Supabase client
        embedding_client: The OpenAI client for embeddings
        user_query: The user query to search for
        sources: Optional list of documentation sources to search in. If None, searches all sources.
                Available sources: 'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
    
    Returns:
        A formatted string containing the top 4 most relevant documentation chunks
    """
    try:
        # Get the embedding for the query
        query_embedding = await get_embedding(user_query, embedding_client)
        
        # Set up the filter based on provided sources or default to all sources
        if not sources:
            sources = ['pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs']
        
        # Create a filter with OR conditions for each source
        filter_data = {}
        if len(sources) == 1:
            filter_data = {'source': sources[0]}
        else:
            # For multiple sources, we need to create a different query structure
            result_data = []
            
            # Query each source and collect results
            for source in sources:
                source_result = supabase.rpc(
                    'match_site_pages',
                    {
                        'query_embedding': query_embedding,
                        'match_count': 2,  # Get 2 from each source for variety
                        'filter': {'source': source}
                    }
                ).execute()
                
                if source_result.data:
                    result_data.extend(source_result.data)
            
            # Sort by similarity score (higher is better)
            result_data.sort(key=lambda x: x.get('similarity', 0), reverse=True)
            
            # Take top 4 overall
            result_data = result_data[:4]
            
            if not result_data:
                return "No relevant documentation found."
                
            # Format the results
            formatted_chunks = []
            for doc in result_data:
                source_name = "Unknown Source"
                if doc.get('metadata', {}).get('source') == 'pydantic_ai_docs':
                    source_name = "Pydantic AI"
                elif doc.get('metadata', {}).get('source') == 'crawl4ai_docs':
                    source_name = "Crawl4AI"
                elif doc.get('metadata', {}).get('source') == 'langchain_python_docs':
                    source_name = "Langchain Python"
                
                chunk_text = f"""
# {doc['title']} (Source: {source_name})

{doc['content']}
"""
                formatted_chunks.append(chunk_text)
                
            # Join all chunks with a separator
            return "\n\n---\n\n".join(formatted_chunks)
        
        # Default query if we have a simple filter (only one source)
        result = supabase.rpc(
            'match_site_pages',
            {
                'query_embedding': query_embedding,
                'match_count': 4,
                'filter': filter_data
            }
        ).execute()
        
        if not result.data:
            return "No relevant documentation found."
            
        # Format the results
        formatted_chunks = []
        for doc in result.data:
            chunk_text = f"""
# {doc['title']}

{doc['content']}
"""
            formatted_chunks.append(chunk_text)
            
        # Join all chunks with a separator
        return "\n\n---\n\n".join(formatted_chunks)
        
    except Exception as e:
        print(f"Error retrieving documentation: {e}")
        return f"Error retrieving documentation: {str(e)}" 

async def list_documentation_pages_tool(supabase: Client, source: Optional[str] = None) -> List[str]:
    """
    Function to retrieve a list of all available documentation pages.
    This is called by the list_documentation_pages tool and also externally
    to fetch documentation pages for the reasoner LLM.
    
    Args:
        supabase: The Supabase client
        source: Optional documentation source to filter by.
               Available sources: 'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
               If None, returns pages from all sources.
    
    Returns:
        List[str]: List of unique URLs for all documentation pages
    """
    try:
        query = supabase.from_('site_pages').select('url, metadata')
        
        # Apply source filter if specified
        if source:
            query = query.eq('metadata->>source', source)
        
        result = query.execute()
        
        if not result.data:
            return []
            
        # Extract unique URLs
        urls = []
        for doc in result.data:
            source_name = ""
            if doc.get('metadata', {}).get('source') == 'pydantic_ai_docs':
                source_name = "[Pydantic AI] "
            elif doc.get('metadata', {}).get('source') == 'crawl4ai_docs':
                source_name = "[Crawl4AI] "
            elif doc.get('metadata', {}).get('source') == 'langchain_python_docs':
                source_name = "[Langchain Python] "
            
            urls.append(f"{source_name}{doc['url']}")
        
        return sorted(set(urls))
        
    except Exception as e:
        print(f"Error retrieving documentation pages: {e}")
        return []

async def get_page_content_tool(supabase: Client, url: str, source: Optional[str] = None) -> str:
    """
    Retrieve the full content of a specific documentation page by combining all its chunks.
    
    Args:
        supabase: The Supabase client
        url: The URL of the page to retrieve
        source: Optional documentation source to use when retrieving the page.
               Available sources: 'pydantic_ai_docs', 'crawl4ai_docs', 'langchain_python_docs'
               If None, attempts to find the page without filtering by source.
    
    Returns:
        str: The complete page content with all chunks combined in order
    """
    try:
        # Clean URL (remove source prefix if present)
        clean_url = url
        if "[Pydantic AI] " in url:
            clean_url = url.replace("[Pydantic AI] ", "")
            if not source:
                source = 'pydantic_ai_docs'
        elif "[Crawl4AI] " in url:
            clean_url = url.replace("[Crawl4AI] ", "")
            if not source:
                source = 'crawl4ai_docs'
        elif "[Langchain Python] " in url:
            clean_url = url.replace("[Langchain Python] ", "")
            if not source:
                source = 'langchain_python_docs'
        
        # Set up the query
        query = supabase.from_('site_pages') \
            .select('title, content, chunk_number') \
            .eq('url', clean_url)
        
        # Apply source filter if specified
        if source:
            query = query.eq('metadata->>source', source)
        
        # Execute query with ordering
        result = query.order('chunk_number').execute()
        
        if not result.data:
            # If no results with the source filter, try without it
            if source:
                return await get_page_content_tool(supabase, clean_url, None)
            return f"No content found for URL: {clean_url}"
            
        # Get the source from the first result for display
        doc_source = result.data[0].get('metadata', {}).get('source', 'unknown')
        source_name = ""
        if doc_source == 'pydantic_ai_docs':
            source_name = "Pydantic AI: "
        elif doc_source == 'crawl4ai_docs':
            source_name = "Crawl4AI: "
        elif doc_source == 'langchain_python_docs':
            source_name = "Langchain Python: "
        
        # Format the page with its title and all chunks
        page_title = result.data[0]['title'].split(' - ')[0]  # Get the main title
        formatted_content = [f"# {source_name}{page_title}\n"]
        
        # Add each chunk's content
        for chunk in result.data:
            formatted_content.append(chunk['content'])
            
        # Join everything together but limit the characters in case the page is massive
        # This will be improved later so if the page is too big RAG will be performed on the page itself
        return "\n\n".join(formatted_content)[:20000]
        
    except Exception as e:
        print(f"Error retrieving page content: {e}")
        return f"Error retrieving page content: {str(e)}"