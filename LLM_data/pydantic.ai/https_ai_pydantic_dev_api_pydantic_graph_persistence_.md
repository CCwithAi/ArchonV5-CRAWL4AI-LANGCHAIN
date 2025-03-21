[ Skip to content ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graphpersistence)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_graph.persistence 
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
    * pydantic_graph.persistence  [ pydantic_graph.persistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/) Table of contents 
      * [ persistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence)
      * [ SnapshotStatus  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.SnapshotStatus)
      * [ NodeSnapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot)
        * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.state)
        * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.node)
        * [ start_ts  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.start_ts)
        * [ duration  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.duration)
        * [ status  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.status)
        * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.kind)
        * [ id  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.id)
      * [ EndSnapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot)
        * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.state)
        * [ result  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.result)
        * [ ts  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.ts)
        * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.kind)
        * [ id  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.id)
        * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.node)
      * [ Snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot)
      * [ BaseStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence)
        * [ snapshot_node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_node)
        * [ snapshot_node_if_new  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_node_if_new)
        * [ snapshot_end  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_end)
        * [ record_run  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.record_run)
        * [ load_next  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_next)
        * [ load_all  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_all)
        * [ set_graph_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_graph_types)
        * [ should_set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.should_set_types)
        * [ set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_types)
      * [ build_snapshot_list_type_adapter  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.build_snapshot_list_type_adapter)
      * [ in_mem  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem)
      * [ SimpleStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence)
        * [ last_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence.last_snapshot)
      * [ FullStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence)
        * [ deep_copy  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.deep_copy)
        * [ history  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.history)
        * [ dump_json  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.dump_json)
        * [ load_json  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.load_json)
      * [ file  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file)
      * [ FileStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence)
        * [ json_file  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence.json_file)
        * [ should_set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence.should_set_types)
    * [ pydantic_graph.mermaid  ](https://ai.pydantic.dev/api/pydantic_graph/mermaid/)
    * [ pydantic_graph.exceptions  ](https://ai.pydantic.dev/api/pydantic_graph/exceptions/)


Table of contents 
  * [ persistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence)
  * [ SnapshotStatus  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.SnapshotStatus)
  * [ NodeSnapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot)
    * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.state)
    * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.node)
    * [ start_ts  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.start_ts)
    * [ duration  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.duration)
    * [ status  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.status)
    * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.kind)
    * [ id  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.id)
  * [ EndSnapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot)
    * [ state  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.state)
    * [ result  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.result)
    * [ ts  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.ts)
    * [ kind  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.kind)
    * [ id  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.id)
    * [ node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.node)
  * [ Snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot)
  * [ BaseStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence)
    * [ snapshot_node  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_node)
    * [ snapshot_node_if_new  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_node_if_new)
    * [ snapshot_end  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_end)
    * [ record_run  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.record_run)
    * [ load_next  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_next)
    * [ load_all  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_all)
    * [ set_graph_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_graph_types)
    * [ should_set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.should_set_types)
    * [ set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_types)
  * [ build_snapshot_list_type_adapter  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.build_snapshot_list_type_adapter)
  * [ in_mem  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem)
  * [ SimpleStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence)
    * [ last_snapshot  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.SimpleStatePersistence.last_snapshot)
  * [ FullStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence)
    * [ deep_copy  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.deep_copy)
    * [ history  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.history)
    * [ dump_json  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.dump_json)
    * [ load_json  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.in_mem.FullStatePersistence.load_json)
  * [ file  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file)
  * [ FileStatePersistence  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence)
    * [ json_file  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence.json_file)
    * [ should_set_types  ](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.file.FileStatePersistence.should_set_types)


# `pydantic_graph.persistence`
###  SnapshotStatus `module-attribute`
```
SnapshotStatus = Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")[
  "created", "pending", "running", "success", "error"
]

```

The status of a snapshot.
  * `'created'`: The snapshot has been created but not yet run.
  * `'pending'`: The snapshot has been retrieved with [`load_next`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.load_next) but not yet run.
  * `'running'`: The snapshot is currently running.
  * `'success'`: The snapshot has been run successfully.
  * `'error'`: The snapshot has been run but an error occurred.


###  NodeSnapshot `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT, RunEndT]`
History step describing the execution of a node in a graph.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
@dataclass
classNodeSnapshot(Generic[StateT, RunEndT]):
"""History step describing the execution of a node in a graph."""
  state: StateT
"""The state of the graph before the node is run."""
  node: Annotated[BaseNode[StateT, Any, RunEndT], _utils.CustomNodeSchema()]
"""The node to run next."""
  start_ts: datetime | None = None
"""The timestamp when the node started running, `None` until the run starts."""
  duration: float | None = None
