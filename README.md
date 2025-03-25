Add Langchain Python and Crawl4AI Documentation Crawling Support

This PR adds a new capability to Archon: the ability to crawl and index both Langchain Python documentation and Crawl4AI documentation, similar to how the existing Pydantic AI documentation crawler works.
New Features

    Added archon/crawl_langchain_python_docs.py for crawling the Langchain Python documentation
    Added archon/crawl_craw4ai_docs.py for crawling the Crawl4AI documentation
    Updated the Streamlit UI in streamlit_pages/documentation.py to include tabs for both new crawlers

Implementation Details

Both crawlers use the same approach as the existing Pydantic AI documentation crawler:

    Fetching URLs from the respective sitemaps
    Crawling each page and extracting content
    Splitting content into chunks
    Generating embeddings for each chunk
    Storing the chunks in the Supabase database

Testing

Both crawlers have been tested and are working correctly. The Streamlit UI provides proper progress tracking and status updates during the crawling process.
Benefits

This integration enables Archon to create agents that leverage knowledge from multiple documentation sources:

    Pydantic AI for agent creation
    Langchain for workflow orchestration and LLM interactions
    Crawl4AI for web crawling capabilities

By having all three documentation sources available, Archon can create more comprehensive and capable agents that combine the strengths of each framework.
