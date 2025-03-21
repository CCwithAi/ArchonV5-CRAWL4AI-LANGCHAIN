[ Skip to content ](https://ai.pydantic.dev/troubleshooting/#troubleshooting)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Troubleshooting 
Type to start searching
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI") PydanticAI 
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
  * [ Introduction  ](https://ai.pydantic.dev/)
  * [ Installation  ](https://ai.pydantic.dev/install/)
  * [ Getting Help  ](https://ai.pydantic.dev/help/)
  * [ Contributing  ](https://ai.pydantic.dev/contributing/)
  * Troubleshooting  [ Troubleshooting  ](https://ai.pydantic.dev/troubleshooting/) Table of contents 
    * [ Jupyter Notebook Errors  ](https://ai.pydantic.dev/troubleshooting/#jupyter-notebook-errors)
      * [ RuntimeError: This event loop is already running  ](https://ai.pydantic.dev/troubleshooting/#runtimeerror-this-event-loop-is-already-running)
    * [ API Key Configuration  ](https://ai.pydantic.dev/troubleshooting/#api-key-configuration)
      * [ UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable  ](https://ai.pydantic.dev/troubleshooting/#usererror-api-key-must-be-provided-or-set-in-the-model_api_key-environment-variable)
    * [ Monitoring HTTPX Requests  ](https://ai.pydantic.dev/troubleshooting/#monitoring-httpx-requests)
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
  * [ Jupyter Notebook Errors  ](https://ai.pydantic.dev/troubleshooting/#jupyter-notebook-errors)
    * [ RuntimeError: This event loop is already running  ](https://ai.pydantic.dev/troubleshooting/#runtimeerror-this-event-loop-is-already-running)
  * [ API Key Configuration  ](https://ai.pydantic.dev/troubleshooting/#api-key-configuration)
    * [ UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable  ](https://ai.pydantic.dev/troubleshooting/#usererror-api-key-must-be-provided-or-set-in-the-model_api_key-environment-variable)
  * [ Monitoring HTTPX Requests  ](https://ai.pydantic.dev/troubleshooting/#monitoring-httpx-requests)


# Troubleshooting
Below are suggestions on how to fix some common errors you might encounter while using PydanticAI. If the issue you're experiencing is not listed below or addressed in the documentation, please feel free to ask in the [Pydantic Slack](https://ai.pydantic.dev/help/) or create an issue on [GitHub](https://github.com/pydantic/pydantic-ai/issues).
## Jupyter Notebook Errors
### `RuntimeError: This event loop is already running`
This error is caused by conflicts between the event loops in Jupyter notebook and PydanticAI's. One way to manage these conflicts is by using [`nest-asyncio`](https://pypi.org/project/nest-asyncio/). Namely, before you execute any agent runs, do the following: 
```
importnest_asyncio
nest_asyncio.apply()

```

Note: This fix also applies to Google Colab. 
## API Key Configuration
### `UserError: API key must be provided or set in the [MODEL]_API_KEY environment variable`
If you're running into issues with setting the API key for your model, visit the [Models](https://ai.pydantic.dev/models/) page to learn more about how to set an environment variable and/or pass in an `api_key` argument.
## Monitoring HTTPX Requests
You can use custom `httpx` clients in your models in order to access specific requests, responses, and headers at runtime.
It's particularly helpful to use `logfire`'s [HTTPX integration](https://ai.pydantic.dev/logfire/#monitoring-httpx-requests) to monitor the above.
© Pydantic Services Inc. 2024 to present 
