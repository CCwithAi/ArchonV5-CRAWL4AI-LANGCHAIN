[ Skip to content ](https://ai.pydantic.dev/examples/#examples)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Examples 
Type to start searching
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI") PydanticAI 
[ pydantic/pydantic-ai  ](https://github.com/pydantic/pydantic-ai "Go to repository")
  * [ Introduction  ](https://ai.pydantic.dev/)
  * [ Installation  ](https://ai.pydantic.dev/install/)
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
  * [ Usage  ](https://ai.pydantic.dev/examples/#usage)
    * [ Installing required dependencies  ](https://ai.pydantic.dev/examples/#installing-required-dependencies)
    * [ Setting model environment variables  ](https://ai.pydantic.dev/examples/#setting-model-environment-variables)
    * [ Running Examples  ](https://ai.pydantic.dev/examples/#running-examples)


# Examples
Examples of how to use PydanticAI and what it can do.
## Usage
These examples are distributed with `pydantic-ai` so you can run them either by cloning the [pydantic-ai repo](https://github.com/pydantic/pydantic-ai) or by simply installing `pydantic-ai` from PyPI with `pip` or `uv`.
### Installing required dependencies
Either way you'll need to install extra dependencies to run some examples, you just need to install the `examples` optional dependency group.
If you've installed `pydantic-ai` via pip/uv, you can install the extra dependencies with:
[pip](https://ai.pydantic.dev/examples/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/#__tabbed_1_2)
```
pipinstall'pydantic-ai[examples]'

```

```
uvadd'pydantic-ai[examples]'

```

If you clone the repo, you should instead use `uv sync --extra examples` to install extra dependencies.
### Setting model environment variables
These examples will need you to set up authentication with one or more of the LLMs, see the [model configuration](https://ai.pydantic.dev/models/) docs for details on how to do this.
TL;DR: in most cases you'll need to set one of the following environment variables:
[OpenAI](https://ai.pydantic.dev/examples/#__tabbed_2_1)[Google Gemini](https://ai.pydantic.dev/examples/#__tabbed_2_2)
```
exportOPENAI_API_KEY=your-api-key

```

```
exportGEMINI_API_KEY=your-api-key

```

### Running Examples
To run the examples (this will work whether you installed `pydantic_ai`, or cloned the repo), run:
[pip](https://ai.pydantic.dev/examples/#__tabbed_3_1)[uv](https://ai.pydantic.dev/examples/#__tabbed_3_2)
```
python-mpydantic_ai_examples.<example_module_name>

```

```
uvrun-mpydantic_ai_examples.<example_module_name>

```

For examples, to run the very simple [`pydantic_model`](https://ai.pydantic.dev/examples/pydantic-model/) example:
[pip](https://ai.pydantic.dev/examples/#__tabbed_4_1)[uv](https://ai.pydantic.dev/examples/#__tabbed_4_2)
```
python-mpydantic_ai_examples.pydantic_model

```

```
uvrun-mpydantic_ai_examples.pydantic_model

```

If you like one-liners and you're using uv, you can run a pydantic-ai example with zero setup:
```
OPENAI_API_KEY='your-api-key'\
uvrun--with'pydantic-ai[examples]'\
-mpydantic_ai_examples.pydantic_model

```

You'll probably want to edit examples in addition to just running them. You can copy the examples to a new directory with:
[pip](https://ai.pydantic.dev/examples/#__tabbed_5_1)[uv](https://ai.pydantic.dev/examples/#__tabbed_5_2)
```
python-mpydantic_ai_examples--copy-toexamples/

```

```
uvrun-mpydantic_ai_examples--copy-toexamples/

```

© Pydantic Services Inc. 2024 to present 
