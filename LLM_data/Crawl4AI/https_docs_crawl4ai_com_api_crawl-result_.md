[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/api/crawl-result/)


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
    * CrawlResult
    * [Strategies](https://docs.crawl4ai.com/api/strategies/)


  * [CrawlResult Reference](https://docs.crawl4ai.com/api/crawl-result/#crawlresult-reference)
  * [1. Basic Crawl Info](https://docs.crawl4ai.com/api/crawl-result/#1-basic-crawl-info)
  * [2. Raw / Cleaned Content](https://docs.crawl4ai.com/api/crawl-result/#2-raw-cleaned-content)
  * [3. Markdown Fields](https://docs.crawl4ai.com/api/crawl-result/#3-markdown-fields)
  * [4. Media & Links](https://docs.crawl4ai.com/api/crawl-result/#4-media-links)
  * [5. Additional Fields](https://docs.crawl4ai.com/api/crawl-result/#5-additional-fields)
  * [6. dispatch_result (optional)](https://docs.crawl4ai.com/api/crawl-result/#6-dispatch_result-optional)
  * [7. Example: Accessing Everything](https://docs.crawl4ai.com/api/crawl-result/#7-example-accessing-everything)
  * [8. Key Points & Future](https://docs.crawl4ai.com/api/crawl-result/#8-key-points-future)


# `CrawlResult` Reference
The **`CrawlResult`**class encapsulates everything returned after a single crawl operation. It provides the**raw or processed content** , details on links and media, plus optional metadata (like screenshots, PDFs, or extracted JSON).
**Location** : `crawl4ai/crawler/models.py` (for reference)
```
class CrawlResult(BaseModel):
  url: str
  html: str
  success: bool
  cleaned_html: Optional[str] = None
  media: Dict[str, List[Dict]] = {}
  links: Dict[str, List[Dict]] = {}
  downloaded_files: Optional[List[str]] = None
  screenshot: Optional[str] = None
  pdf : Optional[bytes] = None
  markdown: Optional[Union[str, MarkdownGenerationResult]] = None
  extracted_content: Optional[str] = None
  metadata: Optional[dict] = None
  error_message: Optional[str] = None
  session_id: Optional[str] = None
  response_headers: Optional[dict] = None
  status_code: Optional[int] = None
  ssl_certificate: Optional[SSLCertificate] = None
  dispatch_result: Optional[DispatchResult] = None
  ...

```

Below is a **field-by-field** explanation and possible usage patterns.
## 1. Basic Crawl Info
### 1.1 **`url`**_(str)_
**What** : The final crawled URL (after any redirects). **Usage** : 
```
print(result.url) # e.g., "https://example.com/"

```

### 1.2 **`success`**_(bool)_
**What** : `True` if the crawl pipeline ended without major errors; `False` otherwise. **Usage** : 
```
if not result.success:
  print(f"Crawl failed: {result.error_message}")

```

### 1.3 **`status_code`**_(Optional[int])_
**What** : The page’s HTTP status code (e.g., 200, 404). **Usage** : 
```
if result.status_code == 404:
  print("Page not found!")

```

### 1.4 **`error_message`**_(Optional[str])_
**What** : If `success=False`, a textual description of the failure. **Usage** : 
```
if not result.success:
  print("Error:", result.error_message)

```

### 1.5 **`session_id`**_(Optional[str])_
**What** : The ID used for reusing a browser context across multiple calls. **Usage** : 
```
# If you used session_id="login_session" in CrawlerRunConfig, see it here:
print("Session:", result.session_id)

```

### 1.6 **`response_headers`**_(Optional[dict])_
**What** : Final HTTP response headers. **Usage** : 
```
if result.response_headers:
  print("Server:", result.response_headers.get("Server", "Unknown"))

```

### 1.7 **`ssl_certificate`**_(Optional[SSLCertificate])_
**What** : If `fetch_ssl_certificate=True` in your CrawlerRunConfig, **`result.ssl_certificate`**contains a[**`SSLCertificate`**](https://docs.crawl4ai.com/advanced/ssl-certificate/)object describing the site’s certificate. You can export the cert in multiple formats (PEM/DER/JSON) or access its properties like`issuer`, `subject`, `valid_from`, `valid_until`, etc. **Usage** : 
```
if result.ssl_certificate:
  print("Issuer:", result.ssl_certificate.issuer)

```

## 2. Raw / Cleaned Content
### 2.1 **`html`**_(str)_
**What** : The **original** unmodified HTML from the final page load. **Usage** : 
```
# Possibly large
print(len(result.html))

```

### 2.2 **`cleaned_html`**_(Optional[str])_
**What** : A sanitized HTML version—scripts, styles, or excluded tags are removed based on your `CrawlerRunConfig`. **Usage** : 
```
print(result.cleaned_html[:500]) # Show a snippet

```

### 2.3 **`fit_html`**_(Optional[str])_
**What** : If a **content filter** or heuristic (e.g., Pruning/BM25) modifies the HTML, the “fit” or post-filter version. **When** : This is **only** present if your `markdown_generator` or `content_filter` produces it. **Usage** : 
```
if result.markdown.fit_html:
  print("High-value HTML content:", result.markdown.fit_html[:300])

```

## 3. Markdown Fields
### 3.1 The Markdown Generation Approach
Crawl4AI can convert HTML→Markdown, optionally including:
  * **Raw** markdown 
  * **Links as citations** (with a references section) 
  * **Fit** markdown if a **content filter** is used (like Pruning or BM25)


**`MarkdownGenerationResult`**includes: -**`raw_markdown`**_(str)_ : The full HTML→Markdown conversion. - **`markdown_with_citations`**_(str)_ : Same markdown, but with link references as academic-style citations. - **`references_markdown`**_(str)_ : The reference list or footnotes at the end. - **`fit_markdown`**_(Optional[str])_ : If content filtering (Pruning/BM25) was applied, the filtered “fit” text. - **`fit_html`**_(Optional[str])_ : The HTML that led to `fit_markdown`.
**Usage** : 
```
if result.markdown:
  md_res = result.markdown
  print("Raw MD:", md_res.raw_markdown[:300])
  print("Citations MD:", md_res.markdown_with_citations[:300])
  print("References:", md_res.references_markdown)
  if md_res.fit_markdown:
    print("Pruned text:", md_res.fit_markdown[:300])

```

### 3.2 **`markdown`**_(Optional[Union[str, MarkdownGenerationResult]])_
**What** : Holds the `MarkdownGenerationResult`. **Usage** : 
```
print(result.markdown.raw_markdown[:200])
print(result.markdown.fit_markdown)
print(result.markdown.fit_html)

```

**Important** : “Fit” content (in `fit_markdown`/`fit_html`) exists in result.markdown, only if you used a **filter** (like **PruningContentFilter** or **BM25ContentFilter**) within a `MarkdownGenerationStrategy`. 
## 4. Media & Links
### 4.1 **`media`**_(Dict[str, List[Dict]])_
**What** : Contains info about discovered images, videos, or audio. Typically keys: `"images"`, `"videos"`, `"audios"`. **Common Fields** in each item:
  * `src` _(str)_ : Media URL 
  * `alt` or `title` _(str)_ : Descriptive text 
  * `score` _(float)_ : Relevance score if the crawler’s heuristic found it “important” 
  * `desc` or `description` _(Optional[str])_ : Additional context extracted from surrounding text 


**Usage** : 
```
images = result.media.get("images", [])
for img in images:
  if img.get("score", 0) > 5:
    print("High-value image:", img["src"])

```

### 4.2 **`links`**_(Dict[str, List[Dict]])_
**What** : Holds internal and external link data. Usually two keys: `"internal"` and `"external"`. **Common Fields** :
  * `href` _(str)_ : The link target 
  * `text` _(str)_ : Link text 
  * `title` _(str)_ : Title attribute 
  * `context` _(str)_ : Surrounding text snippet 
  * `domain` _(str)_ : If external, the domain


**Usage** : 
```
for link in result.links["internal"]:
  print(f"Internal link to {link['href']} with text {link['text']}")

```

## 5. Additional Fields
### 5.1 **`extracted_content`**_(Optional[str])_
**What** : If you used **`extraction_strategy`**(CSS, LLM, etc.), the structured output (JSON).**Usage** : 
```
if result.extracted_content:
  data = json.loads(result.extracted_content)
  print(data)

```

### 5.2 **`downloaded_files`**_(Optional[List[str]])_
**What** : If `accept_downloads=True` in your `BrowserConfig` + `downloads_path`, lists local file paths for downloaded items. **Usage** : 
```
if result.downloaded_files:
  for file_path in result.downloaded_files:
    print("Downloaded:", file_path)

```

### 5.3 **`screenshot`**_(Optional[str])_
**What** : Base64-encoded screenshot if `screenshot=True` in `CrawlerRunConfig`. **Usage** : 
```
import base64
if result.screenshot:
  with open("page.png", "wb") as f:
    f.write(base64.b64decode(result.screenshot))

```

### 5.4 **`pdf`**_(Optional[bytes])_
**What** : Raw PDF bytes if `pdf=True` in `CrawlerRunConfig`. **Usage** : 
```
if result.pdf:
  with open("page.pdf", "wb") as f:
    f.write(result.pdf)

```

### 5.5 **`metadata`**_(Optional[dict])_
**What** : Page-level metadata if discovered (title, description, OG data, etc.). **Usage** : 
```
if result.metadata:
  print("Title:", result.metadata.get("title"))
  print("Author:", result.metadata.get("author"))

```

## 6. `dispatch_result` (optional)
A `DispatchResult` object providing additional concurrency and resource usage information when crawling URLs in parallel (e.g., via `arun_many()` with custom dispatchers). It contains:
  * **`task_id`**: A unique identifier for the parallel task.
  * **`memory_usage`**(float): The memory (in MB) used at the time of completion.
  * **`peak_memory`**(float): The peak memory usage (in MB) recorded during the task’s execution.
  * **`start_time`**/**`end_time`**(datetime): Time range for this crawling task.
  * **`error_message`**(str): Any dispatcher- or concurrency-related error encountered.


```
# Example usage:
for result in results:
  if result.success and result.dispatch_result:
    dr = result.dispatch_result
    print(f"URL: {result.url}, Task ID: {dr.task_id}")
    print(f"Memory: {dr.memory_usage:.1f} MB (Peak: {dr.peak_memory:.1f} MB)")
    print(f"Duration: {dr.end_time - dr.start_time}")

```

> **Note** : This field is typically populated when using `arun_many(...)` alongside a **dispatcher** (e.g., `MemoryAdaptiveDispatcher` or `SemaphoreDispatcher`). If no concurrency or dispatcher is used, `dispatch_result` may remain `None`. 
## 7. Example: Accessing Everything
```
async def handle_result(result: CrawlResult):
  if not result.success:
    print("Crawl error:", result.error_message)
    return
  # Basic info
  print("Crawled URL:", result.url)
  print("Status code:", result.status_code)
  # HTML
  print("Original HTML size:", len(result.html))
  print("Cleaned HTML size:", len(result.cleaned_html or ""))
  # Markdown output
  if result.markdown:
    print("Raw Markdown:", result.markdown.raw_markdown[:300])
    print("Citations Markdown:", result.markdown.markdown_with_citations[:300])
    if result.markdown.fit_markdown:
      print("Fit Markdown:", result.markdown.fit_markdown[:200])
  # Media & Links
  if "images" in result.media:
    print("Image count:", len(result.media["images"]))
  if "internal" in result.links:
    print("Internal link count:", len(result.links["internal"]))
  # Extraction strategy result
  if result.extracted_content:
    print("Structured data:", result.extracted_content)
  # Screenshot/PDF
  if result.screenshot:
    print("Screenshot length:", len(result.screenshot))
  if result.pdf:
    print("PDF bytes length:", len(result.pdf))

```

## 8. Key Points & Future
1. **Deprecated legacy properties of CrawlResult** - `markdown_v2` - Deprecated in v0.5. Just use `markdown`. It holds the `MarkdownGenerationResult` now! - `fit_markdown` and `fit_html` - Deprecated in v0.5. They can now be accessed via `MarkdownGenerationResult` in `result.markdown`. eg: `result.markdown.fit_markdown` and `result.markdown.fit_html`
2. **Fit Content** - **`fit_markdown`**and**`fit_html`**appear in MarkdownGenerationResult, only if you used a content filter (like**PruningContentFilter** or **BM25ContentFilter**) inside your **MarkdownGenerationStrategy** or set them directly. - If no filter is used, they remain `None`.
3. **References & Citations** - If you enable link citations in your `DefaultMarkdownGenerator` (`options={"citations": True}`), you’ll see `markdown_with_citations` plus a **`references_markdown`**block. This helps large language models or academic-like referencing.
4. **Links & Media** - `links["internal"]` and `links["external"]` group discovered anchors by domain. - `media["images"]` / `["videos"]` / `["audios"]` store extracted media elements with optional scoring or context.
5. **Error Cases** - If `success=False`, check `error_message` (e.g., timeouts, invalid URLs). - `status_code` might be `None` if we failed before an HTTP response.
Use **`CrawlResult`**to glean all final outputs and feed them into your data pipelines, AI models, or archives. With the synergy of a properly configured**BrowserConfig** and **CrawlerRunConfig** , the crawler can produce robust, structured results here in **`CrawlResult`**.
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
