[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/session-management/)


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
    * Session Management
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


  * [Session Management](https://docs.crawl4ai.com/advanced/session-management/#session-management)
  * [Basic Session Usage](https://docs.crawl4ai.com/advanced/session-management/#basic-session-usage)
  * [Dynamic Content with Sessions](https://docs.crawl4ai.com/advanced/session-management/#dynamic-content-with-sessions)
  * [Example 1: Basic Session-Based Crawling](https://docs.crawl4ai.com/advanced/session-management/#example-1-basic-session-based-crawling)
  * [Advanced Technique 1: Custom Execution Hooks](https://docs.crawl4ai.com/advanced/session-management/#advanced-technique-1-custom-execution-hooks)
  * [Advanced Technique 2: Integrated JavaScript Execution and Waiting](https://docs.crawl4ai.com/advanced/session-management/#advanced-technique-2-integrated-javascript-execution-and-waiting)


# Session Management
Session management in Crawl4AI is a powerful feature that allows you to maintain state across multiple requests, making it particularly suitable for handling complex multi-step crawling tasks. It enables you to reuse the same browser tab (or page object) across sequential actions and crawls, which is beneficial for:
  * **Performing JavaScript actions before and after crawling.**
  * **Executing multiple sequential crawls faster** without needing to reopen tabs or allocate memory repeatedly.


**Note:** This feature is designed for sequential workflows and is not suitable for parallel operations.
#### Basic Session Usage
Use `BrowserConfig` and `CrawlerRunConfig` to maintain state with a `session_id`:
```
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
async with AsyncWebCrawler() as crawler:
  session_id = "my_session"
  # Define configurations
  config1 = CrawlerRunConfig(
    url="https://example.com/page1", session_id=session_id
  )
  config2 = CrawlerRunConfig(
    url="https://example.com/page2", session_id=session_id
  )
  # First request
  result1 = await crawler.arun(config=config1)
  # Subsequent request using the same session
  result2 = await crawler.arun(config=config2)
  # Clean up when done
  await crawler.crawler_strategy.kill_session(session_id)

```

#### Dynamic Content with Sessions
Here's an example of crawling GitHub commits across multiple pages while preserving session state:
```
from crawl4ai.async_configs import CrawlerRunConfig
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from crawl4ai.cache_context import CacheMode
async def crawl_dynamic_content():
  async with AsyncWebCrawler() as crawler:
    session_id = "github_commits_session"
    url = "https://github.com/microsoft/TypeScript/commits/main"
    all_commits = []
    # Define extraction schema
    schema = {
      "name": "Commit Extractor",
      "baseSelector": "li.Box-sc-g0xbh4-0",
      "fields": [{
        "name": "title", "selector": "h4.markdown-title", "type": "text"
      }],
    }
    extraction_strategy = JsonCssExtractionStrategy(schema)
    # JavaScript and wait configurations
    js_next_page = """document.querySelector('a[data-testid="pagination-next-button"]').click();"""
    wait_for = """() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"""
    # Crawl multiple pages
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        extraction_strategy=extraction_strategy,
        js_code=js_next_page if page > 0 else None,
        wait_for=wait_for if page > 0 else None,
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      if result.success:
        commits = json.loads(result.extracted_content)
        all_commits.extend(commits)
        print(f"Page {page + 1}: Found {len(commits)} commits")
    # Clean up session
    await crawler.crawler_strategy.kill_session(session_id)
    return all_commits

```

## Example 1: Basic Session-Based Crawling
A simple example using session-based crawling:
```
import asyncio
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.cache_context import CacheMode
async def basic_session_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "dynamic_content_session"
    url = "https://example.com/dynamic-content"
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code="document.querySelector('.load-more-button').click();" if page > 0 else None,
        css_selector=".content-item",
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {result.extracted_content.count('.content-item')} items")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(basic_session_crawl())

```

This example shows: 1. Reusing the same `session_id` across multiple requests. 2. Executing JavaScript to load more content dynamically. 3. Properly closing the session to free resources.
## Advanced Technique 1: Custom Execution Hooks
> Warning: You might feel confused by the end of the next few examples 😅, so make sure you are comfortable with the order of the parts before you start this.
Use custom hooks to handle complex scenarios, such as waiting for content to load dynamically:
```
async def advanced_session_crawl_with_hooks():
  first_commit = ""
  async def on_execution_started(page):
    nonlocal first_commit
    try:
      while True:
        await page.wait_for_selector("li.commit-item h4")
        commit = await page.query_selector("li.commit-item h4")
        commit = await commit.evaluate("(element) => element.textContent").strip()
        if commit and commit != first_commit:
          first_commit = commit
          break
        await asyncio.sleep(0.5)
    except Exception as e:
      print(f"Warning: New content didn't appear: {e}")
  async with AsyncWebCrawler() as crawler:
    session_id = "commit_session"
    url = "https://github.com/example/repo/commits/main"
    crawler.crawler_strategy.set_hook("on_execution_started", on_execution_started)
    js_next_page = """document.querySelector('a.pagination-next').click();"""
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(advanced_session_crawl_with_hooks())

```

This technique ensures new content loads before the next action.
## Advanced Technique 2: Integrated JavaScript Execution and Waiting
Combine JavaScript execution and waiting logic for concise handling of dynamic content:
```
async def integrated_js_and_wait_crawl():
  async with AsyncWebCrawler() as crawler:
    session_id = "integrated_session"
    url = "https://github.com/example/repo/commits/main"
    js_next_page_and_wait = """
    (async () => {
      const getCurrentCommit = () => document.querySelector('li.commit-item h4').textContent.trim();
      const initialCommit = getCurrentCommit();
      document.querySelector('a.pagination-next').click();
      while (getCurrentCommit() === initialCommit) {
        await new Promise(resolve => setTimeout(resolve, 100));
      }
    })();
    """
    for page in range(3):
      config = CrawlerRunConfig(
        url=url,
        session_id=session_id,
        js_code=js_next_page_and_wait if page > 0 else None,
        css_selector="li.commit-item",
        js_only=page > 0,
        cache_mode=CacheMode.BYPASS
      )
      result = await crawler.arun(config=config)
      print(f"Page {page + 1}: Found {len(result.extracted_content)} commits")
    await crawler.crawler_strategy.kill_session(session_id)
asyncio.run(integrated_js_and_wait_crawl())

```

#### Common Use Cases for Sessions
1. **Authentication Flows** : Login and interact with secured pages.
2. **Pagination Handling** : Navigate through multiple pages.
3. **Form Submissions** : Fill forms, submit, and process results.
4. **Multi-step Processes** : Complete workflows that span multiple actions.
5. **Dynamic Content Navigation** : Handle JavaScript-rendered or event-triggered content.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
