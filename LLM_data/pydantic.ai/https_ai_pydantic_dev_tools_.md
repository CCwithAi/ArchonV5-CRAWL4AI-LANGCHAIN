[ Skip to content ](https://ai.pydantic.dev/tools/#function-tools)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Function Tools 
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
    * Function Tools  [ Function Tools  ](https://ai.pydantic.dev/tools/) Table of contents 
      * [ Registering Function Tools via kwarg  ](https://ai.pydantic.dev/tools/#registering-function-tools-via-kwarg)
      * [ Function Tools vs. Structured Results  ](https://ai.pydantic.dev/tools/#function-tools-vs-structured-results)
      * [ Function tools and schema  ](https://ai.pydantic.dev/tools/#function-tools-and-schema)
      * [ Dynamic Function tools  ](https://ai.pydantic.dev/tools/#tool-prepare)
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
  * [ Registering Function Tools via kwarg  ](https://ai.pydantic.dev/tools/#registering-function-tools-via-kwarg)
  * [ Function Tools vs. Structured Results  ](https://ai.pydantic.dev/tools/#function-tools-vs-structured-results)
  * [ Function tools and schema  ](https://ai.pydantic.dev/tools/#function-tools-and-schema)
  * [ Dynamic Function tools  ](https://ai.pydantic.dev/tools/#tool-prepare)


# Function Tools
Function tools provide a mechanism for models to retrieve extra information to help them generate a response.
They're useful when it is impractical or impossible to put all the context an agent might need into the system prompt, or when you want to make agents' behavior more deterministic or reliable by deferring some of the logic required to generate a response to another (not necessarily AI-powered) tool.
Function tools vs. RAG
Function tools are basically the "R" of RAG (Retrieval-Augmented Generation) — they augment what the model can do by letting it request extra information.
The main semantic difference between PydanticAI Tools and RAG is RAG is synonymous with vector search, while PydanticAI tools are more general-purpose. (Note: we may add support for vector search functionality in the future, particularly an API for generating embeddings. See [#58](https://github.com/pydantic/pydantic-ai/issues/58))
There are a number of ways to register tools with an agent:
  * via the [`@agent.tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool) decorator — for tools that need access to the agent [context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext)
  * via the [`@agent.tool_plain`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool_plain) decorator — for tools that do not need access to the agent [context](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext)
  * via the [`tools`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__) keyword argument to `Agent` which can take either plain functions, or instances of [`Tool`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool)


`@agent.tool` is considered the default decorator since in the majority of cases tools will need access to the agent context.
Here's an example using both:
dice_game.py```
importrandom
frompydantic_aiimport Agent, RunContext
agent = Agent(
  'google-gla:gemini-1.5-flash', [](https://ai.pydantic.dev/tools/#__code_0_annotation_1)
  deps_type=str, [](https://ai.pydantic.dev/tools/#__code_0_annotation_2)
  system_prompt=(
    "You're a dice game, you should roll the die and see if the number "
    "you get back matches the user's guess. If so, tell them they're a winner. "
    "Use the player's name in the response."
  ),
)

@agent.tool_plain [](https://ai.pydantic.dev/tools/#__code_0_annotation_3)
defroll_die() -> str:
"""Roll a six-sided die and return the result."""
  return str(random.randint(1, 6))

@agent.tool [](https://ai.pydantic.dev/tools/#__code_0_annotation_4)
defget_player_name(ctx: RunContext[str]) -> str:
"""Get the player's name."""
  return ctx.deps

dice_result = agent.run_sync('My guess is 4', deps='Anne') [](https://ai.pydantic.dev/tools/#__code_0_annotation_5)
print(dice_result.data)
#> Congratulations Anne, you guessed correctly! You're a winner!

```

_(This example is complete, it can be run "as is")_
Let's print the messages from that game to see what happened:
dice_game_messages.py```
fromdice_gameimport dice_result
print(dice_result.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content="You're a dice game, you should roll the die and see if the number you get back matches the user's guess. If so, tell them they're a winner. Use the player's name in the response.",
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='My guess is 4',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      ToolCallPart(
        tool_name='roll_die', args={}, tool_call_id=None, part_kind='tool-call'
      )
    ],
    model_name='gemini-1.5-flash',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      ToolReturnPart(
        tool_name='roll_die',
        content='4',
        tool_call_id=None,
        timestamp=datetime.datetime(...),
        part_kind='tool-return',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      ToolCallPart(
        tool_name='get_player_name',
        args={},
        tool_call_id=None,
        part_kind='tool-call',
      )
    ],
    model_name='gemini-1.5-flash',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      ToolReturnPart(
        tool_name='get_player_name',
        content='Anne',
        tool_call_id=None,
        timestamp=datetime.datetime(...),
        part_kind='tool-return',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content="Congratulations Anne, you guessed correctly! You're a winner!",
        part_kind='text',
      )
    ],
    model_name='gemini-1.5-flash',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```

We can represent this with a diagram:
## Registering Function Tools via kwarg
As well as using the decorators, we can register tools via the `tools` argument to the [`Agent` constructor](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.__init__). This is useful when you want to reuse tools, and can also give more fine-grained control over the tools.
dice_game_tool_kwarg.py```
importrandom
frompydantic_aiimport Agent, RunContext, Tool

defroll_die() -> str:
"""Roll a six-sided die and return the result."""
  return str(random.randint(1, 6))

defget_player_name(ctx: RunContext[str]) -> str:
"""Get the player's name."""
  return ctx.deps

agent_a = Agent(
  'google-gla:gemini-1.5-flash',
  deps_type=str,
  tools=[roll_die, get_player_name], [](https://ai.pydantic.dev/tools/#__code_2_annotation_1)
)
agent_b = Agent(
  'google-gla:gemini-1.5-flash',
  deps_type=str,
  tools=[ [](https://ai.pydantic.dev/tools/#__code_2_annotation_2)
    Tool(roll_die, takes_ctx=False),
    Tool(get_player_name, takes_ctx=True),
  ],
)
dice_result = agent_b.run_sync('My guess is 4', deps='Anne')
print(dice_result.data)
#> Congratulations Anne, you guessed correctly! You're a winner!

```

_(This example is complete, it can be run "as is")_
## Function Tools vs. Structured Results
As the name suggests, function tools use the model's "tools" or "functions" API to let the model know what is available to call. Tools or functions are also used to define the schema(s) for structured responses, thus a model might have access to many tools, some of which call function tools while others end the run and return a result.
## Function tools and schema
Function parameters are extracted from the function signature, and all parameters except `RunContext` are used to build the schema for that tool call.
Even better, PydanticAI extracts the docstring from functions and (thanks to [griffe](https://mkdocstrings.github.io/griffe/)) extracts parameter descriptions from the docstring and adds them to the schema.
[Griffe supports](https://mkdocstrings.github.io/griffe/reference/docstrings/#docstrings) extracting parameter descriptions from `google`, `numpy`, and `sphinx` style docstrings. PydanticAI will infer the format to use based on the docstring, but you can explicitly set it using [`docstring_format`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat). You can also enforce parameter requirements by setting `require_parameter_descriptions=True`. This will raise a [`UserError`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UserError) if a parameter description is missing.
To demonstrate a tool's schema, here we use [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel) to print the schema a model would receive:
tool_schema.py```
frompydantic_aiimport Agent
frompydantic_ai.messagesimport ModelMessage, ModelResponse, TextPart
frompydantic_ai.models.functionimport AgentInfo, FunctionModel
agent = Agent()

@agent.tool_plain(docstring_format='google', require_parameter_descriptions=True)
deffoobar(a: int, b: str, c: dict[str, list[float]]) -> str:
"""Get me foobar.
  Args:
    a: apple pie
    b: banana cake
    c: carrot smoothie
  """
  return f'{a}{b}{c}'

defprint_schema(messages: list[ModelMessage], info: AgentInfo) -> ModelResponse:
  tool = info.function_tools[0]
  print(tool.description)
  #> Get me foobar.
  print(tool.parameters_json_schema)
"""
  {
    'properties': {
      'a': {'description': 'apple pie', 'title': 'A', 'type': 'integer'},
      'b': {'description': 'banana cake', 'title': 'B', 'type': 'string'},
      'c': {
        'additionalProperties': {'items': {'type': 'number'}, 'type': 'array'},
        'description': 'carrot smoothie',
        'title': 'C',
        'type': 'object',
      },
    },
    'required': ['a', 'b', 'c'],
    'type': 'object',
    'additionalProperties': False,
  }
  """
  return ModelResponse(parts=[TextPart('foobar')])

agent.run_sync('hello', model=FunctionModel(print_schema))

```

_(This example is complete, it can be run "as is")_
The return type of tool can be anything which Pydantic can serialize to JSON as some models (e.g. Gemini) support semi-structured return values, some expect text (OpenAI) but seem to be just as good at extracting meaning from the data. If a Python object is returned and the model expects a string, the value will be serialized to JSON.
If a tool has a single parameter that can be represented as an object in JSON schema (e.g. dataclass, TypedDict, pydantic model), the schema for the tool is simplified to be just that object.
Here's an example where we use [`TestModel.last_model_request_parameters`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel.last_model_request_parameters) to inspect the tool schema that would be passed to the model.
single_parameter_tool.py```
frompydanticimport BaseModel
frompydantic_aiimport Agent
frompydantic_ai.models.testimport TestModel
agent = Agent()

classFoobar(BaseModel):
"""This is a Foobar"""
  x: int
  y: str
  z: float = 3.14

@agent.tool_plain
deffoobar(f: Foobar) -> str:
  return str(f)

test_model = TestModel()
result = agent.run_sync('hello', model=test_model)
print(result.data)
#> {"foobar":"x=0 y='a' z=3.14"}
print(test_model.last_model_request_parameters.function_tools)
"""
[
  ToolDefinition(
    name='foobar',
    description='This is a Foobar',
    parameters_json_schema={
      'properties': {
        'x': {'title': 'X', 'type': 'integer'},
        'y': {'title': 'Y', 'type': 'string'},
        'z': {'default': 3.14, 'title': 'Z', 'type': 'number'},
      },
      'required': ['x', 'y'],
      'title': 'Foobar',
      'type': 'object',
    },
    outer_typed_dict_key=None,
  )
]
"""

```

_(This example is complete, it can be run "as is")_
## Dynamic Function tools
Tools can optionally be defined with another function: `prepare`, which is called at each step of a run to customize the definition of the tool passed to the model, or omit the tool completely from that step.
A `prepare` method can be registered via the `prepare` kwarg to any of the tool registration mechanisms:
  * [`@agent.tool`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool) decorator
  * [`@agent.tool_plain`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.tool_plain) decorator
  * [`Tool`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool) dataclass


The `prepare` method, should be of type [`ToolPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc), a function which takes [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext) and a pre-built [`ToolDefinition`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition), and should either return that `ToolDefinition` with or without modifying it, return a new `ToolDefinition`, or return `None` to indicate this tools should not be registered for that step.
Here's a simple `prepare` method that only includes the tool if the value of the dependency is `42`.
As with the previous example, we use [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel) to demonstrate the behavior without calling a real model.
tool_only_if_42.py```
fromtypingimport Union
frompydantic_aiimport Agent, RunContext
frompydantic_ai.toolsimport ToolDefinition
agent = Agent('test')

async defonly_if_42(
  ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
  if ctx.deps == 42:
    return tool_def

@agent.tool(prepare=only_if_42)
defhitchhiker(ctx: RunContext[int], answer: str) -> str:
  return f'{ctx.deps}{answer}'

result = agent.run_sync('testing...', deps=41)
print(result.data)
#> success (no tool calls)
result = agent.run_sync('testing...', deps=42)
print(result.data)
#> {"hitchhiker":"42 a"}

```

_(This example is complete, it can be run "as is")_
Here's a more complex example where we change the description of the `name` parameter to based on the value of `deps`
For the sake of variation, we create this tool using the [`Tool`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool) dataclass.
customize_name.py```
from__future__import annotations
fromtypingimport Literal
frompydantic_aiimport Agent, RunContext
frompydantic_ai.models.testimport TestModel
frompydantic_ai.toolsimport Tool, ToolDefinition

defgreet(name: str) -> str:
  return f'hello {name}'

async defprepare_greet(
  ctx: RunContext[Literal['human', 'machine']], tool_def: ToolDefinition
) -> ToolDefinition | None:
  d = f'Name of the {ctx.deps} to greet.'
  tool_def.parameters_json_schema['properties']['name']['description'] = d
  return tool_def

greet_tool = Tool(greet, prepare=prepare_greet)
test_model = TestModel()
agent = Agent(test_model, tools=[greet_tool], deps_type=Literal['human', 'machine'])
result = agent.run_sync('testing...', deps='human')
print(result.data)
#> {"greet":"hello a"}
print(test_model.last_model_request_parameters.function_tools)
"""
[
  ToolDefinition(
    name='greet',
    description='',
    parameters_json_schema={
      'properties': {
        'name': {
          'title': 'Name',
          'type': 'string',
          'description': 'Name of the human to greet.',
        }
      },
      'required': ['name'],
      'type': 'object',
      'additionalProperties': False,
    },
    outer_typed_dict_key=None,
  )
]
"""

```

_(This example is complete, it can be run "as is")_
© Pydantic Services Inc. 2024 to present 