"""The duration of the node run in seconds, if the node has been run."""
  status: SnapshotStatus = 'created'
"""The status of the snapshot."""
  kind: Literal['node'] = 'node'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  id: str = UNSET_SNAPSHOT_ID
"""Unique ID of the snapshot."""
  def__post_init__(self) -> None:
    if self.id == UNSET_SNAPSHOT_ID:
      self.id = self.node.get_snapshot_id()

```
  
---|---  
####  state `instance-attribute`
```
state: StateT

```

The state of the graph before the node is run.
####  node `instance-attribute`
```
node: Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT], CustomNodeSchema()
]

```

The node to run next.
####  start_ts `class-attribute` `instance-attribute`
```
start_ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") | None = None

```

The timestamp when the node started running, `None` until the run starts.
####  duration `class-attribute` `instance-attribute`
```
duration: float[](https://docs.python.org/3/library/functions.html#float) | None = None

```

The duration of the node run in seconds, if the node has been run.
####  status `class-attribute` `instance-attribute`
```
status: SnapshotStatus[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.SnapshotStatus "pydantic_graph.persistence.SnapshotStatus") = 'created'

```

The status of the snapshot.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['node'] = 'node'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) = UNSET_SNAPSHOT_ID

```

Unique ID of the snapshot.
###  EndSnapshot `dataclass`
Bases: `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT, RunEndT]`
History step describing the end of a graph run.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
```
| ```
@dataclass
classEndSnapshot(Generic[StateT, RunEndT]):
"""History step describing the end of a graph run."""
  state: StateT
"""The state of the graph at the end of the run."""
  result: End[RunEndT]
"""The result of the graph run."""
  ts: datetime = field(default_factory=_utils.now_utc)
"""The timestamp when the graph run ended."""
  kind: Literal['end'] = 'end'
"""The kind of history step, can be used as a discriminator when deserializing history."""
  id: str = UNSET_SNAPSHOT_ID
"""Unique ID of the snapshot."""
  def__post_init__(self) -> None:
    if self.id == UNSET_SNAPSHOT_ID:
      self.id = self.node.get_snapshot_id()
  @property
  defnode(self) -> End[RunEndT]:
"""Shim to get the [`result`][pydantic_graph.persistence.EndSnapshot.result].
    Useful to allow `[snapshot.node for snapshot in persistence.history]`.
    """
    return self.result

```
  
---|---  
####  state `instance-attribute`
```
state: StateT

```

The state of the graph at the end of the run.
####  result `instance-attribute`
```
result: End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT]

```

The result of the graph run.
####  ts `class-attribute` `instance-attribute`
```
ts: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp when the graph run ended.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['end'] = 'end'

```

The kind of history step, can be used as a discriminator when deserializing history.
####  id `class-attribute` `instance-attribute`
```
id: str[](https://docs.python.org/3/library/stdtypes.html#str) = UNSET_SNAPSHOT_ID

```

Unique ID of the snapshot.
####  node `property`
```
node: End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT]

```

Shim to get the [`result`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot.result).
Useful to allow `[snapshot.node for snapshot in persistence.history]`.
###  Snapshot `module-attribute`
```
Snapshot = Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
  NodeSnapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot "pydantic_graph.persistence.NodeSnapshot")[StateT, RunEndT],
  EndSnapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot "pydantic_graph.persistence.EndSnapshot")[StateT, RunEndT],
]

