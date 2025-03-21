[ Skip to content ](https://ai.pydantic.dev/message-history/#messages-and-chat-history)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Messages and chat history 
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
    * Messages and chat history  [ Messages and chat history  ](https://ai.pydantic.dev/message-history/) Table of contents 
      * [ Accessing Messages from Results  ](https://ai.pydantic.dev/message-history/#accessing-messages-from-results)
      * [ Using Messages as Input for Further Agent Runs  ](https://ai.pydantic.dev/message-history/#using-messages-as-input-for-further-agent-runs)
      * [ Storing and loading messages (to JSON)  ](https://ai.pydantic.dev/message-history/#storing-and-loading-messages-to-json)
      * [ Other ways of using messages  ](https://ai.pydantic.dev/message-history/#other-ways-of-using-messages)
      * [ Examples  ](https://ai.pydantic.dev/message-history/#examples)
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
  * [ Accessing Messages from Results  ](https://ai.pydantic.dev/message-history/#accessing-messages-from-results)
  * [ Using Messages as Input for Further Agent Runs  ](https://ai.pydantic.dev/message-history/#using-messages-as-input-for-further-agent-runs)
  * [ Storing and loading messages (to JSON)  ](https://ai.pydantic.dev/message-history/#storing-and-loading-messages-to-json)
  * [ Other ways of using messages  ](https://ai.pydantic.dev/message-history/#other-ways-of-using-messages)
  * [ Examples  ](https://ai.pydantic.dev/message-history/#examples)


# Messages and chat history
PydanticAI provides access to messages exchanged during an agent run. These messages can be used both to continue a coherent conversation, and to understand how an agent performed.
### Accessing Messages from Results
After running an agent, you can access the messages exchanged during that run from the `result` object.
Both [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult) (returned by [`Agent.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run), [`Agent.run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_sync)) and [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult) (returned by [`Agent.run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_stream)) have the following methods:
  * [`all_messages()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.all_messages): returns all messages, including messages from prior runs. There's also a variant that returns JSON bytes, [`all_messages_json()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.all_messages_json).
  * [`new_messages()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.new_messages): returns only the messages from the current run. There's also a variant that returns JSON bytes, [`new_messages_json()`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult.new_messages_json).


StreamedRunResult and complete messages
On [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult), the messages returned from these methods will only include the final result message once the stream has finished.
E.g. you've awaited one of the following coroutines:
  * [`StreamedRunResult.stream()`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream)
  * [`StreamedRunResult.stream_text()`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_text)
  * [`StreamedRunResult.stream_structured()`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_structured)
  * [`StreamedRunResult.get_data()`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.get_data)


**Note:** The final result message will NOT be added to result messages if you use [`.stream_text(delta=True)`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult.stream_text) since in this case the result content is never built as one string.
Example of accessing methods on a [`RunResult`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.AgentRunResult) :
run_result_messages.py```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result = agent.run_sync('Tell me a joke.')
print(result.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
# all messages from the run
print(result.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='gpt-4o',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```

_(This example is complete, it can be run "as is")_
Example of accessing methods on a [`StreamedRunResult`](https://ai.pydantic.dev/api/result/#pydantic_ai.result.StreamedRunResult) :
streamed_run_result_messages.py```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')

async defmain():
  async with agent.run_stream('Tell me a joke.') as result:
    # incomplete messages before the stream finishes
    print(result.all_messages())
"""
    [
      ModelRequest(
        parts=[
          SystemPromptPart(
            content='Be a helpful assistant.',
            dynamic_ref=None,
            part_kind='system-prompt',
          ),
          UserPromptPart(
            content='Tell me a joke.',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          ),
        ],
        kind='request',
      )
    ]
    """
    async for text in result.stream_text():
      print(text)
      #> Did you hear
      #> Did you hear about the toothpaste
      #> Did you hear about the toothpaste scandal? They called
      #> Did you hear about the toothpaste scandal? They called it Colgate.
    # complete messages once the stream finishes
    print(result.all_messages())
"""
    [
      ModelRequest(
        parts=[
          SystemPromptPart(
            content='Be a helpful assistant.',
            dynamic_ref=None,
            part_kind='system-prompt',
          ),
          UserPromptPart(
            content='Tell me a joke.',
            timestamp=datetime.datetime(...),
            part_kind='user-prompt',
          ),
        ],
        kind='request',
      ),
      ModelResponse(
        parts=[
          TextPart(
            content='Did you hear about the toothpaste scandal? They called it Colgate.',
            part_kind='text',
          )
        ],
        model_name='gpt-4o',
        timestamp=datetime.datetime(...),
        kind='response',
      ),
    ]
    """

```

_(This example is complete, it can be run "as is" — you'll need to add`asyncio.run(main())` to run `main`)_
### Using Messages as Input for Further Agent Runs
The primary use of message histories in PydanticAI is to maintain context across multiple agent runs.
To use existing messages in a run, pass them to the `message_history` parameter of [`Agent.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run), [`Agent.run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_sync) or [`Agent.run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_stream).
If `message_history` is set and not empty, a new system prompt is not generated — we assume the existing message history includes a system prompt.
Reusing messages in a conversation```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result1 = agent.run_sync('Tell me a joke.')
print(result1.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
result2 = agent.run_sync('Explain?', message_history=result1.new_messages())
print(result2.data)
#> This is an excellent joke invented by Samuel Colvin, it needs no explanation.
print(result2.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='gpt-4o',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      UserPromptPart(
        content='Explain?',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='This is an excellent joke invented by Samuel Colvin, it needs no explanation.',
        part_kind='text',
      )
    ],
    model_name='gpt-4o',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```

_(This example is complete, it can be run "as is")_
## Storing and loading messages (to JSON)
While maintaining conversation state in memory is enough for many applications, often times you may want to store the messages history of an agent run on disk or in a database. This might be for evals, for sharing data between Python and JavaScript/TypeScript, or any number of other use cases.
The intended way to do this is using a `TypeAdapter`.
We export [`ModelMessagesTypeAdapter`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessagesTypeAdapter) that can be used for this, or you can create your own.
Here's an example showing how:
serialize messages to json```
frompydantic_coreimport to_jsonable_python
frompydantic_aiimport Agent
frompydantic_ai.messagesimport ModelMessagesTypeAdapter [](https://ai.pydantic.dev/message-history/#__code_3_annotation_1)
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result1 = agent.run_sync('Tell me a joke.')
history_step_1 = result1.all_messages()
as_python_objects = to_jsonable_python(history_step_1) [](https://ai.pydantic.dev/message-history/#__code_3_annotation_2)
same_history_as_step_1 = ModelMessagesTypeAdapter.validate_python(as_python_objects)
result2 = agent.run_sync( [](https://ai.pydantic.dev/message-history/#__code_3_annotation_3)
  'Tell me a different joke.', message_history=same_history_as_step_1
)

```

_(This example is complete, it can be run "as is")_
## Other ways of using messages
Since messages are defined by simple dataclasses, you can manually create and manipulate, e.g. for testing.
The message format is independent of the model used, so you can use messages in different agents, or the same agent with different models.
In the example below, we reuse the message from the first agent run, which uses the `openai:gpt-4o` model, in a second agent run using the `google-gla:gemini-1.5-pro` model.
Reusing messages with a different model```
frompydantic_aiimport Agent
agent = Agent('openai:gpt-4o', system_prompt='Be a helpful assistant.')
result1 = agent.run_sync('Tell me a joke.')
print(result1.data)
#> Did you hear about the toothpaste scandal? They called it Colgate.
result2 = agent.run_sync(
  'Explain?',
  model='google-gla:gemini-1.5-pro',
  message_history=result1.new_messages(),
)
print(result2.data)
#> This is an excellent joke invented by Samuel Colvin, it needs no explanation.
print(result2.all_messages())
"""
[
  ModelRequest(
    parts=[
      SystemPromptPart(
        content='Be a helpful assistant.',
        dynamic_ref=None,
        part_kind='system-prompt',
      ),
      UserPromptPart(
        content='Tell me a joke.',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      ),
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='Did you hear about the toothpaste scandal? They called it Colgate.',
        part_kind='text',
      )
    ],
    model_name='gpt-4o',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
  ModelRequest(
    parts=[
      UserPromptPart(
        content='Explain?',
        timestamp=datetime.datetime(...),
        part_kind='user-prompt',
      )
    ],
    kind='request',
  ),
  ModelResponse(
    parts=[
      TextPart(
        content='This is an excellent joke invented by Samuel Colvin, it needs no explanation.',
        part_kind='text',
      )
    ],
    model_name='gemini-1.5-pro',
    timestamp=datetime.datetime(...),
    kind='response',
  ),
]
"""

```

## Examples
For a more complete example of using messages in conversations, see the [chat app](https://ai.pydantic.dev/examples/chat-app/) example.
© Pydantic Services Inc. 2024 to present 
