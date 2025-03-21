[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/advanced/advanced-features/)


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
    * Overview
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


  * [Overview of Some Important Advanced Features](https://docs.crawl4ai.com/advanced/advanced-features/#overview-of-some-important-advanced-features)
  * [1. Proxy Usage](https://docs.crawl4ai.com/advanced/advanced-features/#1-proxy-usage)
  * [2. Capturing PDFs & Screenshots](https://docs.crawl4ai.com/advanced/advanced-features/#2-capturing-pdfs-screenshots)
  * [3. Handling SSL Certificates](https://docs.crawl4ai.com/advanced/advanced-features/#3-handling-ssl-certificates)
  * [4. Custom Headers](https://docs.crawl4ai.com/advanced/advanced-features/#4-custom-headers)
  * [5. Session Persistence & Local Storage](https://docs.crawl4ai.com/advanced/advanced-features/#5-session-persistence-local-storage)
  * [6. Robots.txt Compliance](https://docs.crawl4ai.com/advanced/advanced-features/#6-robotstxt-compliance)
  * [Putting It All Together](https://docs.crawl4ai.com/advanced/advanced-features/#putting-it-all-together)
  * [Conclusion & Next Steps](https://docs.crawl4ai.com/advanced/advanced-features/#conclusion-next-steps)


# Overview of Some Important Advanced Features
(Proxy, PDF, Screenshot, SSL, Headers, & Storage State)
Crawl4AI offers multiple power-user features that go beyond simple crawling. This tutorial covers:
1. **Proxy Usage** 2. **Capturing PDFs & Screenshots** 3. **Handling SSL Certificates** 4. **Custom Headers** 5. **Session Persistence & Local Storage** 6. **Robots.txt Compliance**
> **Prerequisites** - You have a basic grasp of [AsyncWebCrawler Basics](https://docs.crawl4ai.com/core/simple-crawling/) - You know how to run or configure your Python environment with Playwright installed
## 1. Proxy Usage
If you need to route your crawl traffic through a proxy—whether for IP rotation, geo-testing, or privacy—Crawl4AI supports it via `BrowserConfig.proxy_config`.
```
import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
async def main():
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True
  )
  crawler_cfg = CrawlerRunConfig(
    verbose=True
  )
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url="https://www.whatismyip.com/",
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Page fetched via proxy.")
      print("Page HTML snippet:", result.html[:200])
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`proxy_config`**expects a dict with`server` and optional auth credentials. - Many commercial proxies provide an HTTP/HTTPS “gateway” server that you specify in `server`. - If your proxy doesn’t need auth, omit `username`/`password`.
## 2. Capturing PDFs & Screenshots
Sometimes you need a visual record of a page or a PDF “printout.” Crawl4AI can do both in one pass:
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, CacheMode
async def main():
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      url="https://en.wikipedia.org/wiki/List_of_common_misconceptions",
      cache_mode=CacheMode.BYPASS,
      pdf=True,
      screenshot=True
    )
    if result.success:
      # Save screenshot
      if result.screenshot:
        with open("wikipedia_screenshot.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Save PDF
      if result.pdf:
        with open("wikipedia_page.pdf", "wb") as f:
          f.write(result.pdf)
      print("[OK] PDF & screenshot captured.")
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

**Why PDF + Screenshot?** - Large or complex pages can be slow or error-prone with “traditional” full-page screenshots. - Exporting a PDF is more reliable for very long pages. Crawl4AI automatically converts the first PDF page into an image if you request both. 
**Relevant Parameters** - **`pdf=True`**: Exports the current page as a PDF (base64-encoded in`result.pdf`). - **`screenshot=True`**: Creates a screenshot (base64-encoded in`result.screenshot`). - **`scan_full_page`**or advanced hooking can further refine how the crawler captures content.
## 3. Handling SSL Certificates
If you need to verify or export a site’s SSL certificate—for compliance, debugging, or data analysis—Crawl4AI can fetch it during the crawl:
```
import asyncio, os
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
async def main():
  tmp_dir = os.path.join(os.getcwd(), "tmp")
  os.makedirs(tmp_dir, exist_ok=True)
  config = CrawlerRunConfig(
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url="https://example.com", config=config)
    if result.success and result.ssl_certificate:
      cert = result.ssl_certificate
      print("\nCertificate Information:")
      print(f"Issuer (CN): {cert.issuer.get('CN', '')}")
      print(f"Valid until: {cert.valid_until}")
      print(f"Fingerprint: {cert.fingerprint}")
      # Export in multiple formats:
      cert.to_json(os.path.join(tmp_dir, "certificate.json"))
      cert.to_pem(os.path.join(tmp_dir, "certificate.pem"))
      cert.to_der(os.path.join(tmp_dir, "certificate.der"))
      print("\nCertificate exported to JSON/PEM/DER in 'tmp' folder.")
    else:
      print("[ERROR] No certificate or crawl failed.")
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - **`fetch_ssl_certificate=True`**triggers certificate retrieval. -`result.ssl_certificate` includes methods (`to_json`, `to_pem`, `to_der`) for saving in various formats (handy for server config, Java keystores, etc.).
## 4. Custom Headers
Sometimes you need to set custom headers (e.g., language preferences, authentication tokens, or specialized user-agent strings). You can do this in multiple ways:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  # Option 1: Set headers at the crawler strategy level
  crawler1 = AsyncWebCrawler(
    # The underlying strategy can accept headers in its constructor
    crawler_strategy=None # We'll override below for clarity
  )
  crawler1.crawler_strategy.update_user_agent("MyCustomUA/1.0")
  crawler1.crawler_strategy.set_custom_headers({
    "Accept-Language": "fr-FR,fr;q=0.9"
  })
  result1 = await crawler1.arun("https://www.example.com")
  print("Example 1 result success:", result1.success)
  # Option 2: Pass headers directly to `arun()`
  crawler2 = AsyncWebCrawler()
  result2 = await crawler2.arun(
    url="https://www.example.com",
    headers={"Accept-Language": "es-ES,es;q=0.9"}
  )
  print("Example 2 result success:", result2.success)
if __name__ == "__main__":
  asyncio.run(main())

```

**Notes** - Some sites may react differently to certain headers (e.g., `Accept-Language`). - If you need advanced user-agent randomization or client hints, see [Identity-Based Crawling (Anti-Bot)](https://docs.crawl4ai.com/advanced/identity-based-crawling/) or use `UserAgentGenerator`.
## 5. Session Persistence & Local Storage
Crawl4AI can preserve cookies and localStorage so you can continue where you left off—ideal for logging into sites or skipping repeated auth flows.
### 5.1 `storage_state`
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  storage_dict = {
    "cookies": [
      {
        "name": "session",
        "value": "abcd1234",
        "domain": "example.com",
        "path": "/",
        "expires": 1699999999.0,
        "httpOnly": False,
        "secure": False,
        "sameSite": "None"
      }
    ],
    "origins": [
      {
        "origin": "https://example.com",
        "localStorage": [
          {"name": "token", "value": "my_auth_token"}
        ]
      }
    ]
  }
  # Provide the storage state as a dictionary to start "already logged in"
  async with AsyncWebCrawler(
    headless=True,
    storage_state=storage_dict
  ) as crawler:
    result = await crawler.arun("https://example.com/protected")
    if result.success:
      print("Protected page content length:", len(result.html))
    else:
      print("Failed to crawl protected page")
if __name__ == "__main__":
  asyncio.run(main())

```

### 5.2 Exporting & Reusing State
You can sign in once, export the browser context, and reuse it later—without re-entering credentials.
  * **`await context.storage_state(path="my_storage.json")`**: Exports cookies, localStorage, etc. to a file.
  * Provide `storage_state="my_storage.json"` on subsequent runs to skip the login step.


**See** : [Detailed session management tutorial](https://docs.crawl4ai.com/advanced/session-management/) or [Explanations → Browser Context & Managed Browser](https://docs.crawl4ai.com/advanced/identity-based-crawling/) for more advanced scenarios (like multi-step logins, or capturing after interactive pages).
## 6. Robots.txt Compliance
Crawl4AI supports respecting robots.txt rules with efficient caching:
```
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
async def main():
  # Enable robots.txt checking in config
  config = CrawlerRunConfig(
    check_robots_txt=True # Will check and respect robots.txt rules
  )
  async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(
      "https://example.com",
      config=config
    )
    if not result.success and result.status_code == 403:
      print("Access denied by robots.txt")
if __name__ == "__main__":
  asyncio.run(main())

```

**Key Points** - Robots.txt files are cached locally for efficiency - Cache is stored in `~/.crawl4ai/robots/robots_cache.db` - Cache has a default TTL of 7 days - If robots.txt can't be fetched, crawling is allowed - Returns 403 status code if URL is disallowed
## Putting It All Together
Here’s a snippet that combines multiple “advanced” features (proxy, PDF, screenshot, SSL, custom headers, and session reuse) into one run. Normally, you’d tailor each setting to your project’s needs.
```
import os, asyncio
from base64 import b64decode
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
async def main():
  # 1. Browser config with proxy + headless
  browser_cfg = BrowserConfig(
    proxy_config={
      "server": "http://proxy.example.com:8080",
      "username": "myuser",
      "password": "mypass",
    },
    headless=True,
  )
  # 2. Crawler config with PDF, screenshot, SSL, custom headers, and ignoring caches
  crawler_cfg = CrawlerRunConfig(
    pdf=True,
    screenshot=True,
    fetch_ssl_certificate=True,
    cache_mode=CacheMode.BYPASS,
    headers={"Accept-Language": "en-US,en;q=0.8"},
    storage_state="my_storage.json", # Reuse session from a previous sign-in
    verbose=True,
  )
  # 3. Crawl
  async with AsyncWebCrawler(config=browser_cfg) as crawler:
    result = await crawler.arun(
      url = "https://secure.example.com/protected", 
      config=crawler_cfg
    )
    if result.success:
      print("[OK] Crawled the secure page. Links found:", len(result.links.get("internal", [])))
      # Save PDF & screenshot
      if result.pdf:
        with open("result.pdf", "wb") as f:
          f.write(b64decode(result.pdf))
      if result.screenshot:
        with open("result.png", "wb") as f:
          f.write(b64decode(result.screenshot))
      # Check SSL cert
      if result.ssl_certificate:
        print("SSL Issuer CN:", result.ssl_certificate.issuer.get("CN", ""))
    else:
      print("[ERROR]", result.error_message)
if __name__ == "__main__":
  asyncio.run(main())

```

## Conclusion & Next Steps
You’ve now explored several **advanced** features:
  * **Proxy Usage**
  * **PDF & Screenshot** capturing for large or critical pages 
  * **SSL Certificate** retrieval & exporting 
  * **Custom Headers** for language or specialized requests 
  * **Session Persistence** via storage state
  * **Robots.txt Compliance**


With these power tools, you can build robust scraping workflows that mimic real user behavior, handle secure sites, capture detailed snapshots, and manage sessions across multiple runs—streamlining your entire data collection pipeline.
**Last Updated** : 2025-01-01
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