```

A step in the history of a graph run.
[`Graph.run`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.run) returns a list of these steps describing the execution of the graph, together with the run return value.
###  BaseStatePersistence
Bases: `ABC[](https://docs.python.org/3/library/abc.html#abc.ABC "abc.ABC")`, `Generic[](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")[StateT, RunEndT]`
Abstract base class for storing the state of a graph run.
Each instance of a `BaseStatePersistence` subclass should be used for a single graph run.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
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
```
| ```
classBaseStatePersistence(ABC, Generic[StateT, RunEndT]):
"""Abstract base class for storing the state of a graph run.
  Each instance of a `BaseStatePersistence` subclass should be used for a single graph run.
  """
  @abstractmethod
  async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
"""Snapshot the state of a graph, when the next step is to run a node.
    This method should add a [`NodeSnapshot`][pydantic_graph.persistence.NodeSnapshot] to persistence.
    Args:
      state: The state of the graph.
      next_node: The next node to run.
    """
    raise NotImplementedError
  @abstractmethod
  async defsnapshot_node_if_new(
    self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
  ) -> None:
"""Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.
    This method will generally call [`snapshot_node`][pydantic_graph.persistence.BaseStatePersistence.snapshot_node]
    but should do so in an atomic way.
    Args:
      snapshot_id: The ID of the snapshot to check.
      state: The state of the graph.
      next_node: The next node to run.
    """
    raise NotImplementedError
  @abstractmethod
  async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
"""Snapshot the state of a graph when the graph has ended.
    This method should add an [`EndSnapshot`][pydantic_graph.persistence.EndSnapshot] to persistence.
    Args:
      state: The state of the graph.
      end: data from the end of the run.
    """
    raise NotImplementedError
  @abstractmethod
  defrecord_run(self, snapshot_id: str) -> AbstractAsyncContextManager[None]:
"""Record the run of the node, or error if the node is already running.
    Args:
      snapshot_id: The ID of the snapshot to record.
    Raises:
      GraphNodeRunningError: if the node status it not `'created'` or `'pending'`.
      LookupError: if the snapshot ID is not found in persistence.
    Returns:
      An async context manager that records the run of the node.
    In particular this should set:
    - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'running'` and
     [`NodeSnapshot.start_ts`][pydantic_graph.persistence.NodeSnapshot.start_ts] when the run starts.
    - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'success'` or `'error'` and
     [`NodeSnapshot.duration`][pydantic_graph.persistence.NodeSnapshot.duration] when the run finishes.
    """
    raise NotImplementedError
  @abstractmethod
  async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
"""Retrieve a node snapshot with status `'created`' and set its status to `'pending'`.
    This is used by [`Graph.iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence]
    to get the next node to run.
    Returns: The snapshot, or `None` if no snapshot with status `'created`' exists.
    """
    raise NotImplementedError
  @abstractmethod
  async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
"""Load the entire history of snapshots.
    `load_all` is not used by pydantic-graph itself, instead it's provided to make it convenient to
    get all [snapshots][pydantic_graph.persistence.Snapshot] from persistence.
    Returns: The list of snapshots.
    """
    raise NotImplementedError
  defset_graph_types(self, graph: Graph[StateT, Any, RunEndT]) -> None:
"""Set the types of the state and run end from a graph.
    You generally won't need to customise this method, instead implement
    [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types] and
    [`should_set_types`][pydantic_graph.persistence.BaseStatePersistence.should_set_types].
    """
    if self.should_set_types():
      with _utils.set_nodes_type_context(graph.get_nodes()):
        self.set_types(*graph.inferred_types)
  defshould_set_types(self) -> bool:
"""Whether types need to be set.
    Implementations should override this method to return `True` when types have not been set if they are needed.
    """
    return False
  defset_types(self, state_type: type[StateT], run_end_type: type[RunEndT]) -> None:
"""Set the types of the state and run end.
    This can be used to create [type adapters][pydantic.TypeAdapter] for serializing and deserializing snapshots,
    e.g. with [`build_snapshot_list_type_adapter`][pydantic_graph.persistence.build_snapshot_list_type_adapter].
    Args:
      state_type: The state type.
      run_end_type: The run end type.
    """
    pass

```
  
---|---  
####  snapshot_node `abstractmethod` `async`
```
snapshot_node(
  state: StateT, next_node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT]
) -> None

```

Snapshot the state of a graph, when the next step is to run a node.
This method should add a [`NodeSnapshot`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot) to persistence.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`state` |  `StateT` |  The state of the graph. |  _required_  
`next_node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT]` |  The next node to run. |  _required_  
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
112
113
114
115
116
117
118
119
120
121
122
```
| ```
@abstractmethod
async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
"""Snapshot the state of a graph, when the next step is to run a node.
  This method should add a [`NodeSnapshot`][pydantic_graph.persistence.NodeSnapshot] to persistence.
  Args:
    state: The state of the graph.
    next_node: The next node to run.
  """
  raise NotImplementedError

```
  
---|---  
####  snapshot_node_if_new `abstractmethod` `async`
```
snapshot_node_if_new(
  snapshot_id: str[](https://docs.python.org/3/library/stdtypes.html#str),
  state: StateT,
  next_node: BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT],
) -> None

```

Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.
This method will generally call [`snapshot_node`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.snapshot_node) but should do so in an atomic way.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`snapshot_id` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  The ID of the snapshot to check. |  _required_  
`state` |  `StateT` |  The state of the graph. |  _required_  
`next_node` |  `BaseNode[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.BaseNode "pydantic_graph.nodes.BaseNode")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT]` |  The next node to run. |  _required_  
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
```
| ```
@abstractmethod
async defsnapshot_node_if_new(
  self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
) -> None:
"""Snapshot the state of a graph if the snapshot ID doesn't already exist in persistence.
  This method will generally call [`snapshot_node`][pydantic_graph.persistence.BaseStatePersistence.snapshot_node]
  but should do so in an atomic way.
  Args:
    snapshot_id: The ID of the snapshot to check.
    state: The state of the graph.
    next_node: The next node to run.
  """
  raise NotImplementedError

