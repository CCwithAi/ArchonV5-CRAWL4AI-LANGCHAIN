[ Skip to content ](https://ai.pydantic.dev/api/tools/#pydantic_aitools)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_ai.tools 
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
    * pydantic_ai.tools  [ pydantic_ai.tools  ](https://ai.pydantic.dev/api/tools/) Table of contents 
      * [ tools  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools)
      * [ AgentDepsT  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT)
      * [ RunContext  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext)
        * [ deps  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps)
        * [ model  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.model)
        * [ usage  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.usage)
        * [ prompt  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.prompt)
        * [ messages  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.messages)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.tool_call_id)
        * [ tool_name  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.tool_name)
        * [ retry  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.retry)
        * [ run_step  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.run_step)
      * [ ToolParams  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams)
      * [ SystemPromptFunc  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.SystemPromptFunc)
      * [ ToolFuncContext  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext)
      * [ ToolFuncPlain  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain)
      * [ ToolFuncEither  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither)
      * [ ToolPrepareFunc  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc)
      * [ DocstringFormat  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat)
      * [ Tool  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool)
        * [ __init__  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.__init__)
        * [ prepare_tool_def  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.prepare_tool_def)
        * [ run  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.run)
      * [ ObjectJsonSchema  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ObjectJsonSchema)
      * [ ToolDefinition  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition)
        * [ name  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.name)
        * [ description  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.description)
        * [ parameters_json_schema  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.parameters_json_schema)
        * [ outer_typed_dict_key  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.outer_typed_dict_key)
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
  * [ tools  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools)
  * [ AgentDepsT  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT)
  * [ RunContext  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext)
    * [ deps  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.deps)
    * [ model  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.model)
    * [ usage  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.usage)
    * [ prompt  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.prompt)
    * [ messages  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.messages)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.tool_call_id)
    * [ tool_name  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.tool_name)
    * [ retry  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.retry)
    * [ run_step  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext.run_step)
  * [ ToolParams  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams)
  * [ SystemPromptFunc  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.SystemPromptFunc)
  * [ ToolFuncContext  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext)
  * [ ToolFuncPlain  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain)
  * [ ToolFuncEither  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither)
  * [ ToolPrepareFunc  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc)
  * [ DocstringFormat  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat)
  * [ Tool  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool)
    * [ __init__  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.__init__)
    * [ prepare_tool_def  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.prepare_tool_def)
    * [ run  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.Tool.run)
  * [ ObjectJsonSchema  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ObjectJsonSchema)
  * [ ToolDefinition  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition)
    * [ name  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.name)
    * [ description  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.description)
    * [ parameters_json_schema  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.parameters_json_schema)
    * [ outer_typed_dict_key  ](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition.outer_typed_dict_key)


# `pydantic_ai.tools`
###  AgentDepsT `module-attribute`
```
AgentDepsT = TypeVar(
  "AgentDepsT", default=None, contravariant=True
)

```

Type variable for agent dependencies.
###  RunContext `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")]`
Information about the current call.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
```
| ```
@dataclasses.dataclass
classRunContext(Generic[AgentDepsT]):
"""Information about the current call."""
  deps: AgentDepsT
"""Dependencies for the agent."""
  model: models.Model
"""The model used in this run."""
  usage: Usage
"""LLM usage associated with the run."""
  prompt: str | Sequence[_messages.UserContent]
"""The original user prompt passed to the run."""
  messages: list[_messages.ModelMessage] = field(default_factory=list)
"""Messages exchanged in the conversation so far."""
  tool_call_id: str | None = None
"""The ID of the tool call."""
  tool_name: str | None = None
"""Name of the tool being called."""
  retry: int = 0
"""Number of retries so far."""
  run_step: int = 0
"""The current step in the run."""
  defreplace_with(
    self, retry: int | None = None, tool_name: str | None | _utils.Unset = _utils.UNSET
  ) -> RunContext[AgentDepsT]:
    # Create a new `RunContext` a new `retry` value and `tool_name`.
    kwargs = {}
    if retry is not None:
      kwargs['retry'] = retry
    if tool_name is not _utils.UNSET:
      kwargs['tool_name'] = tool_name
    return dataclasses.replace(self, **kwargs)

