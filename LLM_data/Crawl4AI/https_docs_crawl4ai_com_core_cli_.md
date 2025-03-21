[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/core/cli/)


  * [Home](https://docs.crawl4ai.com/)
  * Setup & Installation
    * [Installation](https://docs.crawl4ai.com/core/installation/)
    * [Docker Deployment](https://docs.crawl4ai.com/core/docker-deployment/)
  * [Quick Start](https://docs.crawl4ai.com/core/quickstart/)
  * Blog & Changelog
    * [Blog Home](https://docs.crawl4ai.com/blog/)
    * [Changelog](https://github.com/unclecode/crawl4ai/blob/main/CHANGELOG.md)
  * Core
    * Command Line Interface
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
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Crawl4AI CLI Guide](https://docs.crawl4ai.com/core/cli/#crawl4ai-cli-guide)
  * [Table of Contents](https://docs.crawl4ai.com/core/cli/#table-of-contents)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli/#basic-usage)
  * [Quick Example of Advanced Usage](https://docs.crawl4ai.com/core/cli/#quick-example-of-advanced-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli/#configuration)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli/#advanced-features)
  * [Output Formats](https://docs.crawl4ai.com/core/cli/#output-formats)
  * [Complete Examples](https://docs.crawl4ai.com/core/cli/#complete-examples)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli/#best-practices-tips)
  * [Recap](https://docs.crawl4ai.com/core/cli/#recap)


# Crawl4AI CLI Guide
## Table of Contents
  * [Installation](https://docs.crawl4ai.com/core/cli/#installation)
  * [Basic Usage](https://docs.crawl4ai.com/core/cli/#basic-usage)
  * [Configuration](https://docs.crawl4ai.com/core/cli/#configuration)
  * [Browser Configuration](https://docs.crawl4ai.com/core/cli/#browser-configuration)
  * [Crawler Configuration](https://docs.crawl4ai.com/core/cli/#crawler-configuration)
  * [Extraction Configuration](https://docs.crawl4ai.com/core/cli/#extraction-configuration)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli/#content-filtering)
  * [Advanced Features](https://docs.crawl4ai.com/core/cli/#advanced-features)
  * [LLM Q&A](https://docs.crawl4ai.com/core/cli/#llm-qa)
  * [Structured Data Extraction](https://docs.crawl4ai.com/core/cli/#structured-data-extraction)
  * [Content Filtering](https://docs.crawl4ai.com/core/cli/#content-filtering-1)
  * [Output Formats](https://docs.crawl4ai.com/core/cli/#output-formats)
  * [Examples](https://docs.crawl4ai.com/core/cli/#examples)
  * [Configuration Reference](https://docs.crawl4ai.com/core/cli/#configuration-reference)
  * [Best Practices & Tips](https://docs.crawl4ai.com/core/cli/#best-practices--tips)


## Basic Usage
The Crawl4AI CLI (`crwl`) provides a simple interface to the Crawl4AI library:
```
# Basic crawling
crwl https://example.com
# Get markdown output
crwl https://example.com -o markdown
# Verbose JSON output with cache bypass
crwl https://example.com -o json -v --bypass-cache
# See usage examples
crwl --example

```

## Quick Example of Advanced Usage
If you clone the repository and run the following command, you will receive the content of the page in JSON format according to a JSON-CSS schema:
```
crwl "https://www.infoq.com/ai-ml-data-eng/" -e docs/examples/cli/extract_css.yml -s docs/examples/cli/css_schema.json -o json;

```

## Configuration
### Browser Configuration
Browser settings can be configured via YAML file or command line parameters:
```
# browser.yml
headless: true
viewport_width: 1280
user_agent_mode: "random"
verbose: true
ignore_https_errors: true

```

```
# Using config file
crwl https://example.com -B browser.yml
# Using direct parameters
crwl https://example.com -b "headless=true,viewport_width=1280,user_agent_mode=random"

```

### Crawler Configuration
Control crawling behavior:
```
# crawler.yml
cache_mode: "bypass"
wait_until: "networkidle"
page_timeout: 30000
delay_before_return_html: 0.5
word_count_threshold: 100
scan_full_page: true
scroll_delay: 0.3
process_iframes: false
remove_overlay_elements: true
magic: true
verbose: true

```

```
# Using config file
crwl https://example.com -C crawler.yml
# Using direct parameters
crwl https://example.com -c "css_selector=#main,delay_before_return_html=2,scan_full_page=true"

```

### Extraction Configuration
Two types of extraction are supported:
  1. CSS/XPath-based extraction: 
```
# extract_css.yml
type: "json-css"
params:
 verbose: true

```



```
// css_schema.json
{
 "name": "ArticleExtractor",
 "baseSelector": ".article",
 "fields": [
  {
   "name": "title",
   "selector": "h1.title",
   "type": "text"
  },
  {
   "name": "link",
   "selector": "a.read-more",
   "type": "attribute",
   "attribute": "href"
  }
 ]
}

```

  1. LLM-based extraction: 
```
# extract_llm.yml
type: "llm"
provider: "openai/gpt-4"
instruction: "Extract all articles with their titles and links"
api_token: "your-token"
params:
 temperature: 0.3
 max_tokens: 1000

```



```
// llm_schema.json
{
 "title": "Article",
 "type": "object",
 "properties": {
  "title": {
   "type": "string",
   "description": "The title of the article"
  },
  "link": {
   "type": "string",
   "description": "URL to the full article"
  }
 }
}

```

## Advanced Features
### LLM Q&A
Ask questions about crawled content:
```
# Simple question
crwl https://example.com -q "What is the main topic discussed?"
# View content then ask questions
crwl https://example.com -o markdown # See content first
crwl https://example.com -q "Summarize the key points"
crwl https://example.com -q "What are the conclusions?"
# Combined with advanced crawling
crwl https://example.com \
  -B browser.yml \
  -c "css_selector=article,scan_full_page=true" \
  -q "What are the pros and cons mentioned?"

```

First-time setup: - Prompts for LLM provider and API token - Saves configuration in `~/.crawl4ai/global.yml` - Supports various providers (openai/gpt-4, anthropic/claude-3-sonnet, etc.) - For case of `ollama` you do not need to provide API token. - See [LiteLLM Providers](https://docs.litellm.ai/docs/providers) for full list
### Structured Data Extraction
Extract structured data using CSS selectors:
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json

```

Or using LLM-based extraction:
```
crwl https://example.com \
  -e extract_llm.yml \
  -s llm_schema.json \
  -o json

```

### Content Filtering
Filter content for relevance:
```
# filter_bm25.yml
type: "bm25"
query: "target content"
threshold: 1.0
# filter_pruning.yml
type: "pruning"
query: "focus topic"
threshold: 0.48

```

```
crwl https://example.com -f filter_bm25.yml -o markdown-fit

```

## Output Formats
  * `all` - Full crawl result including metadata
  * `json` - Extracted structured data (when using extraction)
  * `markdown` / `md` - Raw markdown output
  * `markdown-fit` / `md-fit` - Filtered markdown for better readability


## Complete Examples
  1. Basic Extraction: 
```
crwl https://example.com \
  -B browser.yml \
  -C crawler.yml \
  -o json

```

  2. Structured Data Extraction: 
```
crwl https://example.com \
  -e extract_css.yml \
  -s css_schema.json \
  -o json \
  -v

```

  3. LLM Extraction with Filtering: 
```
crwl https://example.com \
  -B browser.yml \
  -e extract_llm.yml \
  -s llm_schema.json \
  -f filter_bm25.yml \
  -o json

```

  4. Interactive Q&A: 
```
# First crawl and view
crwl https://example.com -o markdown
# Then ask questions
crwl https://example.com -q "What are the main points?"
crwl https://example.com -q "Summarize the conclusions"

```



## Best Practices & Tips
  1. **Configuration Management** :
  2. Keep common configurations in YAML files
  3. Use CLI parameters for quick overrides
  4. Store sensitive data (API tokens) in `~/.crawl4ai/global.yml`
  5. **Performance Optimization** :
  6. Use `--bypass-cache` for fresh content
  7. Enable `scan_full_page` for infinite scroll pages
  8. Adjust `delay_before_return_html` for dynamic content
  9. **Content Extraction** :
  10. Use CSS extraction for structured content
  11. Use LLM extraction for unstructured content
  12. Combine with filters for focused results
  13. **Q &A Workflow**:
  14. View content first with `-o markdown`
  15. Ask specific questions
  16. Use broader context with appropriate selectors


## Recap
The Crawl4AI CLI provides: - Flexible configuration via files and parameters - Multiple extraction strategies (CSS, XPath, LLM) - Content filtering and optimization - Interactive Q&A capabilities - Various output formats
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
