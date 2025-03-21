[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/simple-crawling/)


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
    * Simple Crawling
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
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Simple Crawling](https://docs.crawl4ai.com/core/simple-crawling/#simple-crawling)
  * [Basic Usage](https://docs.crawl4ai.com/core/simple-crawling/#basic-usage)
  * [Understanding the Response](https://docs.crawl4ai.com/core/simple-crawling/#understanding-the-response)
  * [Adding Basic Options](https://docs.crawl4ai.com/core/simple-crawling/#adding-basic-options)
  * [Handling Errors](https://docs.crawl4ai.com/core/simple-crawling/#handling-errors)
  * [Logging and Debugging](https://docs.crawl4ai.com/core/simple-crawling/#logging-and-debugging)
  * [Complete Example](https://docs.crawl4ai.com/core/simple-crawling/#complete-example)


# Simple Crawling
This guide covers the basics of web crawling with Crawl4AI. You'll learn how to set up a crawler, make your first request, and understand the response.
## Basic Usage
Set up a simple crawl using `BrowserConfig` and `CrawlerRunConfig`:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async def main():
  browser_config = BrowserConfig() # Default browser configuration
  run_config = CrawlerRunConfig()  # Default crawl run configuration
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    print(result.markdown) # Print clean markdown content
if __name__ == "__main__":
  asyncio.run(main())

```

## Understanding the Response
The `arun()` method returns a `CrawlResult` object with several useful properties. Here's a quick overview (see [CrawlResult](https://docs.crawl4ai.com/api/crawl-result/) for complete details):
```
result = await crawler.arun(
  url="https://example.com",
  config=CrawlerRunConfig(fit_markdown=True)
)
# Different content formats
print(result.html)     # Raw HTML
print(result.cleaned_html) # Cleaned HTML
print(result.markdown.raw_markdown) # Raw markdown from cleaned html
print(result.markdown.fit_markdown) # Most relevant content in markdown
# Check success status
print(result.success)   # True if crawl succeeded
print(result.status_code) # HTTP status code (e.g., 200, 404)
# Access extracted media and links
print(result.media)    # Dictionary of found media (images, videos, audio)
print(result.links)    # Dictionary of internal and external links

```

## Adding Basic Options
Customize your crawl using `CrawlerRunConfig`:
```
run_config = CrawlerRunConfig(
  word_count_threshold=10,    # Minimum words per content block
  exclude_external_links=True,  # Remove external links
  remove_overlay_elements=True,  # Remove popups/modals
  process_iframes=True      # Process iframe content
)
result = await crawler.arun(
  url="https://example.com",
  config=run_config
)

```

## Handling Errors
Always check if the crawl was successful:
```
run_config = CrawlerRunConfig()
result = await crawler.arun(url="https://example.com", config=run_config)
if not result.success:
  print(f"Crawl failed: {result.error_message}")
  print(f"Status code: {result.status_code}")

```

## Logging and Debugging
Enable verbose logging in `BrowserConfig`:
```
browser_config = BrowserConfig(verbose=True)
async with AsyncWebCrawler(config=browser_config) as crawler:
  run_config = CrawlerRunConfig()
  result = await crawler.arun(url="https://example.com", config=run_config)

```

## Complete Example
Here's a more comprehensive example demonstrating common usage patterns:
```
import asyncio
from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  browser_config = BrowserConfig(verbose=True)
  run_config = CrawlerRunConfig(
    # Content filtering
    word_count_threshold=10,
    excluded_tags=['form', 'header'],
    exclude_external_links=True,
    # Content processing
    process_iframes=True,
    remove_overlay_elements=True,
    # Cache control
    cache_mode=CacheMode.ENABLED # Use cache if available
  )
  async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun(
      url="https://example.com",
      config=run_config
    )
    if result.success:
      # Print clean content
      print("Content:", result.markdown[:500]) # First 500 chars
      # Process images
      for image in result.media["images"]:
        print(f"Found image: {image['src']}")
      # Process links
      for link in result.links["internal"]:
        print(f"Internal link: {link['href']}")
    else:
      print(f"Crawl failed: {result.error_message}")
if __name__ == "__main__":
  asyncio.run(main())

```

Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