```
  
---|---  
####  deps `instance-attribute`
```
deps: AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")

```

Dependencies for the agent.
####  model `instance-attribute`
```
model: Model[](https://ai.pydantic.dev/api/models/base/#pydantic_ai.models.Model "pydantic_ai.models.Model")

```

The model used in this run.
####  usage `instance-attribute`
```
usage: Usage[](https://ai.pydantic.dev/api/usage/#pydantic_ai.usage.Usage "pydantic_ai.result.Usage")

```

LLM usage associated with the run.
####  prompt `instance-attribute`
```
prompt: str[](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[UserContent]

```

The original user prompt passed to the run.
####  messages `class-attribute` `instance-attribute`
```
messages: list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "pydantic_ai.messages.ModelMessage")] = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=list[](https://docs.python.org/3/library/stdtypes.html#list))

```

Messages exchanged in the conversation so far.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The ID of the tool call.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Name of the tool being called.
####  retry `class-attribute` `instance-attribute`
```
retry: int[](https://docs.python.org/3/library/functions.html#int) = 0

```

Number of retries so far.
####  run_step `class-attribute` `instance-attribute`
```
run_step: int[](https://docs.python.org/3/library/functions.html#int) = 0

```

The current step in the run.
###  ToolParams `module-attribute`
```
ToolParams = ParamSpec[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.ParamSpec "typing_extensions.ParamSpec")('ToolParams', default=...)

```

Retrieval function param spec.
###  SystemPromptFunc `module-attribute`
```
SystemPromptFunc = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "pydantic_ai.tools.RunContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")]], str[](https://docs.python.org/3/library/stdtypes.html#str)],
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "pydantic_ai.tools.RunContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")]], Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[str[](https://docs.python.org/3/library/stdtypes.html#str)]],
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], str[](https://docs.python.org/3/library/stdtypes.html#str)],
  Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[[], Awaitable[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable")[str[](https://docs.python.org/3/library/stdtypes.html#str)]],
]

```

A function that may or maybe not take `RunContext` as an argument, and may or may not be async.
Usage `SystemPromptFunc[AgentDepsT]`.
###  ToolFuncContext `module-attribute`
```
ToolFuncContext = Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[
  Concatenate[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Concatenate "typing_extensions.Concatenate")[RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "pydantic_ai.tools.RunContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")], ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "pydantic_ai.tools.ToolParams")], Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")
]

```

A tool function that takes `RunContext` as the first argument.
Usage `ToolContextFunc[AgentDepsT, ToolParams]`.
###  ToolFuncPlain `module-attribute`
```
ToolFuncPlain = Callable[](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "pydantic_ai.tools.ToolParams"), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

A tool function that does not take `RunContext` as the first argument.
Usage `ToolPlainFunc[ToolParams]`.
###  ToolFuncEither `module-attribute`
```
ToolFuncEither = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
  ToolFuncContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext "pydantic_ai.tools.ToolFuncContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT"), ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "pydantic_ai.tools.ToolParams")],
  ToolFuncPlain[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain "pydantic_ai.tools.ToolFuncPlain")[ToolParams[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolParams "pydantic_ai.tools.ToolParams")],
]

```

