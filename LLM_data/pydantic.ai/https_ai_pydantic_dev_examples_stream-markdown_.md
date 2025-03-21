[ Skip to content ](https://ai.pydantic.dev/examples/stream-markdown/#running-the-example)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Stream markdown 
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
    * Stream markdown  [ Stream markdown  ](https://ai.pydantic.dev/examples/stream-markdown/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/stream-markdown/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/stream-markdown/#example-code)
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
  * [ Running the Example  ](https://ai.pydantic.dev/examples/stream-markdown/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/stream-markdown/#example-code)


# Stream markdown
This example shows how to stream markdown from an agent, using the [`rich`](https://github.com/Textualize/rich) library to highlight the output in the terminal.
It'll run the example with both OpenAI and Google Gemini models if the required environment variables are set.
Demonstrates:
  * [streaming text responses](https://ai.pydantic.dev/results/#streaming-text)


## Running the Example
With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/stream-markdown/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/stream-markdown/#__tabbed_1_2)
```
python-mpydantic_ai_examples.stream_markdown

```

```
uvrun-mpydantic_ai_examples.stream_markdown

```

## Example Code
```
importasyncio
importos
importlogfire
fromrich.consoleimport Console, ConsoleOptions, RenderResult
fromrich.liveimport Live
fromrich.markdownimport CodeBlock, Markdown
fromrich.syntaximport Syntax
fromrich.textimport Text
frompydantic_aiimport Agent
frompydantic_ai.modelsimport KnownModelName
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
agent = Agent(instrument=True)
# models to try, and the appropriate env var
models: list[tuple[KnownModelName, str]] = [
  ('google-gla:gemini-1.5-flash', 'GEMINI_API_KEY'),
  ('openai:gpt-4o-mini', 'OPENAI_API_KEY'),
  ('groq:llama-3.3-70b-versatile', 'GROQ_API_KEY'),
]

async defmain():
  prettier_code_blocks()
  console = Console()
  prompt = 'Show me a short example of using Pydantic.'
  console.log(f'Asking: {prompt}...', style='cyan')
  for model, env_var in models:
    if env_var in os.environ:
      console.log(f'Using model: {model}')
      with Live('', console=console, vertical_overflow='visible') as live:
        async with agent.run_stream(prompt, model=model) as result:
          async for message in result.stream():
            live.update(Markdown(message))
      console.log(result.usage())
    else:
      console.log(f'{model} requires {env_var} to be set.')

defprettier_code_blocks():
"""Make rich code blocks prettier and easier to copy.
  From https://github.com/samuelcolvin/aicli/blob/v0.8.0/samuelcolvin_aicli.py#L22
  """
  classSimpleCodeBlock(CodeBlock):
    def__rich_console__(
      self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
      code = str(self.text).rstrip()
      yield Text(self.lexer_name, style='dim')
      yield Syntax(
        code,
        self.lexer_name,
        theme=self.theme,
        background_color='default',
        word_wrap=True,
      )
      yield Text(f'/{self.lexer_name}', style='dim')
  Markdown.elements['fence'] = SimpleCodeBlock

if __name__ == '__main__':
  asyncio.run(main())

```

© Pydantic Services Inc. 2024 to present 
