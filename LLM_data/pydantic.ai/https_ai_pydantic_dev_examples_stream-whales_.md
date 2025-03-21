[ Skip to content ](https://ai.pydantic.dev/examples/stream-whales/#running-the-example)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Stream whales 
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
    * Stream whales  [ Stream whales  ](https://ai.pydantic.dev/examples/stream-whales/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/stream-whales/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/stream-whales/#example-code)
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
  * [ Running the Example  ](https://ai.pydantic.dev/examples/stream-whales/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/stream-whales/#example-code)


# Stream whales
Information about whales — an example of streamed structured response validation.
Demonstrates:
  * [streaming structured responses](https://ai.pydantic.dev/results/#streaming-structured-responses)


This script streams structured responses from GPT-4 about whales, validates the data and displays it as a dynamic table using [`rich`](https://github.com/Textualize/rich) as the data is received.
## Running the Example
With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/stream-whales/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/stream-whales/#__tabbed_1_2)
```
python-mpydantic_ai_examples.stream_whales

```

```
uvrun-mpydantic_ai_examples.stream_whales

```

Should give an output like this:
## Example Code
stream_whales.py```
fromtypingimport Annotated
importlogfire
frompydanticimport Field, ValidationError
fromrich.consoleimport Console
fromrich.liveimport Live
fromrich.tableimport Table
fromtyping_extensionsimport NotRequired, TypedDict
frompydantic_aiimport Agent
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

classWhale(TypedDict):
  name: str
  length: Annotated[
    float, Field(description='Average length of an adult whale in meters.')
  ]
  weight: NotRequired[
    Annotated[
      float,
      Field(description='Average weight of an adult whale in kilograms.', ge=50),
    ]
  ]
  ocean: NotRequired[str]
  description: NotRequired[Annotated[str, Field(description='Short Description')]]

agent = Agent('openai:gpt-4', result_type=list[Whale], instrument=True)

async defmain():
  console = Console()
  with Live('\n' * 36, console=console) as live:
    console.print('Requesting data...', style='cyan')
    async with agent.run_stream(
      'Generate me details of 5 species of Whale.'
    ) as result:
      console.print('Response:', style='green')
      async for message, last in result.stream_structured(debounce_by=0.01):
        try:
          whales = await result.validate_structured_result(
            message, allow_partial=not last
          )
        except ValidationError as exc:
          if all(
            e['type'] == 'missing' and e['loc'] == ('response',)
            for e in exc.errors()
          ):
            continue
          else:
            raise
        table = Table(
          title='Species of Whale',
          caption='Streaming Structured responses from GPT-4',
          width=120,
        )
        table.add_column('ID', justify='right')
        table.add_column('Name')
        table.add_column('Avg. Length (m)', justify='right')
        table.add_column('Avg. Weight (kg)', justify='right')
        table.add_column('Ocean')
        table.add_column('Description', justify='right')
        for wid, whale in enumerate(whales, start=1):
          table.add_row(
            str(wid),
            whale['name'],
            f'{whale["length"]:0.0f}',
            f'{w:0.0f}' if (w := whale.get('weight')) else '…',
            whale.get('ocean') or '…',
            whale.get('description') or '…',
          )
        live.update(table)

if __name__ == '__main__':
  importasyncio
  asyncio.run(main())

```

© Pydantic Services Inc. 2024 to present 