Either kind of tool function.
This is just a union of [`ToolFuncContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncContext) and [`ToolFuncPlain`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncPlain).
Usage `ToolFuncEither[AgentDepsT, ToolParams]`.
###  ToolPrepareFunc `module-attribute`
```
ToolPrepareFunc: TypeAlias[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias "typing_extensions.TypeAlias") = (
  "Callable[[RunContext[AgentDepsT], ToolDefinition], Awaitable[ToolDefinition | None]]"
)

```

Definition of a function that can prepare a tool definition at call time.
See [tool docs](https://ai.pydantic.dev/tools/#tool-prepare) for more information.
Example — here `only_if_42` is valid as a `ToolPrepareFunc`:
```
fromtypingimport Union
frompydantic_aiimport RunContext, Tool
frompydantic_ai.toolsimport ToolDefinition
async defonly_if_42(
  ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
  if ctx.deps == 42:
    return tool_def
defhitchhiker(ctx: RunContext[int], answer: str) -> str:
  return f'{ctx.deps}{answer}'
hitchhiker = Tool(hitchhiker, prepare=only_if_42)

```

Usage `ToolPrepareFunc[AgentDepsT]`.
###  DocstringFormat `module-attribute`
```
DocstringFormat = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
  "google", "numpy", "sphinx", "auto"
]

```

Supported docstring formats.
  * `'google'` — [Google-style](https://google.github.io/styleguide/pyguide.html#381-docstrings) docstrings.
  * `'numpy'` — [Numpy-style](https://numpydoc.readthedocs.io/en/latest/format.html) docstrings.
  * `'sphinx'` — [Sphinx-style](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format) docstrings.
  * `'auto'` — Automatically infer the format based on the structure of the docstring.


###  Tool `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")]`
A tool function for an agent.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
```
| ```
@dataclass(init=False)
classTool(Generic[AgentDepsT]):
"""A tool function for an agent."""
  function: ToolFuncEither[AgentDepsT]
  takes_ctx: bool
  max_retries: int | None
  name: str
  description: str
  prepare: ToolPrepareFunc[AgentDepsT] | None
  docstring_format: DocstringFormat
  require_parameter_descriptions: bool
  _is_async: bool = field(init=False)
  _single_arg_name: str | None = field(init=False)
  _positional_fields: list[str] = field(init=False)
  _var_positional_field: str | None = field(init=False)
  _validator: SchemaValidator = field(init=False, repr=False)
  _parameters_json_schema: ObjectJsonSchema = field(init=False)
  # TODO: Move this state off the Tool class, which is otherwise stateless.
  #  This should be tracked inside a specific agent run, not the tool.
  current_retry: int = field(default=0, init=False)
  def__init__(
    self,
    function: ToolFuncEither[AgentDepsT],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[AgentDepsT] | None = None,
    docstring_format: DocstringFormat = 'auto',
    require_parameter_descriptions: bool = False,
  ):
"""Create a new tool instance.
    Example usage:
```python {noqa="I001"}
    from pydantic_ai import Agent, RunContext, Tool
    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
      return f'{ctx.deps} {x} {y}'
    agent = Agent('test', tools=[Tool(my_tool)])
```
    or with a custom prepare method:
```python {noqa="I001"}
    from typing import Union
    from pydantic_ai import Agent, RunContext, Tool
    from pydantic_ai.tools import ToolDefinition
    async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
      return f'{ctx.deps} {x} {y}'
    async def prep_my_tool(
      ctx: RunContext[int], tool_def: ToolDefinition
    ) -> Union[ToolDefinition, None]:
      # only register the tool if `deps == 42`
      if ctx.deps == 42:
        return tool_def
    agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
```

    Args:
      function: The Python function to call as the tool.
      takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
        this is inferred if unset.
      max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
      name: Name of the tool, inferred from the function if `None`.
      description: Description of the tool, inferred from the function if `None`.
      prepare: custom method to prepare the tool definition for each step, return `None` to omit this
        tool from a given step. This is useful if you want to customise a tool at call time,
        or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
      docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
        Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
      require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
    """
    if takes_ctx is None:
      takes_ctx = _pydantic.takes_ctx(function)
    f = _pydantic.function_schema(function, takes_ctx, docstring_format, require_parameter_descriptions)
    self.function = function
    self.takes_ctx = takes_ctx
    self.max_retries = max_retries
    self.name = name or function.__name__
    self.description = description or f['description']
    self.prepare = prepare
    self.docstring_format = docstring_format
    self.require_parameter_descriptions = require_parameter_descriptions
    self._is_async = inspect.iscoroutinefunction(self.function)
    self._single_arg_name = f['single_arg_name']
    self._positional_fields = f['positional_fields']
    self._var_positional_field = f['var_positional_field']
    self._validator = f['validator']
    self._parameters_json_schema = f['json_schema']
  async defprepare_tool_def(self, ctx: RunContext[AgentDepsT]) -> ToolDefinition | None:
"""Get the tool definition.
    By default, this method creates a tool definition, then either returns it, or calls `self.prepare`
    if it's set.
    Returns:
      return a `ToolDefinition` or `None` if the tools should not be registered for this run.
    """
    tool_def = ToolDefinition(
      name=self.name,
      description=self.description,
      parameters_json_schema=self._parameters_json_schema,
    )
    if self.prepare is not None:
      return await self.prepare(ctx, tool_def)
    else:
      return tool_def
  async defrun(
    self, message: _messages.ToolCallPart, run_context: RunContext[AgentDepsT]
  ) -> _messages.ToolReturnPart | _messages.RetryPromptPart:
"""Run the tool function asynchronously."""
    try:
      if isinstance(message.args, str):
        args_dict = self._validator.validate_json(message.args)
      else:
        args_dict = self._validator.validate_python(message.args)
    except ValidationError as e:
      return self._on_error(e, message)
    args, kwargs = self._call_args(args_dict, message, run_context)
    try:
      if self._is_async:
        function = cast(Callable[[Any], Awaitable[str]], self.function)
        response_content = await function(*args, **kwargs)
      else:
        function = cast(Callable[[Any], str], self.function)
        response_content = await _utils.run_in_executor(function, *args, **kwargs)
    except ModelRetry as e:
      return self._on_error(e, message)
    self.current_retry = 0
    return _messages.ToolReturnPart(
      tool_name=message.tool_name,
      content=response_content,
      tool_call_id=message.tool_call_id,
    )
  def_call_args(
    self,
    args_dict: dict[str, Any],
    message: _messages.ToolCallPart,
    run_context: RunContext[AgentDepsT],
  ) -> tuple[list[Any], dict[str, Any]]:
    if self._single_arg_name:
      args_dict = {self._single_arg_name: args_dict}
    ctx = dataclasses.replace(
      run_context,
      retry=self.current_retry,
      tool_name=message.tool_name,
      tool_call_id=message.tool_call_id,
    )
    args = [ctx] if self.takes_ctx else []
    for positional_field in self._positional_fields:
      args.append(args_dict.pop(positional_field))
    if self._var_positional_field:
      args.extend(args_dict.pop(self._var_positional_field))
    return args, args_dict
  def_on_error(
    self, exc: ValidationError | ModelRetry, call_message: _messages.ToolCallPart
  ) -> _messages.RetryPromptPart:
    self.current_retry += 1
    if self.max_retries is None or self.current_retry > self.max_retries:
      raise UnexpectedModelBehavior(f'Tool exceeded max retries count of {self.max_retries}') fromexc
    else:
      if isinstance(exc, ValidationError):
        content = exc.errors(include_url=False)
      else:
        content = exc.message
      return _messages.RetryPromptPart(
        tool_name=call_message.tool_name,
        content=content,
        tool_call_id=call_message.tool_call_id,
      )

```
  
---|---  
####  __init__
```
__init__(
  function: ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "pydantic_ai.tools.ToolFuncEither")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")],
  *,
  takes_ctx: bool[](https://docs.python.org/3/library/functions.html#bool) | None = None,
  max_retries: int[](https://docs.python.org/3/library/functions.html#int) | None = None,
  name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
  description: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None,
  prepare: ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "pydantic_ai.tools.ToolPrepareFunc")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")] | None = None,
  docstring_format: DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "pydantic_ai.tools.DocstringFormat") = "auto",
  require_parameter_descriptions: bool[](https://docs.python.org/3/library/functions.html#bool) = False
)

```

Create a new tool instance.
Example usage:
```
frompydantic_aiimport Agent, RunContext, Tool
async defmy_tool(ctx: RunContext[int], x: int, y: int) -> str:
  return f'{ctx.deps}{x}{y}'
agent = Agent('test', tools=[Tool(my_tool)])

```

or with a custom prepare method:
```
fromtypingimport Union
frompydantic_aiimport Agent, RunContext, Tool
frompydantic_ai.toolsimport ToolDefinition
async defmy_tool(ctx: RunContext[int], x: int, y: int) -> str:
  return f'{ctx.deps}{x}{y}'
async defprep_my_tool(
  ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
  # only register the tool if `deps == 42`
  if ctx.deps == 42:
    return tool_def
agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])