```
  
---|---  
####  snapshot_end `abstractmethod` `async`
```
snapshot_end(state: StateT, end: End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT]) -> None

```

Snapshot the state of a graph when the graph has ended.
This method should add an [`EndSnapshot`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.EndSnapshot) to persistence.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`state` |  `StateT` |  The state of the graph. |  _required_  
`end` |  `End[](https://ai.pydantic.dev/api/pydantic_graph/nodes/#pydantic_graph.nodes.End "pydantic_graph.nodes.End")[RunEndT]` |  data from the end of the run. |  _required_  
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
140
141
142
143
144
145
146
147
148
149
150
```
| ```
@abstractmethod
async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
"""Snapshot the state of a graph when the graph has ended.
  This method should add an [`EndSnapshot`][pydantic_graph.persistence.EndSnapshot] to persistence.
  Args:
    state: The state of the graph.
    end: data from the end of the run.
  """
  raise NotImplementedError

```
  
---|---  
####  record_run `abstractmethod`
```
record_run(
  snapshot_id: str[](https://docs.python.org/3/library/stdtypes.html#str),
) -> AbstractAsyncContextManager[](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager")[None]

```

Record the run of the node, or error if the node is already running.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`snapshot_id` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  The ID of the snapshot to record. |  _required_  
Raises:
Type | Description  
---|---  
`GraphNodeRunningError` |  if the node status it not `'created'` or `'pending'`.  
`LookupError[](https://docs.python.org/3/library/exceptions.html#LookupError)` |  if the snapshot ID is not found in persistence.  
Returns:
Type | Description  
---|---  
`AbstractAsyncContextManager[](https://docs.python.org/3/library/contextlib.html#contextlib.AbstractAsyncContextManager "contextlib.AbstractAsyncContextManager")[None]` |  An async context manager that records the run of the node.  
In particular this should set:
  * [`NodeSnapshot.status`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.status) to `'running'` and [`NodeSnapshot.start_ts`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.start_ts) when the run starts.
  * [`NodeSnapshot.status`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.status) to `'success'` or `'error'` and [`NodeSnapshot.duration`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.duration) when the run finishes.

Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
@abstractmethod
defrecord_run(self, snapshot_id: str) -> AbstractAsyncContextManager[None]:
"""Record the run of the node, or error if the node is already running.
  Args:
    snapshot_id: The ID of the snapshot to record.
  Raises:
    GraphNodeRunningError: if the node status it not `'created'` or `'pending'`.
    LookupError: if the snapshot ID is not found in persistence.
  Returns:
    An async context manager that records the run of the node.
  In particular this should set:
  - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'running'` and
   [`NodeSnapshot.start_ts`][pydantic_graph.persistence.NodeSnapshot.start_ts] when the run starts.
  - [`NodeSnapshot.status`][pydantic_graph.persistence.NodeSnapshot.status] to `'success'` or `'error'` and
   [`NodeSnapshot.duration`][pydantic_graph.persistence.NodeSnapshot.duration] when the run finishes.
  """
  raise NotImplementedError

```
  
---|---  
####  load_next `abstractmethod` `async`
```
load_next() -> NodeSnapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot "pydantic_graph.persistence.NodeSnapshot")[StateT, RunEndT] | None

```

Retrieve a node snapshot with status `'created`' and set its status to `'pending'`.
This is used by [`Graph.iter_from_persistence`](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph.iter_from_persistence) to get the next node to run.
Returns: The snapshot, or `None` if no snapshot with status `'created`' exists.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
@abstractmethod
async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
"""Retrieve a node snapshot with status `'created`' and set its status to `'pending'`.
  This is used by [`Graph.iter_from_persistence`][pydantic_graph.graph.Graph.iter_from_persistence]
  to get the next node to run.
  Returns: The snapshot, or `None` if no snapshot with status `'created`' exists.
  """
  raise NotImplementedError

```
  
---|---  
####  load_all `abstractmethod` `async`
```
load_all() -> list[](https://docs.python.org/3/library/stdtypes.html#list)[Snapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot "pydantic_graph.persistence.Snapshot")[StateT, RunEndT]]

```

Load the entire history of snapshots.
`load_all` is not used by pydantic-graph itself, instead it's provided to make it convenient to get all [snapshots](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot) from persistence.
Returns: The list of snapshots.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
@abstractmethod
async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
"""Load the entire history of snapshots.
  `load_all` is not used by pydantic-graph itself, instead it's provided to make it convenient to
  get all [snapshots][pydantic_graph.persistence.Snapshot] from persistence.
  Returns: The list of snapshots.
  """
  raise NotImplementedError

```
  
---|---  
####  set_graph_types
```
set_graph_types(graph: Graph[](https://ai.pydantic.dev/api/pydantic_graph/graph/#pydantic_graph.graph.Graph "pydantic_graph.Graph")[StateT, Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"), RunEndT]) -> None

```

Set the types of the state and run end from a graph.
You generally won't need to customise this method, instead implement [`set_types`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_types) and [`should_set_types`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.should_set_types).
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
defset_graph_types(self, graph: Graph[StateT, Any, RunEndT]) -> None:
"""Set the types of the state and run end from a graph.
  You generally won't need to customise this method, instead implement
  [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types] and
  [`should_set_types`][pydantic_graph.persistence.BaseStatePersistence.should_set_types].
  """
  if self.should_set_types():
    with _utils.set_nodes_type_context(graph.get_nodes()):
      self.set_types(*graph.inferred_types)

```
  
---|---  
####  should_set_types
```
should_set_types() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Whether types need to be set.
Implementations should override this method to return `True` when types have not been set if they are needed.
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
208
209
210
211
212
213
```
| ```
defshould_set_types(self) -> bool:
"""Whether types need to be set.
  Implementations should override this method to return `True` when types have not been set if they are needed.
  """
  return False

```
  
---|---  
####  set_types
```
set_types(
  state_type: type[](https://docs.python.org/3/library/functions.html#type)[StateT], run_end_type: type[](https://docs.python.org/3/library/functions.html#type)[RunEndT]
) -> None

```

Set the types of the state and run end.
This can be used to create [type adapters](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) for serializing and deserializing snapshots, e.g. with [`build_snapshot_list_type_adapter`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.build_snapshot_list_type_adapter).
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`state_type` |  `type[](https://docs.python.org/3/library/functions.html#type)[StateT]` |  The state type. |  _required_  
`run_end_type` |  `type[](https://docs.python.org/3/library/functions.html#type)[RunEndT]` |  The run end type. |  _required_  
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
defset_types(self, state_type: type[StateT], run_end_type: type[RunEndT]) -> None:
"""Set the types of the state and run end.
  This can be used to create [type adapters][pydantic.TypeAdapter] for serializing and deserializing snapshots,
  e.g. with [`build_snapshot_list_type_adapter`][pydantic_graph.persistence.build_snapshot_list_type_adapter].
  Args:
    state_type: The state type.
    run_end_type: The run end type.
  """
  pass

```
  
---|---  
###  build_snapshot_list_type_adapter
```
build_snapshot_list_type_adapter(
  state_t: type[](https://docs.python.org/3/library/functions.html#type)[StateT], run_end_t: type[](https://docs.python.org/3/library/functions.html#type)[RunEndT]
) -> TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.TypeAdapter")[list[](https://docs.python.org/3/library/stdtypes.html#list)[Snapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot "pydantic_graph.persistence.Snapshot")[StateT, RunEndT]]]

```

Build a type adapter for a list of snapshots.
This method should be called from within [`set_types`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence.set_types) where context variables will be set such that Pydantic can create a schema for [`NodeSnapshot.node`](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.NodeSnapshot.node).
Source code in `pydantic_graph/pydantic_graph/persistence/__init__.py`
```
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
```
| ```
defbuild_snapshot_list_type_adapter(
  state_t: type[StateT], run_end_t: type[RunEndT]
) -> pydantic.TypeAdapter[list[Snapshot[StateT, RunEndT]]]:
"""Build a type adapter for a list of snapshots.
  This method should be called from within
  [`set_types`][pydantic_graph.persistence.BaseStatePersistence.set_types]
  where context variables will be set such that Pydantic can create a schema for
  [`NodeSnapshot.node`][pydantic_graph.persistence.NodeSnapshot.node].
  """
  return pydantic.TypeAdapter(list[Annotated[Snapshot[state_t, run_end_t], pydantic.Discriminator('kind')]])

```
  
---|---  
In memory state persistence.
This module provides simple in memory state persistence for graphs.
###  SimpleStatePersistence `dataclass`
Bases: `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "pydantic_graph.persistence.BaseStatePersistence")[StateT, RunEndT]`
Simple in memory state persistence that just hold the latest snapshot.
If no state persistence implementation is provided when running a graph, this is used by default.
Source code in `pydantic_graph/pydantic_graph/persistence/in_mem.py`
```
31
32
33
34
35
36
37
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
71
72
73
74
75
76
77
78
79
80
81
82
```
| ```
@dataclass
classSimpleStatePersistence(BaseStatePersistence[StateT, RunEndT]):
"""Simple in memory state persistence that just hold the latest snapshot.
  If no state persistence implementation is provided when running a graph, this is used by default.
  """
  last_snapshot: Snapshot[StateT, RunEndT] | None = None
"""The last snapshot."""
  async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
    self.last_snapshot = NodeSnapshot(state=state, node=next_node)
  async defsnapshot_node_if_new(
    self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
  ) -> None:
    if self.last_snapshot and self.last_snapshot.id == snapshot_id:
      return
    else:
      await self.snapshot_node(state, next_node)
  async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
    self.last_snapshot = EndSnapshot(state=state, result=end)
  @asynccontextmanager
  async defrecord_run(self, snapshot_id: str) -> AsyncIterator[None]:
    if self.last_snapshot is None or snapshot_id != self.last_snapshot.id:
      raise LookupError(f'No snapshot found with id={snapshot_id!r}')
    assert isinstance(self.last_snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
    exceptions.GraphNodeStatusError.check(self.last_snapshot.status)
    self.last_snapshot.status = 'running'
    self.last_snapshot.start_ts = _utils.now_utc()
    start = perf_counter()
    try:
      yield
    except Exception:
      self.last_snapshot.duration = perf_counter() - start
      self.last_snapshot.status = 'error'
      raise
    else:
      self.last_snapshot.duration = perf_counter() - start
      self.last_snapshot.status = 'success'
  async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
    if isinstance(self.last_snapshot, NodeSnapshot) and self.last_snapshot.status == 'created':
      self.last_snapshot.status = 'pending'
      return self.last_snapshot
  async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
    raise NotImplementedError('load is not supported for SimpleStatePersistence')

```
  
---|---  
####  last_snapshot `class-attribute` `instance-attribute`
```
last_snapshot: Snapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot "pydantic_graph.persistence.Snapshot")[StateT, RunEndT] | None = None

```

The last snapshot.
###  FullStatePersistence `dataclass`
Bases: `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "pydantic_graph.persistence.BaseStatePersistence")[StateT, RunEndT]`
In memory state persistence that hold a list of snapshots.
Source code in `pydantic_graph/pydantic_graph/persistence/in_mem.py`
```
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
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
```
| ```
@dataclass
classFullStatePersistence(BaseStatePersistence[StateT, RunEndT]):
"""In memory state persistence that hold a list of snapshots."""
  deep_copy: bool = True
"""Whether to deep copy the state and nodes when storing them.
  Defaults to `True` so even if nodes or state are modified after the snapshot is taken,
  the persistence history will record the value at the time of the snapshot.
  """
  history: list[Snapshot[StateT, RunEndT]] = field(default_factory=list)
"""List of snapshots taken during the graph run."""
  _snapshots_type_adapter: pydantic.TypeAdapter[list[Snapshot[StateT, RunEndT]]] | None = field(
    default=None, init=False, repr=False
  )
  async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
    snapshot = NodeSnapshot(
      state=self._prep_state(state),
      node=next_node.deep_copy() if self.deep_copy else next_node,
    )
    self.history.append(snapshot)
  async defsnapshot_node_if_new(
    self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
  ) -> None:
    if not any(s.id == snapshot_id for s in self.history):
      await self.snapshot_node(state, next_node)
  async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
    snapshot = EndSnapshot(
      state=self._prep_state(state),
      result=end.deep_copy_data() if self.deep_copy else end,
    )
    self.history.append(snapshot)
  @asynccontextmanager
  async defrecord_run(self, snapshot_id: str) -> AsyncIterator[None]:
    try:
      snapshot = next(s for s in self.history if s.id == snapshot_id)
    except StopIteration as e:
      raise LookupError(f'No snapshot found with id={snapshot_id!r}') frome
    assert isinstance(snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
    exceptions.GraphNodeStatusError.check(snapshot.status)
    snapshot.status = 'running'
    snapshot.start_ts = _utils.now_utc()
    start = perf_counter()
    try:
      yield
    except Exception:
      snapshot.duration = perf_counter() - start
      snapshot.status = 'error'
      raise
    else:
      snapshot.duration = perf_counter() - start
      snapshot.status = 'success'
  async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
    if snapshot := next((s for s in self.history if isinstance(s, NodeSnapshot) and s.status == 'created'), None):
      snapshot.status = 'pending'
      return snapshot
  async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
    return self.history
  defshould_set_types(self) -> bool:
    return self._snapshots_type_adapter is None
  defset_types(self, state_type: type[StateT], run_end_type: type[RunEndT]) -> None:
    self._snapshots_type_adapter = build_snapshot_list_type_adapter(state_type, run_end_type)
  defdump_json(self, *, indent: int | None = None) -> bytes:
"""Dump the history to JSON bytes."""
    assert self._snapshots_type_adapter is not None, 'type adapter must be set to use `dump_json`'
    return self._snapshots_type_adapter.dump_json(self.history, indent=indent)
  defload_json(self, json_data: str | bytes | bytearray) -> None:
"""Load the history from JSON."""
    assert self._snapshots_type_adapter is not None, 'type adapter must be set to use `load_json`'
    self.history = self._snapshots_type_adapter.validate_json(json_data)
  def_prep_state(self, state: StateT) -> StateT:
"""Prepare state for snapshot, uses [`copy.deepcopy`][copy.deepcopy] by default."""
    if not self.deep_copy or state is None:
      return state
    else:
      return copy.deepcopy(state)

```
  
---|---  
####  deep_copy `class-attribute` `instance-attribute`
```
deep_copy: bool[](https://docs.python.org/3/library/functions.html#bool) = True

```

Whether to deep copy the state and nodes when storing them.
Defaults to `True` so even if nodes or state are modified after the snapshot is taken, the persistence history will record the value at the time of the snapshot.
####  history `class-attribute` `instance-attribute`
```
history: list[](https://docs.python.org/3/library/stdtypes.html#list)[Snapshot[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.Snapshot "pydantic_graph.persistence.Snapshot")[StateT, RunEndT]] = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(
  default_factory=list[](https://docs.python.org/3/library/stdtypes.html#list)
)

```

List of snapshots taken during the graph run.
####  dump_json
```
dump_json(*, indent: int[](https://docs.python.org/3/library/functions.html#int) | None = None) -> bytes[](https://docs.python.org/3/library/stdtypes.html#bytes)

```

Dump the history to JSON bytes.
Source code in `pydantic_graph/pydantic_graph/persistence/in_mem.py`
```
157
158
159
160
```
| ```
defdump_json(self, *, indent: int | None = None) -> bytes:
"""Dump the history to JSON bytes."""
  assert self._snapshots_type_adapter is not None, 'type adapter must be set to use `dump_json`'
  return self._snapshots_type_adapter.dump_json(self.history, indent=indent)

```
  
---|---  
####  load_json
```
load_json(json_data: str[](https://docs.python.org/3/library/stdtypes.html#str) | bytes[](https://docs.python.org/3/library/stdtypes.html#bytes) | bytearray[](https://docs.python.org/3/library/stdtypes.html#bytearray)) -> None

```

Load the history from JSON.
Source code in `pydantic_graph/pydantic_graph/persistence/in_mem.py`
```
162
163
164
165
```
| ```
defload_json(self, json_data: str | bytes | bytearray) -> None:
"""Load the history from JSON."""
  assert self._snapshots_type_adapter is not None, 'type adapter must be set to use `load_json`'
  self.history = self._snapshots_type_adapter.validate_json(json_data)

```
  
---|---  
###  FileStatePersistence `dataclass`
Bases: `BaseStatePersistence[](https://ai.pydantic.dev/api/pydantic_graph/persistence/#pydantic_graph.persistence.BaseStatePersistence "pydantic_graph.persistence.BaseStatePersistence")[StateT, RunEndT]`
File based state persistence that hold graph run state in a JSON file.
Source code in `pydantic_graph/pydantic_graph/persistence/file.py`
```
 29
 30
 31
 32
 33
 34
 35
 36
 37
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
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
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
```
| ```
@dataclass
classFileStatePersistence(BaseStatePersistence[StateT, RunEndT]):
"""File based state persistence that hold graph run state in a JSON file."""
  json_file: Path
"""Path to the JSON file where the snapshots are stored.
  You should use a different file for each graph run, but a single file should be reused for multiple
  steps of the same run.
  For example if you have a run ID of the form `run_123abc`, you might create a `FileStatePersistence` thus:
  ```py
  from pathlib import Path
  from pydantic_graph import FullStatePersistence
  run_id = 'run_123abc'
  persistence = FullStatePersistence(Path('runs') / f'{run_id}.json')
  ```
  """
  _snapshots_type_adapter: pydantic.TypeAdapter[list[Snapshot[StateT, RunEndT]]] | None = field(
    default=None, init=False, repr=False
  )
  async defsnapshot_node(self, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]) -> None:
    await self._append_save(NodeSnapshot(state=state, node=next_node))
  async defsnapshot_node_if_new(
    self, snapshot_id: str, state: StateT, next_node: BaseNode[StateT, Any, RunEndT]
  ) -> None:
    async with self._lock():
      snapshots = await self.load_all()
      if not any(s.id == snapshot_id for s in snapshots):
        await self._append_save(NodeSnapshot(state=state, node=next_node), lock=False)
  async defsnapshot_end(self, state: StateT, end: End[RunEndT]) -> None:
    await self._append_save(EndSnapshot(state=state, result=end))
  @asynccontextmanager
  async defrecord_run(self, snapshot_id: str) -> AsyncIterator[None]:
    async with self._lock():
      snapshots = await self.load_all()
      try:
        snapshot = next(s for s in snapshots if s.id == snapshot_id)
      except StopIteration as e:
        raise LookupError(f'No snapshot found with id={snapshot_id!r}') frome
      assert isinstance(snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
      exceptions.GraphNodeStatusError.check(snapshot.status)
      snapshot.status = 'running'
      snapshot.start_ts = _utils.now_utc()
      await self._save(snapshots)
    start = perf_counter()
    try:
      yield
    except Exception:
      duration = perf_counter() - start
      async with self._lock():
        await _graph_utils.run_in_executor(self._after_run_sync, snapshot_id, duration, 'error')
      raise
    else:
      snapshot.duration = perf_counter() - start
      async with self._lock():
        await _graph_utils.run_in_executor(self._after_run_sync, snapshot_id, snapshot.duration, 'success')
  async defload_next(self) -> NodeSnapshot[StateT, RunEndT] | None:
    async with self._lock():
      snapshots = await self.load_all()
      if snapshot := next((s for s in snapshots if isinstance(s, NodeSnapshot) and s.status == 'created'), None):
        snapshot.status = 'pending'
        await self._save(snapshots)
        return snapshot
  defshould_set_types(self) -> bool:
"""Whether types need to be set."""
    return self._snapshots_type_adapter is None
  defset_types(self, state_type: type[StateT], run_end_type: type[RunEndT]) -> None:
    self._snapshots_type_adapter = build_snapshot_list_type_adapter(state_type, run_end_type)
  async defload_all(self) -> list[Snapshot[StateT, RunEndT]]:
    return await _graph_utils.run_in_executor(self._load_sync)
  def_load_sync(self) -> list[Snapshot[StateT, RunEndT]]:
    assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
    try:
      content = self.json_file.read_bytes()
    except FileNotFoundError:
      return []
    else:
      return self._snapshots_type_adapter.validate_json(content)
  def_after_run_sync(self, snapshot_id: str, duration: float, status: SnapshotStatus) -> None:
    snapshots = self._load_sync()
    snapshot = next(s for s in snapshots if s.id == snapshot_id)
    assert isinstance(snapshot, NodeSnapshot), 'Only NodeSnapshot can be recorded'
    snapshot.duration = duration
    snapshot.status = status
    self._save_sync(snapshots)
  async def_save(self, snapshots: list[Snapshot[StateT, RunEndT]]) -> None:
    await _graph_utils.run_in_executor(self._save_sync, snapshots)
  def_save_sync(self, snapshots: list[Snapshot[StateT, RunEndT]]) -> None:
    assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
    self.json_file.write_bytes(self._snapshots_type_adapter.dump_json(snapshots, indent=2))
  async def_append_save(self, snapshot: Snapshot[StateT, RunEndT], *, lock: bool = True) -> None:
    assert self._snapshots_type_adapter is not None, 'snapshots type adapter must be set'
    async with AsyncExitStack() as stack:
      if lock:
        await stack.enter_async_context(self._lock())
      snapshots = await self.load_all()
      snapshots.append(snapshot)
      await self._save(snapshots)
  @asynccontextmanager
  async def_lock(self, *, timeout: float = 1.0) -> AsyncIterator[None]:
"""Lock a file by checking and writing a `.pydantic-graph-persistence-lock` to it.
    Args:
      timeout: how long to wait for the lock
    Returns: an async context manager that holds the lock
    """
    lock_file = self.json_file.parent / f'{self.json_file.name}.pydantic-graph-persistence-lock'
    lock_id = secrets.token_urlsafe().encode()
    await asyncio.wait_for(_get_lock(lock_file, lock_id), timeout=timeout)
    try:
      yield
    finally:
      await _graph_utils.run_in_executor(lock_file.unlink, missing_ok=True)

```
  
---|---  
####  json_file `instance-attribute`
```
json_file: Path[](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path")

```

Path to the JSON file where the snapshots are stored.
You should use a different file for each graph run, but a single file should be reused for multiple steps of the same run.
For example if you have a run ID of the form `run_123abc`, you might create a `FileStatePersistence` thus:
```
frompathlibimport Path
frompydantic_graphimport FullStatePersistence
run_id = 'run_123abc'
persistence = FullStatePersistence(Path('runs') / f'{run_id}.json')

```

####  should_set_types
```
should_set_types() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Whether types need to be set.
Source code in `pydantic_graph/pydantic_graph/persistence/file.py`
```
104
105
106
```
| ```
defshould_set_types(self) -> bool:
"""Whether types need to be set."""
  return self._snapshots_type_adapter is None

```
  
---|---  
© Pydantic Services Inc. 2024 to present 
