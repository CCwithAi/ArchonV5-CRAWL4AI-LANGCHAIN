[ Skip to content ](https://ai.pydantic.dev/install/#installation)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Installation 
Type to start searching
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI") PydanticAI 
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
  * [ Introduction  ](https://ai.pydantic.dev/)
  * Installation  [ Installation  ](https://ai.pydantic.dev/install/) Table of contents 
    * [ Use with Pydantic Logfire  ](https://ai.pydantic.dev/install/#use-with-pydantic-logfire)
    * [ Running Examples  ](https://ai.pydantic.dev/install/#running-examples)
    * [ Slim Install  ](https://ai.pydantic.dev/install/#slim-install)
  * [ Getting Help  ](https://ai.pydantic.dev/help/)
  * [ Contributing  ](https://ai.pydantic.dev/contributing/)
  * [ Troubleshooting  ](https://ai.pydantic.dev/troubleshooting/)
  * Documentation  Documentation 
    * [ Agents  ](https://ai.pydantic.dev/agents/)
    * [ Models  ](https://ai.pydantic.dev/models/)
    * [ Dependencies  ](https://ai.pydantic.dev/dependencies/)
    * [ Function Tools  ](https://ai.pydantic.dev/tools/)
    * [ Common Tools  ](https://ai.pydantic.dev/common_tools/)
    * [ Results  ](https://ai.pydantic.dev/results/)
    * [ Messages and chat history  ](https://ai.pydantic.dev/message-history/)
    * [ Testing and Evals  ](https://ai.pydantic.dev/testing-evals/)
    * [ Debugging and Monitoring  ](https://ai.pydantic.dev/logfire/)
    * [ Multi-agent Applications  ](https://ai.pydantic.dev/multi-agent-applications/)
    * [ Graphs  ](https://ai.pydantic.dev/graph/)
    * [ Image, Audio & Document Input  ](https://ai.pydantic.dev/input/)
    * [ Command Line Interface (CLI)  ](https://ai.pydantic.dev/cli/)
  * [ Examples  ](https://ai.pydantic.dev/examples/)
Examples 
    * [ Pydantic Model  ](https://ai.pydantic.dev/examples/pydantic-model/)
    * [ Weather agent  ](https://ai.pydantic.dev/examples/weather-agent/)
    * [ Bank support  ](https://ai.pydantic.dev/examples/bank-support/)
    * [ SQL Generation  ](https://ai.pydantic.dev/examples/sql-gen/)
    * [ Flight booking  ](https://ai.pydantic.dev/examples/flight-booking/)
    * [ RAG  ](https://ai.pydantic.dev/examples/rag/)
    * [ Stream markdown  ](https://ai.pydantic.dev/examples/stream-markdown/)
    * [ Stream whales  ](https://ai.pydantic.dev/examples/stream-whales/)
    * [ Chat App with FastAPI  ](https://ai.pydantic.dev/examples/chat-app/)
    * [ Question Graph  ](https://ai.pydantic.dev/examples/question-graph/)
  * API Reference  API Reference 
    * [ pydantic_ai.agent  ](https://ai.pydantic.dev/api/agent/)
    * [ pydantic_ai.tools  ](https://ai.pydantic.dev/api/tools/)
    * [ pydantic_ai.common_tools  ](https://ai.pydantic.dev/api/common_tools/)
    * [ pydantic_ai.result  ](https://ai.pydantic.dev/api/result/)
    * [ pydantic_ai.messages  ](https://ai.pydantic.dev/api/messages/)
    * [ pydantic_ai.exceptions  ](https://ai.pydantic.dev/api/exceptions/)
    * [ pydantic_ai.settings  ](https://ai.pydantic.dev/api/settings/)
    * [ pydantic_ai.usage  ](https://ai.pydantic.dev/api/usage/)
    * [ pydantic_ai.format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/)
    * [ pydantic_ai.models  ](https://ai.pydantic.dev/api/models/base/)
    * [ pydantic_ai.models.openai  ](https://ai.pydantic.dev/api/models/openai/)
    * [ pydantic_ai.models.anthropic  ](https://ai.pydantic.dev/api/models/anthropic/)
    * [ pydantic_ai.models.bedrock  ](https://ai.pydantic.dev/api/models/bedrock/)
    * [ pydantic_ai.models.cohere  ](https://ai.pydantic.dev/api/models/cohere/)
    * [ pydantic_ai.models.gemini  ](https://ai.pydantic.dev/api/models/gemini/)
    * [ pydantic_ai.models.vertexai  ](https://ai.pydantic.dev/api/models/vertexai/)
    * [ pydantic_ai.models.groq  ](https://ai.pydantic.dev/api/models/groq/)
    * [ pydantic_ai.models.mistral  ](https://ai.pydantic.dev/api/models/mistral/)
    * [ pydantic_ai.models.test  ](https://ai.pydantic.dev/api/models/test/)
    * [ pydantic_ai.models.function  ](https://ai.pydantic.dev/api/models/function/)
    * [ pydantic_ai.models.fallback  ](https://ai.pydantic.dev/api/models/fallback/)
    * [ pydantic_ai.providers  ](https://ai.pydantic.dev/api/providers/)
    * [ pydantic_graph  ](https://ai.pydantic.dev/api/pydantic_graph/graph/)
    * [ pydantic_graph.nodes  ](https://ai.pydantic.dev/api/pydantic_graph/nodes/)
    * [ pydantic_graph.persistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/)
    * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)


Table of contents 
  * [ Use with Pydantic Logfire  ](https://ai.pydantic.dev/install/#use-with-pydantic-logfire)
  * [ Running Examples  ](https://ai.pydantic.dev/install/#running-examples)
  * [ Slim Install  ](https://ai.pydantic.dev/install/#slim-install)


# Installation
PydanticAI is available on PyPI as [`pydantic-ai`](https://pypi.org/project/pydantic-ai/) so installation is as simple as:
[pip](https://ai.pydantic.dev/install/#__tabbed_1_1)[uv](https://ai.pydantic.dev/install/#__tabbed_1_2)
```
pipinstallpydantic-ai

```

```
uvaddpydantic-ai

```

(Requires Python 3.9+)
This installs the `pydantic_ai` package, core dependencies, and libraries required to use all the models included in PydanticAI. If you want to use a specific model, you can install the ["slim"](https://ai.pydantic.dev/install/#slim-install) version of PydanticAI.
## Use with Pydantic Logfire
PydanticAI has an excellent (but completely optional) integration with [Pydantic Logfire](https://pydantic.dev/logfire) to help you view and understand agent runs.
To use Logfire with PydanticAI, install `pydantic-ai` or `pydantic-ai-slim` with the `logfire` optional group:
[pip](https://ai.pydantic.dev/install/#__tabbed_2_1)[uv](https://ai.pydantic.dev/install/#__tabbed_2_2)
```
pipinstall'pydantic-ai[logfire]'

```

```
uvadd'pydantic-ai[logfire]'

```

From there, follow the [Logfire setup docs](https://ai.pydantic.dev/logfire/#using-logfire) to configure Logfire.
## Running Examples
We distribute the [`pydantic_ai_examples`](https://github.com/pydantic/pydantic-ai/tree/main/examples/pydantic_ai_examples) directory as a separate PyPI package ([`pydantic-ai-examples`](https://pypi.org/project/pydantic-ai-examples/)) to make examples extremely easy to customize and run.
To install examples, use the `examples` optional group:
[pip](https://ai.pydantic.dev/install/#__tabbed_3_1)[uv](https://ai.pydantic.dev/install/#__tabbed_3_2)
```
pipinstall'pydantic-ai[examples]'

```

```
uvadd'pydantic-ai[examples]'

```

To run the examples, follow instructions in the [examples docs](https://ai.pydantic.dev/examples/).
## Slim Install
If you know which model you're going to use and want to avoid installing superfluous packages, you can use the [`pydantic-ai-slim`](https://pypi.org/project/pydantic-ai-slim/) package. For example, if you're using just [`OpenAIModel`](https://ai.pydantic.dev/api/models/openai/#pydantic_ai.models.openai.OpenAIModel), you would run:
[pip](https://ai.pydantic.dev/install/#__tabbed_4_1)[uv](https://ai.pydantic.dev/install/#__tabbed_4_2)
```
pipinstall'pydantic-ai-slim[openai]'

```

```
uvadd'pydantic-ai-slim[openai]'

```

`pydantic-ai-slim` has the following optional groups:
  * `logfire` — installs [`logfire`](https://ai.pydantic.dev/logfire/) [PyPI ↗](https://pypi.org/project/logfire)
  * `openai` — installs `openai` [PyPI ↗](https://pypi.org/project/openai)
  * `vertexai` — installs `google-auth` [PyPI ↗](https://pypi.org/project/google-auth) and `requests` [PyPI ↗](https://pypi.org/project/requests)
  * `anthropic` — installs `anthropic` [PyPI ↗](https://pypi.org/project/anthropic)
  * `groq` — installs `groq` [PyPI ↗](https://pypi.org/project/groq)
  * `mistral` — installs `mistralai` [PyPI ↗](https://pypi.org/project/mistralai)
  * `cohere` - installs `cohere` [PyPI ↗](https://pypi.org/project/cohere)
  * `duckduckgo` - installs `duckduckgo-search` [PyPI ↗](https://pypi.org/project/duckduckgo-search)
  * `tavily` - installs `tavily-python` [PyPI ↗](https://pypi.org/project/tavily-python)


See the [models](https://ai.pydantic.dev/models/) documentation for information on which optional dependencies are required for each model.
You can also install dependencies for multiple models and use cases, for example:
[pip](https://ai.pydantic.dev/install/#__tabbed_5_1)[uv](https://ai.pydantic.dev/install/#__tabbed_5_2)
```
pipinstall'pydantic-ai-slim[openai,vertexai,logfire]'

```

```
uvadd'pydantic-ai-slim[openai,vertexai,logfire]'

```

© Pydantic Services Inc. 2024 to present 