```

Parameters:
Name | Type | Description | Default  
---|---|---|---  
`function` |  `ToolFuncEither[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolFuncEither "pydantic_ai.tools.ToolFuncEither")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")]` |  The Python function to call as the tool. |  _required_  
`takes_ctx` |  `bool[](https://docs.python.org/3/library/functions.html#bool) | None` |  Whether the function takes a [`RunContext`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext) first argument, this is inferred if unset. |  `None`  
`max_retries` |  `int[](https://docs.python.org/3/library/functions.html#int) | None` |  Maximum number of retries allowed for this tool, set to the agent default if `None`. |  `None`  
`name` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Name of the tool, inferred from the function if `None`. |  `None`  
`description` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Description of the tool, inferred from the function if `None`. |  `None`  
`prepare` |  `ToolPrepareFunc[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc "pydantic_ai.tools.ToolPrepareFunc")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")] | None` |  custom method to prepare the tool definition for each step, return `None` to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See [`ToolPrepareFunc`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolPrepareFunc). |  `None`  
`docstring_format` |  `DocstringFormat[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat "pydantic_ai.tools.DocstringFormat")` |  The format of the docstring, see [`DocstringFormat`](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.DocstringFormat). Defaults to `'auto'`, such that the format is inferred from the structure of the docstring. |  `'auto'`  
`require_parameter_descriptions` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  If True, raise an error if a parameter description is missing. Defaults to False. |  `False`  
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
```
| ```
def__init__(
  self,
  function: ToolFuncEither[AgentDepsT],
  *,
  takes_ctx: bool | None = None,
  max_retries: int | None = None,
  name: str | None = None,
  description: str | None = None,
  prepare: ToolPrepareFunc[AgentDepsT] | None = None,
  docstring_format: DocstringFormat = 'auto',
  require_parameter_descriptions: bool = False,
):
"""Create a new tool instance.
  Example usage:
  ```python {noqa="I001"}
  from pydantic_ai import Agent, RunContext, Tool
  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'
  agent = Agent('test', tools=[Tool(my_tool)])
  ```
  or with a custom prepare method:
  ```python {noqa="I001"}
  from typing import Union
  from pydantic_ai import Agent, RunContext, Tool
  from pydantic_ai.tools import ToolDefinition
  async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'
  async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
  ) -> Union[ToolDefinition, None]:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
      return tool_def
  agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
  ```

  Args:
    function: The Python function to call as the tool.
    takes_ctx: Whether the function takes a [`RunContext`][pydantic_ai.tools.RunContext] first argument,
      this is inferred if unset.
    max_retries: Maximum number of retries allowed for this tool, set to the agent default if `None`.
    name: Name of the tool, inferred from the function if `None`.
    description: Description of the tool, inferred from the function if `None`.
    prepare: custom method to prepare the tool definition for each step, return `None` to omit this
      tool from a given step. This is useful if you want to customise a tool at call time,
      or omit it completely from a step. See [`ToolPrepareFunc`][pydantic_ai.tools.ToolPrepareFunc].
    docstring_format: The format of the docstring, see [`DocstringFormat`][pydantic_ai.tools.DocstringFormat].
      Defaults to `'auto'`, such that the format is inferred from the structure of the docstring.
    require_parameter_descriptions: If True, raise an error if a parameter description is missing. Defaults to False.
  """
  if takes_ctx is None:
    takes_ctx = _pydantic.takes_ctx(function)
  f = _pydantic.function_schema(function, takes_ctx, docstring_format, require_parameter_descriptions)
  self.function = function
  self.takes_ctx = takes_ctx
  self.max_retries = max_retries
  self.name = name or function.__name__
  self.description = description or f['description']
  self.prepare = prepare
  self.docstring_format = docstring_format
  self.require_parameter_descriptions = require_parameter_descriptions
  self._is_async = inspect.iscoroutinefunction(self.function)
  self._single_arg_name = f['single_arg_name']
  self._positional_fields = f['positional_fields']
  self._var_positional_field = f['var_positional_field']
  self._validator = f['validator']
  self._parameters_json_schema = f['json_schema']

