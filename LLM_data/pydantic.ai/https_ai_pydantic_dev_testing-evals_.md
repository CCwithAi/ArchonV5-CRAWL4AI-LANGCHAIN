[ Skip to content ](https://ai.pydantic.dev/testing-evals/#testing-and-evals)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Testing and Evals 
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
    * Testing and Evals  [ Testing and Evals  ](https://ai.pydantic.dev/testing-evals/) Table of contents 
      * [ Unit tests  ](https://ai.pydantic.dev/testing-evals/#unit-tests)
        * [ Unit testing with TestModel  ](https://ai.pydantic.dev/testing-evals/#unit-testing-with-testmodel)
        * [ Unit testing with FunctionModel  ](https://ai.pydantic.dev/testing-evals/#unit-testing-with-functionmodel)
        * [ Overriding model via pytest fixtures  ](https://ai.pydantic.dev/testing-evals/#overriding-model-via-pytest-fixtures)
      * [ Evals  ](https://ai.pydantic.dev/testing-evals/#evals)
        * [ Measuring performance  ](https://ai.pydantic.dev/testing-evals/#measuring-performance)
        * [ System prompt customization  ](https://ai.pydantic.dev/testing-evals/#system-prompt-customization)
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
  * [ Unit tests  ](https://ai.pydantic.dev/testing-evals/#unit-tests)
    * [ Unit testing with TestModel  ](https://ai.pydantic.dev/testing-evals/#unit-testing-with-testmodel)
    * [ Unit testing with FunctionModel  ](https://ai.pydantic.dev/testing-evals/#unit-testing-with-functionmodel)
    * [ Overriding model via pytest fixtures  ](https://ai.pydantic.dev/testing-evals/#overriding-model-via-pytest-fixtures)
  * [ Evals  ](https://ai.pydantic.dev/testing-evals/#evals)
    * [ Measuring performance  ](https://ai.pydantic.dev/testing-evals/#measuring-performance)
    * [ System prompt customization  ](https://ai.pydantic.dev/testing-evals/#system-prompt-customization)


# Testing and Evals
With PydanticAI and LLM integrations in general, there are two distinct kinds of test:
  1. **Unit tests** — tests of your application code, and whether it's behaving correctly
  2. **Evals** — tests of the LLM, and how good or bad its responses are


For the most part, these two kinds of tests have pretty separate goals and considerations.
## Unit tests
Unit tests for PydanticAI code are just like unit tests for any other Python code.
Because for the most part they're nothing new, we have pretty well established tools and patterns for writing and running these kinds of tests.
Unless you're really sure you know better, you'll probably want to follow roughly this strategy:
  * Use [`pytest`](https://docs.pytest.org/en/stable/) as your test harness
  * If you find yourself typing out long assertions, use [inline-snapshot](https://15r10nk.github.io/inline-snapshot/latest/)
  * Similarly, [dirty-equals](https://dirty-equals.helpmanual.io/latest/) can be useful for comparing large data structures
  * Use [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel) or [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel) in place of your actual model to avoid the usage, latency and variability of real LLM calls
  * Use [`Agent.override`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.override) to replace your model inside your application logic
  * Set [`ALLOW_MODEL_REQUESTS=False`](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.ALLOW_MODEL_REQUESTS) globally to block any requests from being made to non-test models accidentally


### Unit testing with `TestModel`
The simplest and fastest way to exercise most of your application code is using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel), this will (by default) call all tools in the agent, then return either plain text or a structured response depending on the return type of the agent.
`TestModel` is not magic
The "clever" (but not too clever) part of `TestModel` is that it will attempt to generate valid structured data for [function tools](https://ai.pydantic.dev/tools/) and [result types](https://ai.pydantic.dev/results/#structured-result-validation) based on the schema of the registered tools.
There's no ML or AI in `TestModel`, it's just plain old procedural Python code that tries to generate data that satisfies the JSON schema of a tool.
The resulting data won't look pretty or relevant, but it should pass Pydantic's validation in most cases. If you want something more sophisticated, use [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel) and write your own data generation logic.
Let's write unit tests for the following application code:
weather_app.py```
importasyncio
fromdatetimeimport date
frompydantic_aiimport Agent, RunContext
fromfake_databaseimport DatabaseConn [](https://ai.pydantic.dev/testing-evals/#__code_0_annotation_1)
fromweather_serviceimport WeatherService [](https://ai.pydantic.dev/testing-evals/#__code_0_annotation_2)
weather_agent = Agent(
  'openai:gpt-4o',
  deps_type=WeatherService,
  system_prompt='Providing a weather forecast at the locations the user provides.',
)

@weather_agent.tool
defweather_forecast(
  ctx: RunContext[WeatherService], location: str, forecast_date: date
) -> str:
  if forecast_date < date.today(): [](https://ai.pydantic.dev/testing-evals/#__code_0_annotation_3)
    return ctx.deps.get_historic_weather(location, forecast_date)
  else:
    return ctx.deps.get_forecast(location, forecast_date)

async defrun_weather_forecast( [](https://ai.pydantic.dev/testing-evals/#__code_0_annotation_4)
  user_prompts: list[tuple[str, int]], conn: DatabaseConn
):
"""Run weather forecast for a list of user prompts and save."""
  async with WeatherService() as weather_service:
    async defrun_forecast(prompt: str, user_id: int):
      result = await weather_agent.run(prompt, deps=weather_service)
      await conn.store_forecast(user_id, result.data)
    # run all prompts in parallel
    await asyncio.gather(
      *(run_forecast(prompt, user_id) for (prompt, user_id) in user_prompts)
    )

```

Here we have a function that takes a list of `(user_prompt, user_id)` tuples, gets a weather forecast for each prompt, and stores the result in the database.
**We want to test this code without having to mock certain objects or modify our code so we can pass test objects in.**
Here's how we would write tests using [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel):
test_weather_app.py```
fromdatetimeimport timezone
importpytest
fromdirty_equalsimport IsNow
frompydantic_aiimport models, capture_run_messages
frompydantic_ai.models.testimport TestModel
frompydantic_ai.messagesimport (
  ModelResponse,
  SystemPromptPart,
  TextPart,
  ToolCallPart,
  ToolReturnPart,
  UserPromptPart,
  ModelRequest,
)
fromfake_databaseimport DatabaseConn
fromweather_appimport run_weather_forecast, weather_agent
pytestmark = pytest.mark.anyio [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_1)
models.ALLOW_MODEL_REQUESTS = False [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_2)

async deftest_forecast():
  conn = DatabaseConn()
  user_id = 1
  with capture_run_messages() as messages:
    with weather_agent.override(model=TestModel()): [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_3)
      prompt = 'What will the weather be like in London on 2024-11-28?'
      await run_weather_forecast([(prompt, user_id)], conn) [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_4)
  forecast = await conn.get_forecast(user_id)
  assert forecast == '{"weather_forecast":"Sunny with a chance of rain"}' [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_5)
  assert messages == [ [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_6)
    ModelRequest(
      parts=[
        SystemPromptPart(
          content='Providing a weather forecast at the locations the user provides.',
        ),
        UserPromptPart(
          content='What will the weather be like in London on 2024-11-28?',
          timestamp=IsNow(tz=timezone.utc), [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_7)
        ),
      ]
    ),
    ModelResponse(
      parts=[
        ToolCallPart(
          tool_name='weather_forecast',
          args={
            'location': 'a',
            'forecast_date': '2024-01-01', [](https://ai.pydantic.dev/testing-evals/#__code_1_annotation_8)
          },
          tool_call_id=None,
        )
      ],
      model_name='test',
      timestamp=IsNow(tz=timezone.utc),
    ),
    ModelRequest(
      parts=[
        ToolReturnPart(
          tool_name='weather_forecast',
          content='Sunny with a chance of rain',
          tool_call_id=None,
          timestamp=IsNow(tz=timezone.utc),
        ),
      ],
    ),
    ModelResponse(
      parts=[
        TextPart(
          content='{"weather_forecast":"Sunny with a chance of rain"}',
        )
      ],
      model_name='test',
      timestamp=IsNow(tz=timezone.utc),
    ),
  ]

```

### Unit testing with `FunctionModel`
The above tests are a great start, but careful readers will notice that the `WeatherService.get_forecast` is never called since `TestModel` calls `weather_forecast` with a date in the past.
To fully exercise `weather_forecast`, we need to use [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel) to customise how the tools is called.
Here's an example of using `FunctionModel` to test the `weather_forecast` tool with custom inputs
test_weather_app2.py```
importre
importpytest
frompydantic_aiimport models
frompydantic_ai.messagesimport (
  ModelMessage,
  ModelResponse,
  TextPart,
  ToolCallPart,
)
frompydantic_ai.models.functionimport AgentInfo, FunctionModel
fromfake_databaseimport DatabaseConn
fromweather_appimport run_weather_forecast, weather_agent
pytestmark = pytest.mark.anyio
models.ALLOW_MODEL_REQUESTS = False

defcall_weather_forecast( [](https://ai.pydantic.dev/testing-evals/#__code_2_annotation_1)
  messages: list[ModelMessage], info: AgentInfo
) -> ModelResponse:
  if len(messages) == 1:
    # first call, call the weather forecast tool
    user_prompt = messages[0].parts[-1]
    m = re.search(r'\d{4}-\d{2}-\d{2}', user_prompt.content)
    assert m is not None
    args = {'location': 'London', 'forecast_date': m.group()} [](https://ai.pydantic.dev/testing-evals/#__code_2_annotation_2)
    return ModelResponse(parts=[ToolCallPart('weather_forecast', args)])
  else:
    # second call, return the forecast
    msg = messages[-1].parts[0]
    assert msg.part_kind == 'tool-return'
    return ModelResponse(parts=[TextPart(f'The forecast is: {msg.content}')])

async deftest_forecast_future():
  conn = DatabaseConn()
  user_id = 1
  with weather_agent.override(model=FunctionModel(call_weather_forecast)): [](https://ai.pydantic.dev/testing-evals/#__code_2_annotation_3)
    prompt = 'What will the weather be like in London on 2032-01-01?'
    await run_weather_forecast([(prompt, user_id)], conn)
  forecast = await conn.get_forecast(user_id)
  assert forecast == 'The forecast is: Rainy with a chance of sun'

```

### Overriding model via pytest fixtures
If you're writing lots of tests that all require model to be overridden, you can use [pytest fixtures](https://docs.pytest.org/en/6.2.x/fixture.html) to override the model with [`TestModel`](https://ai.pydantic.dev/api/models/test/#pydantic_ai.models.test.TestModel) or [`FunctionModel`](https://ai.pydantic.dev/api/models/function/#pydantic_ai.models.function.FunctionModel) in a reusable way.
Here's an example of a fixture that overrides the model with `TestModel`:
tests.py```
importpytest
fromweather_appimport weather_agent
frompydantic_ai.models.testimport TestModel

@pytest.fixture
defoverride_weather_agent():
  with weather_agent.override(model=TestModel()):
    yield

async deftest_forecast(override_weather_agent: None):
  ...
  # test code here

```

## Evals
"Evals" refers to evaluating a models performance for a specific application.
Warning
Unlike unit tests, evals are an emerging art/science; anyone who claims to know for sure exactly how your evals should be defined can safely be ignored.
Evals are generally more like benchmarks than unit tests, they never "pass" although they do "fail"; you care mostly about how they change over time.
Since evals need to be run against the real model, then can be slow and expensive to run, you generally won't want to run them in CI for every commit.
### Measuring performance
The hardest part of evals is measuring how well the model has performed.
In some cases (e.g. an agent to generate SQL) there are simple, easy to run tests that can be used to measure performance (e.g. is the SQL valid? Does it return the right results? Does it return just the right results?).
In other cases (e.g. an agent that gives advice on quitting smoking) it can be very hard or impossible to make quantitative measures of performance — in the smoking case you'd really need to run a double-blind trial over months, then wait 40 years and observe health outcomes to know if changes to your prompt were an improvement.
There are a few different strategies you can use to measure performance:
  * **End to end, self-contained tests** — like the SQL example, we can test the final result of the agent near-instantly
  * **Synthetic self-contained tests** — writing unit test style checks that the output is as expected, checks like `'chewing gum' in response`, while these checks might seem simplistic they can be helpful, one nice characteristic is that it's easy to tell what's wrong when they fail
  * **LLMs evaluating LLMs** — using another models, or even the same model with a different prompt to evaluate the performance of the agent (like when the class marks each other's homework because the teacher has a hangover), while the downsides and complexities of this approach are obvious, some think it can be a useful tool in the right circumstances
  * **Evals in prod** — measuring the end results of the agent in production, then creating a quantitative measure of performance, so you can easily measure changes over time as you change the prompt or model used, [logfire](https://ai.pydantic.dev/logfire/) can be extremely useful in this case since you can write a custom query to measure the performance of your agent


### System prompt customization
The system prompt is the developer's primary tool in controlling an agent's behavior, so it's often useful to be able to customise the system prompt and see how performance changes. This is particularly relevant when the system prompt contains a list of examples and you want to understand how changing that list affects the model's performance.
Let's assume we have the following app for running SQL generated from a user prompt (this examples omits a lot of details for brevity, see the [SQL gen](https://ai.pydantic.dev/examples/sql-gen/) example for a more complete code):
sql_app.py```
importjson
frompathlibimport Path
fromtypingimport Union
frompydantic_aiimport Agent, RunContext
fromfake_databaseimport DatabaseConn

classSqlSystemPrompt: [](https://ai.pydantic.dev/testing-evals/#__code_4_annotation_1)
  def__init__(
    self, examples: Union[list[dict[str, str]], None] = None, db: str = 'PostgreSQL'
  ):
    if examples is None:
      # if examples aren't provided, load them from file, this is the default
      with Path('examples.json').open('rb') as f:
        self.examples = json.load(f)
    else:
      self.examples = examples
    self.db = db
  defbuild_prompt(self) -> str: [](https://ai.pydantic.dev/testing-evals/#__code_4_annotation_2)
    return f"""\
Given the following {self.db} table of records, your job is to
write a SQL query that suits the user's request.
Database schema:
CREATE TABLE records (
 ...
);
{''.join(self.format_example(example)forexampleinself.examples)}
"""
  @staticmethod
  defformat_example(example: dict[str, str]) -> str: [](https://ai.pydantic.dev/testing-evals/#__code_4_annotation_3)
    return f"""\
<example>
 <request>{example['request']}</request>
 <sql>{example['sql']}</sql>
</example>
"""

sql_agent = Agent(
  'google-gla:gemini-1.5-flash',
  deps_type=SqlSystemPrompt,
)

@sql_agent.system_prompt
async defsystem_prompt(ctx: RunContext[SqlSystemPrompt]) -> str:
  return ctx.deps.build_prompt()

async defuser_search(user_prompt: str) -> list[dict[str, str]]:
"""Search the database based on the user's prompts."""
  ... [](https://ai.pydantic.dev/testing-evals/#__code_4_annotation_4)
  result = await sql_agent.run(user_prompt, deps=SqlSystemPrompt())
  conn = DatabaseConn()
  return await conn.execute(result.data)

```

`examples.json` looks something like this:
```
request: show me error records with the tag "foobar"
response: SELECT * FROM records WHERE level = 'error' and 'foobar' = ANY(tags)

```

examples.json```
{
"examples":[
{
"request":"Show me all records",
"sql":"SELECT * FROM records;"
},
{
"request":"Show me all records from 2021",
"sql":"SELECT * FROM records WHERE date_trunc('year', date) = '2021-01-01';"
},
{
"request":"show me error records with the tag 'foobar'",
"sql":"SELECT * FROM records WHERE level = 'error' and 'foobar' = ANY(tags);"
},
...
]
}

```

Now we want a way to quantify the success of the SQL generation so we can judge how changes to the agent affect its performance.
We can use [`Agent.override`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.override) to replace the system prompt with a custom one that uses a subset of examples, and then run the application code (in this case `user_search`). We also run the actual SQL from the examples and compare the "correct" result from the example SQL to the SQL generated by the agent. (We compare the results of running the SQL rather than the SQL itself since the SQL might be semantically equivalent but written in a different way).
To get a quantitative measure of performance, we assign points to each run as follows:
  * **-100** points if the generated SQL is invalid
  * **-1** point for each row returned by the agent (so returning lots of results is discouraged)
  * **+5** points for each row returned by the agent that matches the expected result


We use 5-fold cross-validation to judge the performance of the agent using our existing set of examples.
sql_app_evals.py```
importjson
importstatistics
frompathlibimport Path
fromitertoolsimport chain
fromfake_databaseimport DatabaseConn, QueryError
fromsql_appimport sql_agent, SqlSystemPrompt, user_search

async defmain():
  with Path('examples.json').open('rb') as f:
    examples = json.load(f)
  # split examples into 5 folds
  fold_size = len(examples) // 5
  folds = [examples[i : i + fold_size] for i in range(0, len(examples), fold_size)]
  conn = DatabaseConn()
  scores = []
  for i, fold in enumerate(folds):
    fold_score = 0
    # build all other folds into a list of examples
    other_folds = list(chain(*(f for j, f in enumerate(folds) if j != i)))
    # create a new system prompt with the other fold examples
    system_prompt = SqlSystemPrompt(examples=other_folds)
    # override the system prompt with the new one
    with sql_agent.override(deps=system_prompt):
      for case in fold:
        try:
          agent_results = await user_search(case['request'])
        except QueryError as e:
          print(f'Fold {i}{case}: {e}')
          fold_score -= 100
        else:
          # get the expected results using the SQL from this case
          expected_results = await conn.execute(case['sql'])
        agent_ids = [r['id'] for r in agent_results]
        # each returned value has a score of -1
        fold_score -= len(agent_ids)
        expected_ids = {r['id'] for r in expected_results}
        # each return value that matches the expected value has a score of 3
        fold_score += 5 * len(set(agent_ids) & expected_ids)
    scores.append(fold_score)
  overall_score = statistics.mean(scores)
  print(f'Overall score: {overall_score:0.2f}')
  #> Overall score: 12.00

```

We can then change the prompt, the model, or the examples and see how the score changes over time.
© Pydantic Services Inc. 2024 to present 
