[ Skip to content ](https://ai.pydantic.dev/agents/#introduction)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Agents 
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
    * Agents  [ Agents  ](https://ai.pydantic.dev/agents/) Table of contents 
      * [ Introduction  ](https://ai.pydantic.dev/agents/#introduction)
      * [ Running Agents  ](https://ai.pydantic.dev/agents/#running-agents)
        * [ Iterating Over an Agent's Graph  ](https://ai.pydantic.dev/agents/#iterating-over-an-agents-graph)
          * [ async for iteration  ](https://ai.pydantic.dev/agents/#async-for-iteration)
          * [ Using .next(...) manually  ](https://ai.pydantic.dev/agents/#using-next-manually)
          * [ Accessing usage and the final result  ](https://ai.pydantic.dev/agents/#accessing-usage-and-the-final-result)
        * [ Streaming  ](https://ai.pydantic.dev/agents/#streaming)
        * [ Additional Configuration  ](https://ai.pydantic.dev/agents/#additional-configuration)
          * [ Usage Limits  ](https://ai.pydantic.dev/agents/#usage-limits)
          * [ Model (Run) Settings  ](https://ai.pydantic.dev/agents/#model-run-settings)
        * [ Model specific settings  ](https://ai.pydantic.dev/agents/#model-specific-settings)
      * [ Runs vs. Conversations  ](https://ai.pydantic.dev/agents/#runs-vs-conversations)
      * [ Type safe by design  ](https://ai.pydantic.dev/agents/#static-type-checking)
      * [ System Prompts  ](https://ai.pydantic.dev/agents/#system-prompts)
      * [ Reflection and self-correction  ](https://ai.pydantic.dev/agents/#reflection-and-self-correction)
      * [ Model errors  ](https://ai.pydantic.dev/agents/#model-errors)
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
  * [ Introduction  ](https://ai.pydantic.dev/agents/#introduction)
  * [ Running Agents  ](https://ai.pydantic.dev/agents/#running-agents)
    * [ Iterating Over an Agent's Graph  ](https://ai.pydantic.dev/agents/#iterating-over-an-agents-graph)
      * [ async for iteration  ](https://ai.pydantic.dev/agents/#async-for-iteration)
      * [ Using .next(...) manually  ](https://ai.pydantic.dev/agents/#using-next-manually)
      * [ Accessing usage and the final result  ](https://ai.pydantic.dev/agents/#accessing-usage-and-the-final-result)
    * [ Streaming  ](https://ai.pydantic.dev/agents/#streaming)
    * [ Additional Configuration  ](https://ai.pydantic.dev/agents/#additional-configuration)
      * [ Usage Limits  ](https://ai.pydantic.dev/agents/#usage-limits)
      * [ Model (Run) Settings  ](https://ai.pydantic.dev/agents/#model-run-settings)
    * [ Model specific settings  ](https://ai.pydantic.dev/agents/#model-specific-settings)
  * [ Runs vs. Conversations  ](https://ai.pydantic.dev/agents/#runs-vs-conversations)
  * [ Type safe by design  ](https://ai.pydantic.dev/agents/#static-type-checking)
  * [ System Prompts  ](https://ai.pydantic.dev/agents/#system-prompts)
  * [ Reflection and self-correction  ](https://ai.pydantic.dev/agents/#reflection-and-self-correction)
  * [ Model errors  ](https://ai.pydantic.dev/agents/#model-errors)


# Agents
## Introduction
Agents are PydanticAI's primary interface for interacting with LLMs.
In some use cases a single Agent will control an entire application or component, but multiple agents can also interact to embody more complex workflows.
The [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent) class has full API documentation, but conceptually you can think of an agent as a container for:
**Component** | **Description**  
---|---  
[System prompt(s)](https://ai.pydantic.dev/agents/#system-prompts) | A set of instructions for the LLM written by the developer.  
[Function tool(s)](https://ai.pydantic.dev/tools/) | Functions that the LLM may call to get information while generating a response.  
[Structured result type](https://ai.pydantic.dev/results/) | The structured datatype the LLM must return at the end of a run, if specified.  
[Dependency type constraint](https://ai.pydantic.dev/dependencies/) | System prompt functions, tools, and result validators may all use dependencies when they're run.  
[LLM model](https://ai.pydantic.dev/api/models/base/) | Optional default LLM model associated with the agent. Can also be specified when running the agent.  
[Model Settings](https://ai.pydantic.dev/agents/#additional-configuration) | Optional default model settings to help fine tune requests. Can also be specified when running the agent.  
In typing terms, agents are generic in their dependency and result types, e.g., an agent which required dependencies of type `Foobar` and returned results of type `list[str]` would have type `Agent[Foobar, list[str]]`. In practice, you shouldn't need to care about this, it should just mean your IDE can tell you when you have the right type, and if you choose to use [static type checking](https://ai.pydantic.dev/agents/#static-type-checking) it should work well with PydanticAI.
Here's a toy example of an agent that simulates a roulette wheel:
roulette_wheel.py```
frompydantic_aiimport Agent, RunContext
roulette_agent = Agent( [](https://ai.pydantic.dev/agents/#__code_0_annotation_1)
  'openai:gpt-4o',
  deps_type=int,
  result_type=bool,
  system_prompt=(
    'Use the `roulette_wheel` function to see if the '
    'customer has won based on the number they provide.'
  ),
)

@roulette_agent.tool
async defroulette_wheel(ctx: RunContext[int], square: int) -> str: [](https://ai.pydantic.dev/agents/#__code_0_annotation_2)
"""check if the square is a winner"""
  return 'winner' if square == ctx.deps else 'loser'

# Run the agent
success_number = 18 [](https://ai.pydantic.dev/agents/#__code_0_annotation_3)
result = roulette_agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.data) [](https://ai.pydantic.dev/agents/#__code_0_annotation_4)
#> True
result = roulette_agent.run_sync('I bet five is the winner', deps=success_number)
print(result.data)
#> False

```

Agents are designed for reuse, like FastAPI Apps
Agents are intended to be instantiated once (frequently as module globals) and reused throughout your application, similar to a small [FastAPI](https://fastapi.tiangolo.com/reference/fastapi/#fastapi.FastAPI) app or an [APIRouter](https://fastapi.tiangolo.com/reference/apirouter/#fastapi.APIRouter).
## Running Agents
There are four ways to run an agent:
  1. [`agent.run()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run) — a coroutine which returns a [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult) containing a completed response.
  2. [`agent.run_sync()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_sync) — a plain, synchronous function which returns a [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult) containing a completed response (internally, this just calls `loop.run_until_complete(self.run())`).
  3. [`agent.run_stream()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_stream) — a coroutine which returns a [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult), which contains methods to stream a response as an async iterable.
  4. [`agent.iter()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter) — a context manager which returns an [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun), an async-iterable over the nodes of the agent's underlying [`Graph`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph).


Here's a simple example demonstrating the first three:
run_agent.py```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o')
result_sync = agent.run_sync('What is the capital of Italy?')
print(result_sync.data)
#> Rome

async defmain():
  result = await agent.run('What is the capital of France?')
  print(result.data)
  #> Paris
  async with agent.run_stream('What is the capital of the UK?') as response:
    print(await response.get_data())
    #> London

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
You can also pass messages from previous runs to continue a conversation or provide context, as described in [Messages and Chat History](https://ai.pydantic.dev/message-history/).
### Iterating Over an Agent's Graph
Under the hood, each `Agent` in PydanticAI uses **pydantic-graph** to manage its execution flow. **pydantic-graph** is a generic, type-centric library for building and running finite state machines in Python. It doesn't actually depend on PydanticAI — you can use it standalone for workflows that have nothing to do with GenAI — but PydanticAI makes use of it to orchestrate the handling of model requests and model responses in an agent's run.
In many scenarios, you don't need to worry about pydantic-graph at all; calling `agent.run(...)` simply traverses the underlying graph from start to finish. However, if you need deeper insight or control — for example to capture each tool invocation, or to inject your own logic at specific stages — PydanticAI exposes the lower-level iteration process via [`Agent.iter`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.iter). This method returns an [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun), which you can async-iterate over, or manually drive node-by-node via the [`next`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun.next) method. Once the agent's graph returns an [`End`](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End), you have the final result along with a detailed history of all steps.
#### `async for` iteration
Here's an example of using `async for` with `iter` to record each node the agent executes:
agent_iter_async_for.py```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o')

async defmain():
  nodes = []
  # Begin an AgentRun, which is an async-iterable over the nodes of the agent's graph
  async with agent.iter('What is the capital of France?') as agent_run:
    async for node in agent_run:
      # Each node represents a step in the agent's execution
      nodes.append(node)
  print(nodes)
"""
  [
    ModelRequestNode(
      request=ModelRequest(
        parts=[
          UserPromptPart(
            content='What is the capital of France?',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          )
        ],
        kind='request',
      )
    ),
    CallToolsNode(
      model_response=ModelResponse(
        parts=[TextPart(content='Paris', part_kind='text')],
        model_name='gpt-4o',
        timestamp=datetime.datetime(...),
        kind='response',
      )
    ),
    End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),
  ]
  """
  print(agent_run.result.data)
  #> Paris

```

  * The `AgentRun` is an async iterator that yields each node (`BaseNode` or `End`) in the flow.
  * The run ends when an `End` node is returned.


#### Using `.next(...)` manually
You can also drive the iteration manually by passing the node you want to run next to the `AgentRun.next(...)` method. This allows you to inspect or modify the node before it executes or skip nodes based on your own logic, and to catch errors in `next()` more easily:
agent_iter_next.py```
frompydantic_aiimport Agent
frompydantic_graphimport End
agent = Agent('openai:gpt-4o')

async defmain():
  async with agent.iter('What is the capital of France?') as agent_run:
    node = agent_run.next_node [](https://ai.pydantic.dev/agents/#__code_3_annotation_1)
    all_nodes = [node]
    # Drive the iteration manually:
    while not isinstance(node, End): [](https://ai.pydantic.dev/agents/#__code_3_annotation_2)
      node = await agent_run.next(node) [](https://ai.pydantic.dev/agents/#__code_3_annotation_3)
      all_nodes.append(node) [](https://ai.pydantic.dev/agents/#__code_3_annotation_4)
    print(all_nodes)
"""
    [
      UserPromptNode(
        user_prompt='What is the capital of France?',
        system_prompts=(),
        system_prompt_functions=[],
        system_prompt_dynamic_functions={},
      ),
      ModelRequestNode(
        request=ModelRequest(
          parts=[
            UserPromptPart(
              content='What is the capital of France?',
              timestamp=datetime.datetime(...),
              part_kind='user-prompt',
            )
          ],
          kind='request',
        )
      ),
      CallToolsNode(
        model_response=ModelResponse(
          parts=[TextPart(content='Paris', part_kind='text')],
          model_name='gpt-4o',
          timestamp=datetime.datetime(...),
          kind='response',
        )
      ),
      End(data=FinalResult(data='Paris', tool_name=None, tool_call_id=None)),
    ]
    """

```

#### Accessing usage and the final result
You can retrieve usage statistics (tokens, requests, etc.) at any time from the [`AgentRun`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRun) object via `agent_run.usage()`. This method returns a [`Usage`](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.Usage) object containing the usage data.
Once the run finishes, `agent_run.final_result` becomes a [`AgentRunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult) object containing the final output (and related metadata).
### Streaming
Here is an example of streaming an agent run in combination with `async for` iteration:
streaming.py```
importasyncio
fromdataclassesimport dataclass
fromdatetimeimport date
frompydantic_aiimport Agent
frompydantic_ai.messagesimport (
  FinalResultEvent,
  FunctionToolCallEvent,
  FunctionToolResultEvent,
  PartDeltaEvent,
  PartStartEvent,
  TextPartDelta,
  ToolCallPartDelta,
)
frompydantic_ai.toolsimport RunContext

@dataclass
classWeatherService:
  async defget_forecast(self, location: str, forecast_date: date) -> str:
    # In real code: call weather API, DB queries, etc.
    return f'The forecast in {location} on {forecast_date} is 24°C and sunny.'
  async defget_historic_weather(self, location: str, forecast_date: date) -> str:
    # In real code: call a historical weather API or DB
    return (
      f'The weather in {location} on {forecast_date} was 18°C and partly cloudy.'
    )

weather_agent = Agent[WeatherService, str](
  'openai:gpt-4o',
  deps_type=WeatherService,
  result_type=str, # We'll produce a final answer as plain text
  system_prompt='Providing a weather forecast at the locations the user provides.',
)

@weather_agent.tool
async defweather_forecast(
  ctx: RunContext[WeatherService],
  location: str,
  forecast_date: date,
) -> str:
  if forecast_date >= date.today():
    return await ctx.deps.get_forecast(location, forecast_date)
  else:
    return await ctx.deps.get_historic_weather(location, forecast_date)

output_messages: list[str] = []

async defmain():
  user_prompt = 'What will the weather be like in Paris on Tuesday?'
  # Begin a node-by-node, streaming iteration
  async with weather_agent.iter(user_prompt, deps=WeatherService()) as run:
    async for node in run:
      if Agent.is_user_prompt_node(node):
        # A user prompt node => The user has provided input
        output_messages.append(f'=== UserPromptNode: {node.user_prompt} ===')
      elif Agent.is_model_request_node(node):
        # A model request node => We can stream tokens from the model's request
        output_messages.append(
          '=== ModelRequestNode: streaming partial request tokens ==='
        )
        async with node.stream(run.ctx) as request_stream:
          async for event in request_stream:
            if isinstance(event, PartStartEvent):
              output_messages.append(
                f'[Request] Starting part {event.index}: {event.part!r}'
              )
            elif isinstance(event, PartDeltaEvent):
              if isinstance(event.delta, TextPartDelta):
                output_messages.append(
                  f'[Request] Part {event.index} text delta: {event.delta.content_delta!r}'
                )
              elif isinstance(event.delta, ToolCallPartDelta):
                output_messages.append(
                  f'[Request] Part {event.index} args_delta={event.delta.args_delta}'
                )
            elif isinstance(event, FinalResultEvent):
              output_messages.append(
                f'[Result] The model produced a final result (tool_name={event.tool_name})'
              )
      elif Agent.is_call_tools_node(node):
        # A handle-response node => The model returned some data, potentially calls a tool
        output_messages.append(
          '=== CallToolsNode: streaming partial response & tool usage ==='
        )
        async with node.stream(run.ctx) as handle_stream:
          async for event in handle_stream:
            if isinstance(event, FunctionToolCallEvent):
              output_messages.append(
                f'[Tools] The LLM calls tool={event.part.tool_name!r} with args={event.part.args} (tool_call_id={event.part.tool_call_id!r})'
              )
            elif isinstance(event, FunctionToolResultEvent):
              output_messages.append(
                f'[Tools] Tool call {event.tool_call_id!r} returned => {event.result.content}'
              )
      elif Agent.is_end_node(node):
        assert run.result.data == node.data.data
        # Once an End node is reached, the agent run is complete
        output_messages.append(f'=== Final Agent Output: {run.result.data} ===')

if __name__ == '__main__':
  asyncio.run(main())
  print(output_messages)
"""
  [
    '=== ModelRequestNode: streaming partial request tokens ===',
    '[Request] Starting part 0: ToolCallPart(tool_name=\'weather_forecast\', args=\'{"location":"Pa\', tool_call_id=\'0001\', part_kind=\'tool-call\')',
    '[Request] Part 0 args_delta=ris","forecast_',
    '[Request] Part 0 args_delta=date":"2030-01-',
    '[Request] Part 0 args_delta=01"}',
    '=== CallToolsNode: streaming partial response & tool usage ===',
    '[Tools] The LLM calls tool=\'weather_forecast\' with args={"location":"Paris","forecast_date":"2030-01-01"} (tool_call_id=\'0001\')',
    "[Tools] Tool call '0001' returned => The forecast in Paris on 2030-01-01 is 24°C and sunny.",
    '=== ModelRequestNode: streaming partial request tokens ===',
    "[Request] Starting part 0: TextPart(content='It will be ', part_kind='text')",
    '[Result] The model produced a final result (tool_name=None)',
    "[Request] Part 0 text delta: 'warm and sunny '",
    "[Request] Part 0 text delta: 'in Paris on '",
    "[Request] Part 0 text delta: 'Tuesday.'",
    '=== CallToolsNode: streaming partial response & tool usage ===',
    '=== Final Agent Output: It will be warm and sunny in Paris on Tuesday. ===',
  ]
  """

```

### Additional Configuration
#### Usage Limits
PydanticAI offers a [`UsageLimits`](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits) structure to help you limit your usage (tokens and/or requests) on model runs.
You can apply these settings by passing the `usage_limits` argument to the `run{_sync,_stream}` functions.
Consider the following example, where we limit the number of response tokens:
```
frompydantic_aiimport Agent
frompydantic_ai.exceptionsimport UsageLimitExceeded
frompydantic_ai.usageimport UsageLimits
agent = Agent('anthropic:claude-3-5-sonnet-latest')
result_sync = agent.run_sync(
  'What is the capital of Italy? Answer with just the city.',
  usage_limits=UsageLimits(response_tokens_limit=10),
)
print(result_sync.data)
#> Rome
print(result_sync.usage())
"""
Usage(requests=1, request_tokens=62, response_tokens=1, total_tokens=63, details=None)
"""
try:
  result_sync = agent.run_sync(
    'What is the capital of Italy? Answer with a paragraph.',
    usage_limits=UsageLimits(response_tokens_limit=10),
  )
except UsageLimitExceeded as e:
  print(e)
  #> Exceeded the response_tokens_limit of 10 (response_tokens=32)

```

Restricting the number of requests can be useful in preventing infinite loops or excessive tool calling:
```
fromtyping_extensionsimport TypedDict
frompydantic_aiimport Agent, ModelRetry
frompydantic_ai.exceptionsimport UsageLimitExceeded
frompydantic_ai.usageimport UsageLimits

classNeverResultType(TypedDict):
"""
  Never ever coerce data to this type.
  """
  never_use_this: str

agent = Agent(
  'anthropic:claude-3-5-sonnet-latest',
  retries=3,
  result_type=NeverResultType,
  system_prompt='Any time you get a response, call the `infinite_retry_tool` to produce another response.',
)

@agent.tool_plain(retries=5) [](https://ai.pydantic.dev/agents/#__code_6_annotation_1)
definfinite_retry_tool() -> int:
  raise ModelRetry('Please try again.')

try:
  result_sync = agent.run_sync(
    'Begin infinite retry loop!', usage_limits=UsageLimits(request_limit=3) [](https://ai.pydantic.dev/agents/#__code_6_annotation_2)
  )
except UsageLimitExceeded as e:
  print(e)
  #> The next request would exceed the request_limit of 3

```

Note
This is especially relevant if you've registered many tools. The `request_limit` can be used to prevent the model from calling them in a loop too many times.
#### Model (Run) Settings
PydanticAI offers a [`settings.ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings) structure to help you fine tune your requests. This structure allows you to configure common parameters that influence the model's behavior, such as `temperature`, `max_tokens`, `timeout`, and more.
There are two ways to apply these settings: 1. Passing to `run{_sync,_stream}` functions via the `model_settings` argument. This allows for fine-tuning on a per-request basis. 2. Setting during [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent) initialization via the `model_settings` argument. These settings will be applied by default to all subsequent run calls using said agent. However, `model_settings` provided during a specific run call will override the agent's default settings.
For example, if you'd like to set the `temperature` setting to `0.0` to ensure less random behavior, you can do the following:
```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o')
result_sync = agent.run_sync(
  'What is the capital of Italy?', model_settings={'temperature': 0.0}
)
print(result_sync.data)
#> Rome

```

### Model specific settings
If you wish to further customize model behavior, you can use a subclass of [`ModelSettings`](https://ai.pydantic.dev/api/settings/#pydantic_ai.settings.ModelSettings), like [`GeminiModelSettings`](https://ai.pydantic.dev/api/models/gemini/#pydantic_ai.models.gemini.GeminiModelSettings), associated with your model of choice.
For example:
```
frompydantic_aiimport Agent, UnexpectedModelBehavior
frompydantic_ai.models.geminiimport GeminiModelSettings
agent = Agent('google-gla:gemini-1.5-flash')
try:
  result = agent.run_sync(
    'Write a list of 5 very rude things that I might say to the universe after stubbing my toe in the dark:',
    model_settings=GeminiModelSettings(
      temperature=0.0, # general model settings can also be specified
      gemini_safety_settings=[
        {
          'category': 'HARM_CATEGORY_HARASSMENT',
          'threshold': 'BLOCK_LOW_AND_ABOVE',
        },
        {
          'category': 'HARM_CATEGORY_HATE_SPEECH',
          'threshold': 'BLOCK_LOW_AND_ABOVE',
        },
      ],
    ),
  )
except UnexpectedModelBehavior as e:
  print(e) [](https://ai.pydantic.dev/agents/#__code_8_annotation_1)
"""
  Safety settings triggered, body:
  <safety settings details>
  """

```

## Runs vs. Conversations
An agent **run** might represent an entire conversation — there's no limit to how many messages can be exchanged in a single run. However, a **conversation** might also be composed of multiple runs, especially if you need to maintain state between separate interactions or API calls.
Here's an example of a conversation comprised of multiple runs:
conversation_example.py```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o')
# First run
result1 = agent.run_sync('Who was Albert Einstein?')
print(result1.data)
#> Albert Einstein was a German-born theoretical physicist.
# Second run, passing previous messages
result2 = agent.run_sync(
  'What was his most famous equation?',
  message_history=result1.new_messages(), [](https://ai.pydantic.dev/agents/#__code_9_annotation_1)
)
print(result2.data)
#> Albert Einstein's most famous equation is (E = mc^2).

```

_(This example is complete, it can be run "as is")_
## Type safe by design
PydanticAI is designed to work well with static type checkers, like mypy and pyright.
Typing is (somewhat) optional
PydanticAI is designed to make type checking as useful as possible for you if you choose to use it, but you don't have to use types everywhere all the time.
That said, because PydanticAI uses Pydantic, and Pydantic uses type hints as the definition for schema and validation, some types (specifically type hints on parameters to tools, and the `result_type` arguments to [`Agent`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent)) are used at runtime.
We (the library developers) have messed up if type hints are confusing you more than helping you, if you find this, please create an [issue](https://github.com/pydantic/pydantic-ai/issues) explaining what's annoying you!
In particular, agents are generic in both the type of their dependencies and the type of results they return, so you can use the type hints to ensure you're using the right types.
Consider the following script with type mistakes:
type_mistakes.py```
fromdataclassesimport dataclass
frompydantic_aiimport Agent, RunContext

@dataclass
classUser:
  name: str

agent = Agent(
  'test',
  deps_type=User, [](https://ai.pydantic.dev/agents/#__code_10_annotation_1)
  result_type=bool,
)

@agent.system_prompt
defadd_user_name(ctx: RunContext[str]) -> str: [](https://ai.pydantic.dev/agents/#__code_10_annotation_2)
  return f"The user's name is {ctx.deps}."

deffoobar(x: bytes) -> None:
  pass

result = agent.run_sync('Does their name start with "A"?', deps=User('Anne'))
foobar(result.data) [](https://ai.pydantic.dev/agents/#__code_10_annotation_3)

```

Running `mypy` on this will give the following output:
```
➤uvrunmypytype_mistakes.py
type_mistakes.py:18:error:Argument1to"system_prompt"of"Agent"hasincompatibletype"Callable[[RunContext[str]], str]";expected"Callable[[RunContext[User]], str]"[arg-type]
type_mistakes.py:28:error:Argument1to"foobar"hasincompatibletype"bool";expected"bytes"[arg-type]
Found2errorsin1file(checked1sourcefile)

```

Running `pyright` would identify the same issues.
## System Prompts
System prompts might seem simple at first glance since they're just strings (or sequences of strings that are concatenated), but crafting the right system prompt is key to getting the model to behave as you want.
Generally, system prompts fall into two categories:
  1. **Static system prompts** : These are known when writing the code and can be defined via the `system_prompt` parameter of the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__).
  2. **Dynamic system prompts** : These depend in some way on context that isn't known until runtime, and should be defined via functions decorated with [`@agent.system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt).


You can add both to a single agent; they're appended in the order they're defined at runtime.
Here's an example using both types of system prompts:
system_prompts.py```
fromdatetimeimport date
frompydantic_aiimport Agent, RunContext
agent = Agent(
  'openai:gpt-4o',
  deps_type=str, [](https://ai.pydantic.dev/agents/#__code_12_annotation_1)
  system_prompt="Use the customer's name while replying to them.", [](https://ai.pydantic.dev/agents/#__code_12_annotation_2)
)

@agent.system_prompt [](https://ai.pydantic.dev/agents/#__code_12_annotation_3)
defadd_the_users_name(ctx: RunContext[str]) -> str:
  return f"The user's name is {ctx.deps}."

@agent.system_prompt
defadd_the_date() -> str: [](https://ai.pydantic.dev/agents/#__code_12_annotation_4)
  return f'The date is {date.today()}.'

result = agent.run_sync('What is the date?', deps='Frank')
print(result.data)
#> Hello Frank, the date today is 2032-01-02.

```

_(This example is complete, it can be run "as is")_
## Reflection and self-correction
Validation errors from both function tool parameter validation and [structured result validation](https://ai.pydantic.dev/results/#structured-result-validation) can be passed back to the model with a request to retry.
You can also raise [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry) from within a [tool](https://ai.pydantic.dev/tools/) or [result validator function](https://ai.pydantic.dev/results/#result-validators-functions) to tell the model it should retry generating a response.
  * The default retry count is **1** but can be altered for the [entire agent](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__), a [specific tool](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool), or a [result validator](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__).
  * You can access the current retry count from within a tool or result validator via [`ctx.retry`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext).


Here's an example:
tool_retry.py```
frompydanticimport BaseModel
frompydantic_aiimport Agent, RunContext, ModelRetry
fromfake_databaseimport DatabaseConn

classChatResult(BaseModel):
  user_id: int
  message: str

agent = Agent(
  'openai:gpt-4o',
  deps_type=DatabaseConn,
  result_type=ChatResult,
)

@agent.tool(retries=2)
defget_user_by_name(ctx: RunContext[DatabaseConn], name: str) -> int:
"""Get a user's ID from their full name."""
  print(name)
  #> John
  #> John Doe
  user_id = ctx.deps.users.get(name=name)
  if user_id is None:
    raise ModelRetry(
      f'No user found with name {name!r}, remember to provide their full name'
    )
  return user_id

result = agent.run_sync(
  'Send a message to John Doe asking for coffee next week', deps=DatabaseConn()
)
print(result.data)
"""
user_id=123 message='Hello John, would you be free for coffee sometime next week? Let me know what works for you!'
"""

```

## Model errors
If models behave unexpectedly (e.g., the retry limit is exceeded, or their API returns `503`), agent runs will raise [`UnexpectedModelBehavior`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior).
In these cases, [`capture_run_messages`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.capture_run_messages) can be used to access the messages exchanged during the run to help diagnose the issue.
agent_model_errors.py```
frompydantic_aiimport Agent, ModelRetry, UnexpectedModelBehavior, capture_run_messages
agent = Agent('openai:gpt-4o')

@agent.tool_plain
defcalc_volume(size: int) -> int: [](https://ai.pydantic.dev/agents/#__code_14_annotation_1)
  if size == 42:
    return size**3
  else:
    raise ModelRetry('Please try again.')

with capture_run_messages() as messages: [](https://ai.pydantic.dev/agents/#__code_14_annotation_2)
  try:
    result = agent.run_sync('Please get me the volume of a box with size 6.')
  except UnexpectedModelBehavior as e:
    print('An error occurred:', e)
    #> An error occurred: Tool exceeded max retries count of 1
    print('cause:', repr(e.__cause__))
    #> cause: ModelRetry('Please try again.')
    print('messages:', messages)
"""
    messages:
    [
      ModelRequest(
        parts=[
          UserPromptPart(
            content='Please get me the volume of a box with size 6.',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          )
        ],
        kind='request',
      ),
      ModelResponse(
        parts=[
          ToolCallPart(
            tool_name='calc_volume',
            args={'size': 6},
            tool_call_id=None,
            part_kind='tool-call',
          )
        ],
        model_name='gpt-4o',
        timestamp=datetime.datetime(...),
        kind='response',
      ),
      ModelRequest(
        parts=[
          RetryPromptPart(
            content='Please try again.',
            tool_name='calc_volume',
            tool_call_id=None,
            timestamp=datetime.datetime(...),
            part_kind='retry-prompt',
          )
        ],
        kind='request',
      ),
      ModelResponse(
        parts=[
          ToolCallPart(
            tool_name='calc_volume',
            args={'size': 6},
            tool_call_id=None,
            part_kind='tool-call',
          )
        ],
        model_name='gpt-4o',
        timestamp=datetime.datetime(...),
        kind='response',
      ),
    ]
    """
  else:
    print(result.data)

```

_(This example is complete, it can be run "as is")_
Note
If you call [`run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run), [`run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_sync), or [`run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_stream) more than once within a single `capture_run_messages` context, `messages` will represent the messages exchanged during the first call only.
© Pydantic Services Inc. 2024 to present 