```
  
---|---  
####  prepare_tool_def `async`
```
prepare_tool_def(
  ctx: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "pydantic_ai.tools.RunContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")],
) -> ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "pydantic_ai.tools.ToolDefinition") | None

```

Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls `self.prepare` if it's set.
Returns:
Type | Description  
---|---  
`ToolDefinition[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition "pydantic_ai.tools.ToolDefinition") | None` |  return a `ToolDefinition` or `None` if the tools should not be registered for this run.  
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
```
| ```
async defprepare_tool_def(self, ctx: RunContext[AgentDepsT]) -> ToolDefinition | None:
"""Get the tool definition.
  By default, this method creates a tool definition, then either returns it, or calls `self.prepare`
  if it's set.
  Returns:
    return a `ToolDefinition` or `None` if the tools should not be registered for this run.
  """
  tool_def = ToolDefinition(
    name=self.name,
    description=self.description,
    parameters_json_schema=self._parameters_json_schema,
  )
  if self.prepare is not None:
    return await self.prepare(ctx, tool_def)
  else:
    return tool_def

```
  
---|---  
####  run `async`
```
run(
  message: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart"),
  run_context: RunContext[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.RunContext "pydantic_ai.tools.RunContext")[AgentDepsT[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.AgentDepsT "pydantic_ai.tools.AgentDepsT")],
) -> ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "pydantic_ai.messages.ToolReturnPart") | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "pydantic_ai.messages.RetryPromptPart")

```

