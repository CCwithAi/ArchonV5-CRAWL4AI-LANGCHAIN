[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/strategies/)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * [Command Line Interface](https://docs.crawl4ai.com/core/cli/)
    * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/)
    * [Deep Crawling](https://docs.crawl4ai.com/core/deep-crawling/)
    * [Crawler Result](https://docs.crawl4ai.com/core/crawler-result/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/core/browser-crawler-config/)
    * [Markdown Generation](https://docs.crawl4ai.com/core/markdown-generation/)
    * [Fit Markdown](https://docs.crawl4ai.com/core/fit-markdown/)
    * [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/)
    * [Content Selection](https://docs.crawl4ai.com/core/content-selection/)
    * [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)
    * [Local Files & Raw HTML](https://docs.crawl4ai.com/core/local-files/)
    * [Link & Media](https://docs.crawl4ai.com/core/link-media/)
  * Advanced
    * [Overview](https://docs.crawl4ai.com/advanced/advanced-features/)
    * [File Downloading](https://docs.crawl4ai.com/advanced/file-downloading/)
    * [Lazy Loading](https://docs.crawl4ai.com/advanced/lazy-loading/)
    * [Hooks & Auth](https://docs.crawl4ai.com/advanced/hooks-auth/)
    * [Proxy & Security](https://docs.crawl4ai.com/advanced/proxy-security/)
    * [Session Management](https://docs.crawl4ai.com/advanced/session-management/)
    * [Multi-URL Crawling](https://docs.crawl4ai.com/advanced/multi-url-crawling/)
    * [Crawl Dispatcher](https://docs.crawl4ai.com/advanced/crawl-dispatcher/)
    * [Identity Based Crawling](https://docs.crawl4ai.com/advanced/identity-based-crawling/)
    * [SSL Certificate](https://docs.crawl4ai.com/advanced/ssl-certificate/)
  * Extraction
    * [LLM-Free Strategies](https://docs.crawl4ai.com/extraction/no-llm-strategies/)
    * [LLM Strategies](https://docs.crawl4ai.com/extraction/llm-strategies/)
    * [Clustering Strategies](https://docs.crawl4ai.com/extraction/clustring-strategies/)
    * [Chunking](https://docs.crawl4ai.com/extraction/chunking/)
  * API Reference
    * [AsyncWebCrawler](https://docs.crawl4ai.com/api/async-webcrawler/)
    * [arun()](https://docs.crawl4ai.com/api/arun/)
    * [arun_many()](https://docs.crawl4ai.com/api/arun_many/)
    * [Browser, Crawler & LLM Config](https://docs.crawl4ai.com/api/parameters/)
    * [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/)
    * Strategies


  * [Extraction & Chunking Strategies API](https://docs.crawl4ai.com/api/strategies/#extraction-chunking-strategies-api)
  * [Extraction Strategies](https://docs.crawl4ai.com/api/strategies/#extraction-strategies)
  * [Chunking Strategies](https://docs.crawl4ai.com/api/strategies/#chunking-strategies)
  * [Usage Examples](https://docs.crawl4ai.com/api/strategies/#usage-examples)
  * [Best Practices](https://docs.crawl4ai.com/api/strategies/#best-practices)


# Extraction & Chunking Strategies API
This documentation covers the API reference for extraction and chunking strategies in Crawl4AI.
## Extraction Strategies
All extraction strategies inherit from the base `ExtractionStrategy` class and implement two key methods: - `extract(url: str, html: str) -> List[Dict[str, Any]]` - `run(url: str, sections: List[str]) -> List[Dict[str, Any]]`
### LLMExtractionStrategy
Used for extracting structured data using Language Models.
```
LLMExtractionStrategy(
  # Required Parameters
  provider: str = DEFAULT_PROVIDER,   # LLM provider (e.g., "ollama/llama2")
  api_token: Optional[str] = None,   # API token
  # Extraction Configuration
  instruction: str = None,       # Custom extraction instruction
  schema: Dict = None,         # Pydantic model schema for structured data
  extraction_type: str = "block",    # "block" or "schema"
  # Chunking Parameters
  chunk_token_threshold: int = 4000,  # Maximum tokens per chunk
  overlap_rate: float = 0.1,      # Overlap between chunks
  word_token_rate: float = 0.75,    # Word to token conversion rate
  apply_chunking: bool = True,     # Enable/disable chunking
  # API Configuration
  base_url: str = None,        # Base URL for API
  extra_args: Dict = {},        # Additional provider arguments
  verbose: bool = False        # Enable verbose logging
)

```

### CosineStrategy
Used for content similarity-based extraction and clustering.
```
CosineStrategy(
  # Content Filtering
  semantic_filter: str = None,    # Topic/keyword filter
  word_count_threshold: int = 10,   # Minimum words per cluster
  sim_threshold: float = 0.3,     # Similarity threshold
  # Clustering Parameters
  max_dist: float = 0.2,       # Maximum cluster distance
  linkage_method: str = 'ward',    # Clustering method
  top_k: int = 3,          # Top clusters to return
  # Model Configuration
  model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', # Embedding model
  verbose: bool = False       # Enable verbose logging
)

```

### JsonCssExtractionStrategy
Used for CSS selector-based structured data extraction.
```
JsonCssExtractionStrategy(
  schema: Dict[str, Any],  # Extraction schema
  verbose: bool = False   # Enable verbose logging
)
# Schema Structure
schema = {
  "name": str,       # Schema name
  "baseSelector": str,   # Base CSS selector
  "fields": [        # List of fields to extract
    {
      "name": str,   # Field name
      "selector": str, # CSS selector
      "type": str,   # Field type: "text", "attribute", "html", "regex"
      "attribute": str, # For type="attribute"
      "pattern": str, # For type="regex"
      "transform": str, # Optional: "lowercase", "uppercase", "strip"
      "default": Any  # Default value if extraction fails
    }
  ]
}

```

## Chunking Strategies
All chunking strategies inherit from `ChunkingStrategy` and implement the `chunk(text: str) -> list` method.
### RegexChunking
Splits text based on regex patterns.
```
RegexChunking(
  patterns: List[str] = None # Regex patterns for splitting
                # Default: [r'\n\n']
)

```

### SlidingWindowChunking
Creates overlapping chunks with a sliding window approach.
```
SlidingWindowChunking(
  window_size: int = 100,  # Window size in words
  step: int = 50       # Step size between windows
)

```

### OverlappingWindowChunking
Creates chunks with specified overlap.
```
OverlappingWindowChunking(
  window_size: int = 1000,  # Chunk size in words
  overlap: int = 100     # Overlap size in words
)

```

## Usage Examples
### LLM Extraction
```
from pydantic import BaseModel
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from crawl4ai import LLMConfig
# Define schema
class Article(BaseModel):
  title: str
  content: str
  author: str
# Create strategy
strategy = LLMExtractionStrategy(
  llm_config = LLMConfig(provider="ollama/llama2"),
  schema=Article.schema(),
  instruction="Extract article details"
)
# Use with crawler
result = await crawler.arun(
  url="https://example.com/article",
  extraction_strategy=strategy
)
# Access extracted data
data = json.loads(result.extracted_content)

```

### CSS Extraction
```
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
# Define schema
schema = {
  "name": "Product List",
  "baseSelector": ".product-card",
  "fields": [
    {
      "name": "title",
      "selector": "h2.title",
      "type": "text"
    },
    {
      "name": "price",
      "selector": ".price",
      "type": "text",
      "transform": "strip"
    },
    {
      "name": "image",
      "selector": "img",
      "type": "attribute",
      "attribute": "src"
    }
  ]
}
# Create and use strategy
strategy = JsonCssExtractionStrategy(schema)
result = await crawler.arun(
  url="https://example.com/products",
  extraction_strategy=strategy
)

```

### Content Chunking
```
from crawl4ai.chunking_strategy import OverlappingWindowChunking
from crawl4ai import LLMConfig
# Create chunking strategy
chunker = OverlappingWindowChunking(
  window_size=500, # 500 words per chunk
  overlap=50    # 50 words overlap
)
# Use with extraction strategy
strategy = LLMExtractionStrategy(
  llm_config = LLMConfig(provider="ollama/llama2"),
  chunking_strategy=chunker
)
result = await crawler.arun(
  url="https://example.com/long-article",
  extraction_strategy=strategy
)

```

## Best Practices
1. **Choose the Right Strategy** - Use `LLMExtractionStrategy` for complex, unstructured content - Use `JsonCssExtractionStrategy` for well-structured HTML - Use `CosineStrategy` for content similarity and clustering
2. **Optimize Chunking**
```
# For long documents
strategy = LLMExtractionStrategy(
  chunk_token_threshold=2000, # Smaller chunks
  overlap_rate=0.1      # 10% overlap
)

```

3. **Handle Errors**
```
try:
  result = await crawler.arun(
    url="https://example.com",
    extraction_strategy=strategy
  )
  if result.success:
    content = json.loads(result.extracted_content)
except Exception as e:
  print(f"Extraction failed: {e}")

```

4. **Monitor Performance**
```
strategy = CosineStrategy(
  verbose=True, # Enable logging
  word_count_threshold=20, # Filter short content
  top_k=5 # Limit results
)

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
