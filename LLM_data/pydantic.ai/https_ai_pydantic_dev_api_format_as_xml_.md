[ Skip to content ](https://ai.pydantic.dev/api/format_as_xml/#pydantic_aiformat_as_xml)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_ai.format_as_xml 
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
    * pydantic_ai.format_as_xml  [ pydantic_ai.format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/) Table of contents 
      * [ format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/#pydantic_ai.format_as_xml)
      * [ format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/#pydantic_ai.format_as_xml.format_as_xml)
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
  * [ format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/#pydantic_ai.format_as_xml)
  * [ format_as_xml  ](https://ai.pydantic.dev/api/format_as_xml/#pydantic_ai.format_as_xml.format_as_xml)


# `pydantic_ai.format_as_xml`
###  format_as_xml
```
format_as_xml(
  obj: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any"),
  root_tag: str[](https://docs.python.org/3/library/stdtypes.html#str) = "examples",
  item_tag: str[](https://docs.python.org/3/library/stdtypes.html#str) = "example",
  include_root_tag: bool[](https://docs.python.org/3/library/functions.html#bool) = True,
  none_str: str[](https://docs.python.org/3/library/stdtypes.html#str) = "null",
  indent: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = " ",
) -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Format a Python object as XML.
This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML, rather than JSON etc.
Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `Mapping`, `Iterable`, `dataclass`, and `BaseModel`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`obj` |  `Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")` |  Python Object to serialize to XML. |  _required_  
`root_tag` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  Outer tag to wrap the XML in, use `None` to omit the outer tag. |  `'examples'`  
`item_tag` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  Tag to use for each item in an iterable (e.g. list), this is overridden by the class name for dataclasses and Pydantic models. |  `'example'`  
`include_root_tag` |  `bool[](https://docs.python.org/3/library/functions.html#bool)` |  Whether to include the root tag in the output (The root tag is always included if it includes a body - e.g. when the input is a simple value). |  `True`  
`none_str` |  `str[](https://docs.python.org/3/library/stdtypes.html#str)` |  String to use for `None` values. |  `'null'`  
`indent` |  `str[](https://docs.python.org/3/library/stdtypes.html#str) | None` |  Indentation string to use for pretty printing. |  `' '`  
Returns:
Type | Description  
---|---  
`str[](https://docs.python.org/3/library/stdtypes.html#str)` |  XML representation of the object.  
Example: 
format_as_xml_example.py```
frompydantic_ai.format_as_xmlimport format_as_xml
print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
'''
<user>
 <name>John</name>
 <height>6</height>
 <weight>200</weight>
</user>
'''

```

Source code in `pydantic_ai_slim/pydantic_ai/format_as_xml.py`
```
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
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
```
| ```
defformat_as_xml(
  obj: Any,
  root_tag: str = 'examples',
  item_tag: str = 'example',
  include_root_tag: bool = True,
  none_str: str = 'null',
  indent: str | None = ' ',
) -> str:
"""Format a Python object as XML.
  This is useful since LLMs often find it easier to read semi-structured data (e.g. examples) as XML,
  rather than JSON etc.
  Supports: `str`, `bytes`, `bytearray`, `bool`, `int`, `float`, `date`, `datetime`, `Mapping`,
  `Iterable`, `dataclass`, and `BaseModel`.
  Args:
    obj: Python Object to serialize to XML.
    root_tag: Outer tag to wrap the XML in, use `None` to omit the outer tag.
    item_tag: Tag to use for each item in an iterable (e.g. list), this is overridden by the class name
      for dataclasses and Pydantic models.
    include_root_tag: Whether to include the root tag in the output
      (The root tag is always included if it includes a body - e.g. when the input is a simple value).
    none_str: String to use for `None` values.
    indent: Indentation string to use for pretty printing.
  Returns:
    XML representation of the object.
  Example:
  ```python {title="format_as_xml_example.py" lint="skip"}
  from pydantic_ai.format_as_xml import format_as_xml
  print(format_as_xml({'name': 'John', 'height': 6, 'weight': 200}, root_tag='user'))
  '''
  <user>
   <name>John</name>
   <height>6</height>
   <weight>200</weight>
  </user>
  '''
  ```
  """
  el = _ToXml(item_tag=item_tag, none_str=none_str).to_xml(obj, root_tag)
  if not include_root_tag and el.text is None:
    join = '' if indent is None else '\n'
    return join.join(_rootless_xml_elements(el, indent))
  else:
    if indent is not None:
      ElementTree.indent(el, space=indent)
    return ElementTree.tostring(el, encoding='unicode')

```
  
---|---  
© Pydantic Services Inc. 2024 to present 