Run the tool function asynchronously.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
```
| ```
async defrun(
  self, message: _messages.ToolCallPart, run_context: RunContext[AgentDepsT]
) -> _messages.ToolReturnPart | _messages.RetryPromptPart:
"""Run the tool function asynchronously."""
  try:
    if isinstance(message.args, str):
      args_dict = self._validator.validate_json(message.args)
    else:
      args_dict = self._validator.validate_python(message.args)
  except ValidationError as e:
    return self._on_error(e, message)
  args, kwargs = self._call_args(args_dict, message, run_context)
  try:
    if self._is_async:
      function = cast(Callable[[Any], Awaitable[str]], self.function)
      response_content = await function(*args, **kwargs)
    else:
      function = cast(Callable[[Any], str], self.function)
      response_content = await _utils.run_in_executor(function, *args, **kwargs)
  except ModelRetry as e:
    return self._on_error(e, message)
  self.current_retry = 0
  return _messages.ToolReturnPart(
    tool_name=message.tool_name,
    content=response_content,
    tool_call_id=message.tool_call_id,
  )

```
  
---|---  
###  ObjectJsonSchema `module-attribute`
```
ObjectJsonSchema: TypeAlias[](https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAlias "typing_extensions.TypeAlias") = dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

Type representing JSON schema of an object, e.g. where `"type": "object"`.
This type is used to define tools parameters (aka arguments) in [ToolDefinition](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ToolDefinition).
With PEP-728 this should be a TypedDict with `type: Literal['object']`, and `extra_parts=Any`
###  ToolDefinition `dataclass`
Definition of a tool passed to a model.
This is used for both function tools result tools.
Source code in `pydantic_ai_slim/pydantic_ai/tools.py`
```
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
```
| ```
@dataclass
classToolDefinition:
"""Definition of a tool passed to a model.
  This is used for both function tools result tools.
  """
  name: str
"""The name of the tool."""
  description: str
"""The description of the tool."""
  parameters_json_schema: ObjectJsonSchema
"""The JSON schema for the tool's parameters."""
  outer_typed_dict_key: str | None = None
"""The key in the outer [TypedDict] that wraps a result tool.
  This will only be set for result tools which don't have an `object` JSON schema.
  """

```
  
---|---  
####  name `instance-attribute`
```
name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The name of the tool.
####  description `instance-attribute`
```
description: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The description of the tool.
####  parameters_json_schema `instance-attribute`
```
parameters_json_schema: ObjectJsonSchema[](https://ai.pydantic.dev/api/tools/#pydantic_ai.tools.ObjectJsonSchema "pydantic_ai.tools.ObjectJsonSchema")

```

The JSON schema for the tool's parameters.
####  outer_typed_dict_key `class-attribute` `instance-attribute`
```
outer_typed_dict_key: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The key in the outer [TypedDict] that wraps a result tool.
This will only be set for result tools which don't have an `object` JSON schema.
© Pydantic Services Inc. 2024 to present 
