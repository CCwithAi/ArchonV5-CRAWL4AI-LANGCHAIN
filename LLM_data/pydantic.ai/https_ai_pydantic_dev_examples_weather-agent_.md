[ Skip to content ](https://ai.pydantic.dev/examples/weather-agent/#running-the-example)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Weather agent 
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
    * Weather agent  [ Weather agent  ](https://ai.pydantic.dev/examples/weather-agent/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/weather-agent/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/weather-agent/#example-code)
      * [ Running the UI  ](https://ai.pydantic.dev/examples/weather-agent/#running-the-ui)
      * [ UI Code  ](https://ai.pydantic.dev/examples/weather-agent/#ui-code)
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
  * [ Running the Example  ](https://ai.pydantic.dev/examples/weather-agent/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/weather-agent/#example-code)
  * [ Running the UI  ](https://ai.pydantic.dev/examples/weather-agent/#running-the-ui)
  * [ UI Code  ](https://ai.pydantic.dev/examples/weather-agent/#ui-code)


# Weather agent
Example of PydanticAI with multiple tools which the LLM needs to call in turn to answer a question.
Demonstrates:
  * [tools](https://ai.pydantic.dev/tools/)
  * [agent dependencies](https://ai.pydantic.dev/dependencies/)
  * [streaming text responses](https://ai.pydantic.dev/results/#streaming-text)
  * Building a [Gradio](https://www.gradio.app/) UI for the agent


In this case the idea is a "weather" agent — the user can ask for the weather in multiple locations, the agent will use the `get_lat_lng` tool to get the latitude and longitude of the locations, then use the `get_weather` tool to get the weather for those locations.
## Running the Example
To run this example properly, you might want to add two extra API keys **(Note if either key is missing, the code will fall back to dummy data, so they're not required)** :
  * A weather API key from [tomorrow.io](https://www.tomorrow.io/weather-api/) set via `WEATHER_API_KEY`
  * A geocoding API key from [geocode.maps.co](https://geocode.maps.co/) set via `GEO_API_KEY`


With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/weather-agent/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/weather-agent/#__tabbed_1_2)
```
python-mpydantic_ai_examples.weather_agent

```

```
uvrun-mpydantic_ai_examples.weather_agent

```

## Example Code
pydantic_ai_examples/weather_agent.py```
from__future__import annotations as _annotations
importasyncio
importos
fromdataclassesimport dataclass
fromtypingimport Any
importlogfire
fromdevtoolsimport debug
fromhttpximport AsyncClient
frompydantic_aiimport Agent, ModelRetry, RunContext
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')

@dataclass
classDeps:
  client: AsyncClient
  weather_api_key: str | None
  geo_api_key: str | None

weather_agent = Agent(
  'openai:gpt-4o',
  # 'Be concise, reply with one sentence.' is enough for some models (like openai) to use
  # the below tools appropriately, but others like anthropic and gemini require a bit more direction.
  system_prompt=(
    'Be concise, reply with one sentence.'
    'Use the `get_lat_lng` tool to get the latitude and longitude of the locations, '
    'then use the `get_weather` tool to get the weather.'
  ),
  deps_type=Deps,
  retries=2,
  instrument=True,
)

@weather_agent.tool
async defget_lat_lng(
  ctx: RunContext[Deps], location_description: str
) -> dict[str, float]:
"""Get the latitude and longitude of a location.
  Args:
    ctx: The context.
    location_description: A description of a location.
  """
  if ctx.deps.geo_api_key is None:
    # if no API key is provided, return a dummy response (London)
    return {'lat': 51.1, 'lng': -0.1}
  params = {
    'q': location_description,
    'api_key': ctx.deps.geo_api_key,
  }
  with logfire.span('calling geocode API', params=params) as span:
    r = await ctx.deps.client.get('https://geocode.maps.co/search', params=params)
    r.raise_for_status()
    data = r.json()
    span.set_attribute('response', data)
  if data:
    return {'lat': data[0]['lat'], 'lng': data[0]['lon']}
  else:
    raise ModelRetry('Could not find the location')

@weather_agent.tool
async defget_weather(ctx: RunContext[Deps], lat: float, lng: float) -> dict[str, Any]:
"""Get the weather at a location.
  Args:
    ctx: The context.
    lat: Latitude of the location.
    lng: Longitude of the location.
  """
  if ctx.deps.weather_api_key is None:
    # if no API key is provided, return a dummy response
    return {'temperature': '21 °C', 'description': 'Sunny'}
  params = {
    'apikey': ctx.deps.weather_api_key,
    'location': f'{lat},{lng}',
    'units': 'metric',
  }
  with logfire.span('calling weather API', params=params) as span:
    r = await ctx.deps.client.get(
      'https://api.tomorrow.io/v4/weather/realtime', params=params
    )
    r.raise_for_status()
    data = r.json()
    span.set_attribute('response', data)
  values = data['data']['values']
  # https://docs.tomorrow.io/reference/data-layers-weather-codes
  code_lookup = {
    1000: 'Clear, Sunny',
    1100: 'Mostly Clear',
    1101: 'Partly Cloudy',
    1102: 'Mostly Cloudy',
    1001: 'Cloudy',
    2000: 'Fog',
    2100: 'Light Fog',
    4000: 'Drizzle',
    4001: 'Rain',
    4200: 'Light Rain',
    4201: 'Heavy Rain',
    5000: 'Snow',
    5001: 'Flurries',
    5100: 'Light Snow',
    5101: 'Heavy Snow',
    6000: 'Freezing Drizzle',
    6001: 'Freezing Rain',
    6200: 'Light Freezing Rain',
    6201: 'Heavy Freezing Rain',
    7000: 'Ice Pellets',
    7101: 'Heavy Ice Pellets',
    7102: 'Light Ice Pellets',
    8000: 'Thunderstorm',
  }
  return {
    'temperature': f'{values["temperatureApparent"]:0.0f}°C',
    'description': code_lookup.get(values['weatherCode'], 'Unknown'),
  }

async defmain():
  async with AsyncClient() as client:
    # create a free API key at https://www.tomorrow.io/weather-api/
    weather_api_key = os.getenv('WEATHER_API_KEY')
    # create a free API key at https://geocode.maps.co/
    geo_api_key = os.getenv('GEO_API_KEY')
    deps = Deps(
      client=client, weather_api_key=weather_api_key, geo_api_key=geo_api_key
    )
    result = await weather_agent.run(
      'What is the weather like in London and in Wiltshire?', deps=deps
    )
    debug(result)
    print('Response:', result.data)

if __name__ == '__main__':
  asyncio.run(main())

```

## Running the UI
You can build multi-turn chat applications for your agent with [Gradio](https://www.gradio.app/), a framework for building AI web applications entirely in python. Gradio comes with built-in chat components and agent support so the entire UI will be implemented in a single python file!
Here's what the UI looks like for the weather agent:
Note, to run the UI, you'll need Python 3.10+.
```
pipinstallgradio>=5.9.0
python/uv-run-mpydantic_ai_examples.weather_agent_gradio

```

## UI Code
pydantic_ai_examples/weather_agent_gradio.py```
from__future__import annotations as _annotations
importjson
importos
fromhttpximport AsyncClient
frompydantic_ai.messagesimport ToolCallPart, ToolReturnPart
frompydantic_ai_examples.weather_agentimport Deps, weather_agent
try:
  importgradioasgr
except ImportError as e:
  raise ImportError(
    'Please install gradio with `pip install gradio`. You must use python>=3.10.'
  ) frome
TOOL_TO_DISPLAY_NAME = {'get_lat_lng': 'Geocoding API', 'get_weather': 'Weather API'}
client = AsyncClient()
weather_api_key = os.getenv('WEATHER_API_KEY')
# create a free API key at https://geocode.maps.co/
geo_api_key = os.getenv('GEO_API_KEY')
deps = Deps(client=client, weather_api_key=weather_api_key, geo_api_key=geo_api_key)

async defstream_from_agent(prompt: str, chatbot: list[dict], past_messages: list):
  chatbot.append({'role': 'user', 'content': prompt})
  yield gr.Textbox(interactive=False, value=''), chatbot, gr.skip()
  async with weather_agent.run_stream(
    prompt, deps=deps, message_history=past_messages
  ) as result:
    for message in result.new_messages():
      for call in message.parts:
        if isinstance(call, ToolCallPart):
          call_args = (
            call.args.args_json
            if hasattr(call.args, 'args_json')
            else json.dumps(call.args.args_dict)
          )
          metadata = {
            'title': f'🛠️ Using {TOOL_TO_DISPLAY_NAME[call.tool_name]}',
          }
          if call.tool_call_id is not None:
            metadata['id'] = {call.tool_call_id}
          gr_message = {
            'role': 'assistant',
            'content': 'Parameters: ' + call_args,
            'metadata': metadata,
          }
          chatbot.append(gr_message)
        if isinstance(call, ToolReturnPart):
          for gr_message in chatbot:
            if (
              gr_message.get('metadata', {}).get('id', '')
              == call.tool_call_id
            ):
              gr_message['content'] += (
                f'\nOutput: {json.dumps(call.content)}'
              )
        yield gr.skip(), chatbot, gr.skip()
    chatbot.append({'role': 'assistant', 'content': ''})
    async for message in result.stream_text():
      chatbot[-1]['content'] = message
      yield gr.skip(), chatbot, gr.skip()
    past_messages = result.all_messages()
    yield gr.Textbox(interactive=True), gr.skip(), past_messages

async defhandle_retry(chatbot, past_messages: list, retry_data: gr.RetryData):
  new_history = chatbot[: retry_data.index]
  previous_prompt = chatbot[retry_data.index]['content']
  past_messages = past_messages[: retry_data.index]
  async for update in stream_from_agent(previous_prompt, new_history, past_messages):
    yield update

defundo(chatbot, past_messages: list, undo_data: gr.UndoData):
  new_history = chatbot[: undo_data.index]
  past_messages = past_messages[: undo_data.index]
  return chatbot[undo_data.index]['content'], new_history, past_messages

defselect_data(message: gr.SelectData) -> str:
  return message.value['text']

with gr.Blocks() as demo:
  gr.HTML(
"""
<div style="display: flex; justify-content: center; align-items: center; gap: 2rem; padding: 1rem; width: 100%">
  <img src="https://ai.pydantic.dev/img/logo-white.svg" style="max-width: 200px; height: auto">
  <div>
    <h1 style="margin: 0 0 1rem 0">Weather Assistant</h1>
    <h3 style="margin: 0 0 0.5rem 0">
      This assistant answer your weather questions.
    </h3>
  </div>
</div>
"""
  )
  past_messages = gr.State([])
  chatbot = gr.Chatbot(
    label='Packing Assistant',
    type='messages',
    avatar_images=(None, 'https://ai.pydantic.dev/img/logo-white.svg'),
    examples=[
      {'text': 'What is the weather like in Miami?'},
      {'text': 'What is the weather like in London?'},
    ],
  )
  with gr.Row():
    prompt = gr.Textbox(
      lines=1,
      show_label=False,
      placeholder='What is the weather like in New York City?',
    )
  generation = prompt.submit(
    stream_from_agent,
    inputs=[prompt, chatbot, past_messages],
    outputs=[prompt, chatbot, past_messages],
  )
  chatbot.example_select(select_data, None, [prompt])
  chatbot.retry(
    handle_retry, [chatbot, past_messages], [prompt, chatbot, past_messages]
  )
  chatbot.undo(undo, [chatbot, past_messages], [prompt, chatbot, past_messages])

if __name__ == '__main__':
  demo.launch()

```

© Pydantic Services Inc. 2024 to present 
