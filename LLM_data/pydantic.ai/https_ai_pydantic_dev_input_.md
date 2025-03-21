[ Skip to content ](https://ai.pydantic.dev/input/#image-audio-document-input)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Image, Audio & Document Input 
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
    * Image, Audio & Document Input  [ Image, Audio & Document Input  ](https://ai.pydantic.dev/input/) Table of contents 
      * [ Image Input  ](https://ai.pydantic.dev/input/#image-input)
      * [ Audio Input  ](https://ai.pydantic.dev/input/#audio-input)
      * [ Document Input  ](https://ai.pydantic.dev/input/#document-input)
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
  * [ Image Input  ](https://ai.pydantic.dev/input/#image-input)
  * [ Audio Input  ](https://ai.pydantic.dev/input/#audio-input)
  * [ Document Input  ](https://ai.pydantic.dev/input/#document-input)


# Image, Audio & Document Input
Some LLMs are now capable of understanding both audio, image and document content.
## Image Input
Info
Some models do not support image input. Please check the model's documentation to confirm whether it supports image input.
If you have a direct URL for the image, you can use [`ImageUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl):
main.py```
frompydantic_aiimport Agent, ImageUrl
agent = Agent(model='openai:gpt-4o')
result = agent.run_sync(
  [
    'What company is this logo from?',
    ImageUrl(url='https://iili.io/3Hs4FMg.png'),
  ]
)
print(result.data)
#> This is the logo for Pydantic, a data validation and settings management library in Python.

```

If you have the image locally, you can also use [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent):
main.py```
importhttpx
frompydantic_aiimport Agent, BinaryContent
image_response = httpx.get('https://iili.io/3Hs4FMg.png') # Pydantic logo
agent = Agent(model='openai:gpt-4o')
result = agent.run_sync(
  [
    'What company is this logo from?',
    BinaryContent(data=image_response.content, media_type='image/png'), 
To ensure the example is runnable we download this image from the web, but you can also use Path().read_bytes() to read a local file's contents.
[](https://ai.pydantic.dev/input/#__code_1_annotation_1)
  ]
)
print(result.data)
#> This is the logo for Pydantic, a data validation and settings management library in Python.

```

## Audio Input
Info
Some models do not support audio input. Please check the model's documentation to confirm whether it supports audio input.
You can provide audio input using either [`AudioUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl) or [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent). The process is analogous to the examples above.
## Document Input
Info
Some models do not support document input. Please check the model's documentation to confirm whether it supports document input.
Warning
When using Gemini models, the document content will always be sent as binary data, regardless of whether you use `DocumentUrl` or `BinaryContent`. This is due to differences in how Vertex AI and Google AI handle document inputs.
For more details, see [this discussion](https://discuss.ai.google.dev/t/i-am-using-google-generative-ai-model-gemini-1-5-pro-for-image-analysis-but-getting-error/34866/4).
If you are unsatisfied with this behavior, please let us know by opening an issue on [GitHub](https://github.com/pydantic/pydantic-ai/issues).
You can provide document input using either [`DocumentUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl) or [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent). The process is similar to the examples above.
If you have a direct URL for the document, you can use [`DocumentUrl`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl):
main.py```
frompydantic_aiimport Agent, DocumentUrl
agent = Agent(model='anthropic:claude-3-sonnet')
result = agent.run_sync(
  [
    'What is the main content of this document?',
    DocumentUrl(url='https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf'),
  ]
)
print(result.data)
#> This document is the technical report introducing Gemini 1.5, Google's latest large language model...

```

The supported document formats vary by model.
You can also use [`BinaryContent`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent) to pass document data directly:
main.py```
frompathlibimport Path
frompydantic_aiimport Agent, BinaryContent
pdf_path = Path('document.pdf')
agent = Agent(model='anthropic:claude-3-sonnet')
result = agent.run_sync(
  [
    'What is the main content of this document?',
    BinaryContent(data=pdf_path.read_bytes(), media_type='application/pdf'),
  ]
)
print(result.data)
#> The document discusses...

```

© Pydantic Services Inc. 2024 to present 
