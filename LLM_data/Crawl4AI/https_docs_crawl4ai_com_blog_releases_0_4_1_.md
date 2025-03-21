[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/blog/releases/0.4.1/)


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
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features!](https://docs.crawl4ai.com/blog/releases/0.4.1/#release-summary-for-version-041-december-8-2024-major-efficiency-boosts-with-new-features)
  * [Handling Lazy Loading Better (Images Included)](https://docs.crawl4ai.com/blog/releases/0.4.1/#handling-lazy-loading-better-images-included)
  * [Text-Only Mode (Fast, Lightweight Crawling)](https://docs.crawl4ai.com/blog/releases/0.4.1/#text-only-mode-fast-lightweight-crawling)
  * [Adjusting the Viewport Dynamically](https://docs.crawl4ai.com/blog/releases/0.4.1/#adjusting-the-viewport-dynamically)
  * [Simulating Full-Page Scrolling](https://docs.crawl4ai.com/blog/releases/0.4.1/#simulating-full-page-scrolling)
  * [Reusing Browser Sessions (Save Time on Setup)](https://docs.crawl4ai.com/blog/releases/0.4.1/#reusing-browser-sessions-save-time-on-setup)
  * [Other Updates](https://docs.crawl4ai.com/blog/releases/0.4.1/#other-updates)
  * [How to Get the Update](https://docs.crawl4ai.com/blog/releases/0.4.1/#how-to-get-the-update)


# Release Summary for Version 0.4.1 (December 8, 2024): Major Efficiency Boosts with New Features!
_This post was generated with the help of ChatGPT, take everything with a grain of salt. 🧂_
Hi everyone,
I just finished putting together version 0.4.1 of Crawl4AI, and there are a few changes in here that I think you’ll find really helpful. I’ll explain what’s new, why it matters, and exactly how you can use these features (with the code to back it up). Let’s get into it.
### Handling Lazy Loading Better (Images Included)
One thing that always bugged me with crawlers is how often they miss lazy-loaded content, especially images. In this version, I made sure Crawl4AI **waits for all images to load** before moving forward. This is useful because many modern websites only load images when they’re in the viewport or after some JavaScript executes.
Here’s how to enable it:
```
await crawler.crawl(
  url="https://example.com",
  wait_for_images=True # Add this argument to ensure images are fully loaded
)

```

What this does is: 1. Waits for the page to reach a "network idle" state. 2. Ensures all images on the page have been completely loaded.
This single change handles the majority of lazy-loading cases you’re likely to encounter.
### Text-Only Mode (Fast, Lightweight Crawling)
Sometimes, you don’t need to download images or process JavaScript at all. For example, if you’re crawling to extract text data, you can enable **text-only mode** to speed things up. By disabling images, JavaScript, and other heavy resources, this mode makes crawling **3-4 times faster** in most cases.
Here’s how to turn it on:
```
crawler = AsyncPlaywrightCrawlerStrategy(
  text_mode=True # Set this to True to enable text-only crawling
)

```

When `text_mode=True`, the crawler automatically: - Disables GPU processing. - Blocks image and JavaScript resources. - Reduces the viewport size to 800x600 (you can override this with `viewport_width` and `viewport_height`).
If you need to crawl thousands of pages where you only care about text, this mode will save you a ton of time and resources.
### Adjusting the Viewport Dynamically
Another useful addition is the ability to **dynamically adjust the viewport size** to match the content on the page. This is particularly helpful when you’re working with responsive layouts or want to ensure all parts of the page load properly.
Here’s how it works: 1. The crawler calculates the page’s width and height after it loads. 2. It adjusts the viewport to fit the content dimensions. 3. (Optional) It uses Chrome DevTools Protocol (CDP) to simulate zooming out so everything fits in the viewport.
To enable this, use:
```
await crawler.crawl(
  url="https://example.com",
  adjust_viewport_to_content=True # Dynamically adjusts the viewport
)

```

This approach makes sure the entire page gets loaded into the viewport, especially for layouts that load content based on visibility.
### Simulating Full-Page Scrolling
Some websites load data dynamically as you scroll down the page. To handle these cases, I added support for **full-page scanning**. It simulates scrolling to the bottom of the page, checking for new content, and capturing it all.
Here’s an example:
```
await crawler.crawl(
  url="https://example.com",
  scan_full_page=True,  # Enables scrolling
  scroll_delay=0.2    # Waits 200ms between scrolls (optional)
)

```

What happens here: 1. The crawler scrolls down in increments, waiting for content to load after each scroll. 2. It stops when no new content appears (i.e., dynamic elements stop loading). 3. It scrolls back to the top before finishing (if necessary).
If you’ve ever had to deal with infinite scroll pages, this is going to save you a lot of headaches.
### Reusing Browser Sessions (Save Time on Setup)
By default, every time you crawl a page, a new browser context (or tab) is created. That’s fine for small crawls, but if you’re working on a large dataset, it’s more efficient to reuse the same session.
I added a method called `create_session` for this:
```
session_id = await crawler.create_session()
# Use the same session for multiple crawls
await crawler.crawl(
  url="https://example.com/page1",
  session_id=session_id # Reuse the session
)
await crawler.crawl(
  url="https://example.com/page2",
  session_id=session_id
)

```

This avoids creating a new tab for every page, speeding up the crawl and reducing memory usage.
### Other Updates
Here are a few smaller updates I’ve made: - **Light Mode** : Use `light_mode=True` to disable background processes, extensions, and other unnecessary features, making the browser more efficient. - **Logging** : Improved logs to make debugging easier. - **Defaults** : Added sensible defaults for things like `delay_before_return_html` (now set to 0.1 seconds).
### How to Get the Update
You can install or upgrade to version `0.4.1` like this:
```
pip install crawl4ai --upgrade

```

As always, I’d love to hear your thoughts. If there’s something you think could be improved or if you have suggestions for future versions, let me know!
Enjoy the new features, and happy crawling! 🕷️
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
