[Crawl4AI Documentation (v0.5.x)](https://docs.crawl4ai.com/)
  * [ Home ](https://docs.crawl4ai.com/)
  * [ Quick Start ](https://docs.crawl4ai.com/core/quickstart/)
  * [ Search ](https://docs.crawl4ai.com/basic/installation/)


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


  * [Installation 💻](https://docs.crawl4ai.com/basic/installation/#installation)
  * [Option 1: Python Package Installation (Recommended)](https://docs.crawl4ai.com/basic/installation/#option-1-python-package-installation-recommended)
  * [Playwright Installation Note for Ubuntu](https://docs.crawl4ai.com/basic/installation/#playwright-installation-note-for-ubuntu)
  * [Option 2: Using Docker (Coming Soon)](https://docs.crawl4ai.com/basic/installation/#option-2-using-docker-coming-soon)
  * [Option 3: Local Server Installation](https://docs.crawl4ai.com/basic/installation/#option-3-local-server-installation)
  * [Verifying Your Installation](https://docs.crawl4ai.com/basic/installation/#verifying-your-installation)
  * [Getting Help](https://docs.crawl4ai.com/basic/installation/#getting-help)


# Installation 💻
Crawl4AI offers flexible installation options to suit various use cases. You can install it as a Python package, use it with Docker, or run it as a local server.
## Option 1: Python Package Installation (Recommended)
Crawl4AI is now available on PyPI, making installation easier than ever. Choose the option that best fits your needs:
### Basic Installation
For basic web crawling and scraping tasks:
```
pip install crawl4ai
playwright install # Install Playwright dependencies

```

### Installation with PyTorch
For advanced text clustering (includes CosineSimilarity cluster strategy):
```
pip install crawl4ai[torch]

```

### Installation with Transformers
For text summarization and Hugging Face models:
```
pip install crawl4ai[transformer]

```

### Full Installation
For all features:
```
pip install crawl4ai[all]

```

### Development Installation
For contributors who plan to modify the source code:
```
git clone https://github.com/unclecode/crawl4ai.git
cd crawl4ai
pip install -e ".[all]"
playwright install # Install Playwright dependencies

```

💡 After installation with "torch", "transformer", or "all" options, it's recommended to run the following CLI command to load the required models:
```
crawl4ai-download-models

```

This is optional but will boost the performance and speed of the crawler. You only need to do this once after installation.
## Playwright Installation Note for Ubuntu
If you encounter issues with Playwright installation on Ubuntu, you may need to install additional dependencies:
```
sudo apt-get install -y \
  libwoff1 \
  libopus0 \
  libwebp7 \
  libwebpdemux2 \
  libenchant-2-2 \
  libgudev-1.0-0 \
  libsecret-1-0 \
  libhyphen0 \
  libgdk-pixbuf2.0-0 \
  libegl1 \
  libnotify4 \
  libxslt1.1 \
  libevent-2.1-7 \
  libgles2 \
  libxcomposite1 \
  libatk1.0-0 \
  libatk-bridge2.0-0 \
  libepoxy0 \
  libgtk-3-0 \
  libharfbuzz-icu0 \
  libgstreamer-gl1.0-0 \
  libgstreamer-plugins-bad1.0-0 \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  libxt6 \
  libxaw7 \
  xvfb \
  fonts-noto-color-emoji \
  libfontconfig \
  libfreetype6 \
  xfonts-cyrillic \
  xfonts-scalable \
  fonts-liberation \
  fonts-ipafont-gothic \
  fonts-wqy-zenhei \
  fonts-tlwg-loma-otf \
  fonts-freefont-ttf

```

## Option 2: Using Docker (Coming Soon)
Docker support for Crawl4AI is currently in progress and will be available soon. This will allow you to run Crawl4AI in a containerized environment, ensuring consistency across different systems.
## Option 3: Local Server Installation
For those who prefer to run Crawl4AI as a local server, instructions will be provided once the Docker implementation is complete.
## Verifying Your Installation
After installation, you can verify that Crawl4AI is working correctly by running a simple Python script:
```
import asyncio
from crawl4ai import AsyncWebCrawler
async def main():
  async with AsyncWebCrawler(verbose=True) as crawler:
    result = await crawler.arun(url="https://www.example.com")
    print(result.markdown[:500]) # Print first 500 characters
if __name__ == "__main__":
  asyncio.run(main())

```

This script should successfully crawl the example website and print the first 500 characters of the extracted content.
## Getting Help
If you encounter any issues during installation or usage, please check the [documentation](https://docs.crawl4ai.com/) or raise an issue on the [GitHub repository](https://github.com/unclecode/crawl4ai/issues).
Happy crawling! 🕷️🤖
Site built with [MkDocs](http://www.mkdocs.org) and [Terminal for MkDocs](https://github.com/ntno/mkdocs-terminal). 
##### Search
xClose
Type to start searching
