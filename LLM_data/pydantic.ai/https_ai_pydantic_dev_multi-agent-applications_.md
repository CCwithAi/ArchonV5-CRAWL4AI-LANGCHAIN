[ Skip to content ](https://ai.pydantic.dev/multi-agent-applications/#multi-agent-applications)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Multi-agent Applications 
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
    * Multi-agent Applications  [ Multi-agent Applications  ](https://ai.pydantic.dev/multi-agent-applications/) Table of contents 
      * [ Agent delegation  ](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation)
        * [ Agent delegation and dependencies  ](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation-and-dependencies)
      * [ Programmatic agent hand-off  ](https://ai.pydantic.dev/multi-agent-applications/#programmatic-agent-hand-off)
      * [ Pydantic Graphs  ](https://ai.pydantic.dev/multi-agent-applications/#pydantic-graphs)
      * [ Examples  ](https://ai.pydantic.dev/multi-agent-applications/#examples)
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
  * [ Agent delegation  ](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation)
    * [ Agent delegation and dependencies  ](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation-and-dependencies)
  * [ Programmatic agent hand-off  ](https://ai.pydantic.dev/multi-agent-applications/#programmatic-agent-hand-off)
  * [ Pydantic Graphs  ](https://ai.pydantic.dev/multi-agent-applications/#pydantic-graphs)
  * [ Examples  ](https://ai.pydantic.dev/multi-agent-applications/#examples)


# Multi-agent Applications
There are roughly four levels of complexity when building applications with PydanticAI:
  1. Single agent workflows — what most of the `pydantic_ai` documentation covers
  2. [Agent delegation](https://ai.pydantic.dev/multi-agent-applications/#agent-delegation) — agents using another agent via tools
  3. [Programmatic agent hand-off](https://ai.pydantic.dev/multi-agent-applications/#programmatic-agent-hand-off) — one agent runs, then application code calls another agent
  4. [Graph based control flow](https://ai.pydantic.dev/graph/) — for the most complex cases, a graph-based state machine can be used to control the execution of multiple agents


Of course, you can combine multiple strategies in a single application.
## Agent delegation
"Agent delegation" refers to the scenario where an agent delegates work to another agent, then takes back control when the delegate agent (the agent called from within a tool) finishes.
Since agents are stateless and designed to be global, you do not need to include the agent itself in agent [dependencies](https://ai.pydantic.dev/dependencies/).
You'll generally want to pass [`ctx.usage`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.usage) to the [`usage`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run) keyword argument of the delegate agent run so usage within that run counts towards the total usage of the parent agent run.
Multiple models
Agent delegation doesn't need to use the same model for each agent. If you choose to use different models within a run, calculating the monetary cost from the final [`result.usage()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.usage) of the run will not be possible, but you can still use [`UsageLimits`](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.UsageLimits) to avoid unexpected costs.
agent_delegation_simple.py```
frompydantic_aiimport Agent, RunContext
frompydantic_ai.usageimport UsageLimits
joke_selection_agent = Agent( [](https://ai.pydantic.dev/multi-agent-applications/#__code_0_annotation_1)
  'openai:gpt-4o',
  system_prompt=(
    'Use the `joke_factory` to generate some jokes, then choose the best. '
    'You must return just a single joke.'
  ),
)
joke_generation_agent = Agent( [](https://ai.pydantic.dev/multi-agent-applications/#__code_0_annotation_2)
  'google-gla:gemini-1.5-flash', result_type=list[str]
)

@joke_selection_agent.tool
async defjoke_factory(ctx: RunContext[None], count: int) -> list[str]:
  r = await joke_generation_agent.run( [](https://ai.pydantic.dev/multi-agent-applications/#__code_0_annotation_3)
    f'Please generate {count} jokes.',
    usage=ctx.usage, [](https://ai.pydantic.dev/multi-agent-applications/#__code_0_annotation_4)
  )
  return r.data [](https://ai.pydantic.dev/multi-agent-applications/#__code_0_annotation_5)

result = joke_selection_agent.run_sync(
  'Tell me a joke.',
  usage_limits=UsageLimits(request_limit=5, total_tokens_limit=300),
)
print(result.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
print(result.usage())
"""
Usage(
  requests=3, request_tokens=204, response_tokens=24, total_tokens=228, details=None
)
"""

```

_(This example is complete, it can be run "as is")_
The control flow for this example is pretty simple and can be summarised as follows:
### Agent delegation and dependencies
Generally the delegate agent needs to either have the same [dependencies](https://ai.pydantic.dev/dependencies/) as the calling agent, or dependencies which are a subset of the calling agent's dependencies.
Initializing dependencies
We say "generally" above since there's nothing to stop you initializing dependencies within a tool call and therefore using interdependencies in a delegate agent that are not available on the parent, this should often be avoided since it can be significantly slower than reusing connections etc. from the parent agent.
agent_delegation_deps.py```
fromdataclassesimport dataclass
importhttpx
frompydantic_aiimport Agent, RunContext

@dataclass
classClientAndKey: [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_1)
  http_client: httpx.AsyncClient
  api_key: str

joke_selection_agent = Agent(
  'openai:gpt-4o',
  deps_type=ClientAndKey, [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_2)
  system_prompt=(
    'Use the `joke_factory` tool to generate some jokes on the given subject, '
    'then choose the best. You must return just a single joke.'
  ),
)
joke_generation_agent = Agent(
  'gemini-1.5-flash',
  deps_type=ClientAndKey, [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_4)
  result_type=list[str],
  system_prompt=(
    'Use the "get_jokes" tool to get some jokes on the given subject, '
    'then extract each joke into a list.'
  ),
)

@joke_selection_agent.tool
async defjoke_factory(ctx: RunContext[ClientAndKey], count: int) -> list[str]:
  r = await joke_generation_agent.run(
    f'Please generate {count} jokes.',
    deps=ctx.deps, [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_3)
    usage=ctx.usage,
  )
  return r.data

@joke_generation_agent.tool [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_5)
async defget_jokes(ctx: RunContext[ClientAndKey], count: int) -> str:
  response = await ctx.deps.http_client.get(
    'https://example.com',
    params={'count': count},
    headers={'Authorization': f'Bearer {ctx.deps.api_key}'},
  )
  response.raise_for_status()
  return response.text

async defmain():
  async with httpx.AsyncClient() as client:
    deps = ClientAndKey(client, 'foobar')
    result = await joke_selection_agent.run('Tell me a joke.', deps=deps)
    print(result.data)
    #> Did you hear about the toothpaste scandal? They called it Colgate.
    print(result.usage()) [](https://ai.pydantic.dev/multi-agent-applications/#__code_1_annotation_6)
"""
    Usage(
      requests=4,
      request_tokens=309,
      response_tokens=32,
      total_tokens=341,
      details=None,
    )
    """

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
This example shows how even a fairly simple agent delegation can lead to a complex control flow:
## Programmatic agent hand-off
"Programmatic agent hand-off" refers to the scenario where multiple agents are called in succession, with application code and/or a human in the loop responsible for deciding which agent to call next.
Here agents don't need to use the same deps.
Here we show two agents used in succession, the first to find a flight and the second to extract the user's seat preference.
programmatic_handoff.py```
fromtypingimport Literal, Union
frompydanticimport BaseModel, Field
fromrich.promptimport Prompt
frompydantic_aiimport Agent, RunContext
frompydantic_ai.messagesimport ModelMessage
frompydantic_ai.usageimport Usage, UsageLimits

classFlightDetails(BaseModel):
  flight_number: str

classFailed(BaseModel):
"""Unable to find a satisfactory choice."""

flight_search_agent = Agent[None, Union[FlightDetails, Failed]]( [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_1)
  'openai:gpt-4o',
  result_type=Union[FlightDetails, Failed], # type: ignore
  system_prompt=(
    'Use the "flight_search" tool to find a flight '
    'from the given origin to the given destination.'
  ),
)

@flight_search_agent.tool [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_2)
async defflight_search(
  ctx: RunContext[None], origin: str, destination: str
) -> Union[FlightDetails, None]:
  # in reality, this would call a flight search API or
  # use a browser to scrape a flight search website
  return FlightDetails(flight_number='AK456')

usage_limits = UsageLimits(request_limit=15) [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_3)

async deffind_flight(usage: Usage) -> Union[FlightDetails, None]: [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_4)
  message_history: Union[list[ModelMessage], None] = None
  for _ in range(3):
    prompt = Prompt.ask(
      'Where would you like to fly from and to?',
    )
    result = await flight_search_agent.run(
      prompt,
      message_history=message_history,
      usage=usage,
      usage_limits=usage_limits,
    )
    if isinstance(result.data, FlightDetails):
      return result.data
    else:
      message_history = result.all_messages(
        result_tool_return_content='Please try again.'
      )

classSeatPreference(BaseModel):
  row: int = Field(ge=1, le=30)
  seat: Literal['A', 'B', 'C', 'D', 'E', 'F']

# This agent is responsible for extracting the user's seat selection
seat_preference_agent = Agent[None, Union[SeatPreference, Failed]]( [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_5)
  'openai:gpt-4o',
  result_type=Union[SeatPreference, Failed], # type: ignore
  system_prompt=(
    "Extract the user's seat preference. "
    'Seats A and F are window seats. '
    'Row 1 is the front row and has extra leg room. '
    'Rows 14, and 20 also have extra leg room. '
  ),
)

async deffind_seat(usage: Usage) -> SeatPreference: [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_6)
  message_history: Union[list[ModelMessage], None] = None
  while True:
    answer = Prompt.ask('What seat would you like?')
    result = await seat_preference_agent.run(
      answer,
      message_history=message_history,
      usage=usage,
      usage_limits=usage_limits,
    )
    if isinstance(result.data, SeatPreference):
      return result.data
    else:
      print('Could not understand seat preference. Please try again.')
      message_history = result.all_messages()

async defmain(): [](https://ai.pydantic.dev/multi-agent-applications/#__code_2_annotation_7)
  usage: Usage = Usage()
  opt_flight_details = await find_flight(usage)
  if opt_flight_details is not None:
    print(f'Flight found: {opt_flight_details.flight_number}')
    #> Flight found: AK456
    seat_preference = await find_seat(usage)
    print(f'Seat preference: {seat_preference}')
    #> Seat preference: row=1 seat='A'

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
The control flow for this example can be summarised as follows:
## Pydantic Graphs
See the [graph](https://ai.pydantic.dev/graph/) documentation on when and how to use graphs.
## Examples
The following examples demonstrate how to use dependencies in PydanticAI:
  * [Flight booking](https://ai.pydantic.dev/examples/flight-booking/)


© Pydantic Services Inc. 2024 to present 
