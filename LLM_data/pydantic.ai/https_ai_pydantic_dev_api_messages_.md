[ Skip to content ](https://ai.pydantic.dev/api/messages/#pydantic_aimessages)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
pydantic_ai.messages 
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
    * pydantic_ai.messages  [ pydantic_ai.messages  ](https://ai.pydantic.dev/api/messages/) Table of contents 
      * [ messages  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages)
      * [ SystemPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart)
        * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.content)
        * [ dynamic_ref  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.part_kind)
      * [ AudioUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl)
        * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.url)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.kind)
        * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.media_type)
      * [ ImageUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl)
        * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.url)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.kind)
        * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.media_type)
        * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.format)
      * [ DocumentUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl)
        * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.url)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.kind)
        * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.media_type)
        * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.format)
      * [ BinaryContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent)
        * [ data  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data)
        * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.media_type)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.kind)
        * [ is_audio  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_audio)
        * [ is_image  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_image)
        * [ is_document  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_document)
        * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.format)
      * [ UserPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart)
        * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.content)
        * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.timestamp)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.part_kind)
      * [ ToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart)
        * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.tool_name)
        * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.content)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.tool_call_id)
        * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.timestamp)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.part_kind)
        * [ model_response_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.model_response_str)
        * [ model_response_object  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.model_response_object)
      * [ RetryPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart)
        * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.content)
        * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_name)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_call_id)
        * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.timestamp)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.part_kind)
        * [ model_response  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.model_response)
      * [ ModelRequestPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart)
      * [ ModelRequest  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest)
        * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.parts)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.kind)
      * [ TextPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart)
        * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.content)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.part_kind)
        * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.has_content)
      * [ ToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart)
        * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.tool_name)
        * [ args  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.tool_call_id)
        * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.part_kind)
        * [ args_as_dict  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args_as_dict)
        * [ args_as_json_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args_as_json_str)
        * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.has_content)
      * [ ModelResponsePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart)
      * [ ModelResponse  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse)
        * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.parts)
        * [ model_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.model_name)
        * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.timestamp)
        * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.kind)
        * [ otel_events  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.otel_events)
      * [ ModelMessage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage)
      * [ ModelMessagesTypeAdapter  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessagesTypeAdapter)
      * [ TextPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta)
        * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.content_delta)
        * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.part_delta_kind)
        * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.apply)
      * [ ToolCallPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta)
        * [ tool_name_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta)
        * [ args_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.args_delta)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_call_id)
        * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind)
        * [ as_part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.as_part)
        * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.apply)
      * [ ModelResponsePartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta)
      * [ PartStartEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent)
        * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.index)
        * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.part)
        * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.event_kind)
      * [ PartDeltaEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent)
        * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.index)
        * [ delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.delta)
        * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.event_kind)
      * [ FinalResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent)
        * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_name)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_call_id)
        * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.event_kind)
      * [ ModelResponseStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent)
      * [ AgentStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent)
      * [ FunctionToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent)
        * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.part)
        * [ call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.call_id)
        * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.event_kind)
      * [ FunctionToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent)
        * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.result)
        * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id)
        * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.event_kind)
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
  * [ messages  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages)
  * [ SystemPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.content)
    * [ dynamic_ref  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.dynamic_ref)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart.part_kind)
  * [ AudioUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.kind)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AudioUrl.media_type)
  * [ ImageUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.kind)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.media_type)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ImageUrl.format)
  * [ DocumentUrl  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl)
    * [ url  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.url)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.kind)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.media_type)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.DocumentUrl.format)
  * [ BinaryContent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent)
    * [ data  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.data)
    * [ media_type  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.media_type)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.kind)
    * [ is_audio  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_audio)
    * [ is_image  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_image)
    * [ is_document  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.is_document)
    * [ format  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.BinaryContent.format)
  * [ UserPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.content)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.timestamp)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart.part_kind)
  * [ ToolReturnPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.tool_name)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.content)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.tool_call_id)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.timestamp)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.part_kind)
    * [ model_response_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.model_response_str)
    * [ model_response_object  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart.model_response_object)
  * [ RetryPromptPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.content)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_name)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.tool_call_id)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.timestamp)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.part_kind)
    * [ model_response  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart.model_response)
  * [ ModelRequestPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart)
  * [ ModelRequest  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest)
    * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.parts)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest.kind)
  * [ TextPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart)
    * [ content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.content)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.part_kind)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart.has_content)
  * [ ToolCallPart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.tool_name)
    * [ args  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.tool_call_id)
    * [ part_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.part_kind)
    * [ args_as_dict  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args_as_dict)
    * [ args_as_json_str  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.args_as_json_str)
    * [ has_content  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart.has_content)
  * [ ModelResponsePart  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart)
  * [ ModelResponse  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse)
    * [ parts  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.parts)
    * [ model_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.model_name)
    * [ timestamp  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.timestamp)
    * [ kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.kind)
    * [ otel_events  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse.otel_events)
  * [ ModelMessage  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage)
  * [ ModelMessagesTypeAdapter  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessagesTypeAdapter)
  * [ TextPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta)
    * [ content_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.content_delta)
    * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.part_delta_kind)
    * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta.apply)
  * [ ToolCallPartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta)
    * [ tool_name_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_name_delta)
    * [ args_delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.args_delta)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.tool_call_id)
    * [ part_delta_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.part_delta_kind)
    * [ as_part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.as_part)
    * [ apply  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta.apply)
  * [ ModelResponsePartDelta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta)
  * [ PartStartEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent)
    * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.index)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.part)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent.event_kind)
  * [ PartDeltaEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent)
    * [ index  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.index)
    * [ delta  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.delta)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent.event_kind)
  * [ FinalResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent)
    * [ tool_name  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_name)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.tool_call_id)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent.event_kind)
  * [ ModelResponseStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponseStreamEvent)
  * [ AgentStreamEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent)
  * [ FunctionToolCallEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent)
    * [ part  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.part)
    * [ call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.call_id)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolCallEvent.event_kind)
  * [ FunctionToolResultEvent  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent)
    * [ result  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.result)
    * [ tool_call_id  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.tool_call_id)
    * [ event_kind  ](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FunctionToolResultEvent.event_kind)


# `pydantic_ai.messages`
The structure of [`ModelMessage`](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage) can be shown as a graph:
###  SystemPromptPart `dataclass`
A system prompt, generally written by the application developer.
This gives the model context and guidance on how to respond.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classSystemPromptPart:
"""A system prompt, generally written by the application developer.
  This gives the model context and guidance on how to respond.
  """
  content: str
"""The content of the prompt."""
  dynamic_ref: str | None = None
"""The ref of the dynamic system prompt function that generated this part.
  Only set if system prompt is dynamic, see [`system_prompt`][pydantic_ai.Agent.system_prompt] for more information.
  """
  part_kind: Literal['system-prompt'] = 'system-prompt'
"""Part type identifier, this is available on all parts as a discriminator."""
  defotel_event(self) -> Event:
    return Event('gen_ai.system.message', body={'content': self.content, 'role': 'system'})

```
  
---|---  
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The content of the prompt.
####  dynamic_ref `class-attribute` `instance-attribute`
```
dynamic_ref: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The ref of the dynamic system prompt function that generated this part.
Only set if system prompt is dynamic, see [`system_prompt`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.system_prompt) for more information.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['system-prompt'] = 'system-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  AudioUrl `dataclass`
A URL to an audio file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classAudioUrl:
"""A URL to an audio file."""
  url: str
"""The URL of the audio file."""
  kind: Literal['audio-url'] = 'audio-url'
"""Type identifier, this is available on all parts as a discriminator."""
  @property
  defmedia_type(self) -> AudioMediaType:
"""Return the media type of the audio file, based on the url."""
    if self.url.endswith('.mp3'):
      return 'audio/mpeg'
    elif self.url.endswith('.wav'):
      return 'audio/wav'
    else:
      raise ValueError(f'Unknown audio file extension: {self.url}')

```
  
---|---  
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the audio file.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['audio-url'] = 'audio-url'

```

Type identifier, this is available on all parts as a discriminator.
####  media_type `property`
```
media_type: AudioMediaType

```

Return the media type of the audio file, based on the url.
###  ImageUrl `dataclass`
A URL to an image.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classImageUrl:
"""A URL to an image."""
  url: str
"""The URL of the image."""
  kind: Literal['image-url'] = 'image-url'
"""Type identifier, this is available on all parts as a discriminator."""
  @property
  defmedia_type(self) -> ImageMediaType:
"""Return the media type of the image, based on the url."""
    if self.url.endswith(('.jpg', '.jpeg')):
      return 'image/jpeg'
    elif self.url.endswith('.png'):
      return 'image/png'
    elif self.url.endswith('.gif'):
      return 'image/gif'
    elif self.url.endswith('.webp'):
      return 'image/webp'
    else:
      raise ValueError(f'Unknown image file extension: {self.url}')
  @property
  defformat(self) -> ImageFormat:
"""The file format of the image.
    The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
    """
    return _image_format(self.media_type)

```
  
---|---  
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the image.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['image-url'] = 'image-url'

```

Type identifier, this is available on all parts as a discriminator.
####  media_type `property`
```
media_type: ImageMediaType

```

Return the media type of the image, based on the url.
####  format `property`
```
format: ImageFormat

```

The file format of the image.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  DocumentUrl `dataclass`
The URL of the document.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classDocumentUrl:
"""The URL of the document."""
  url: str
"""The URL of the document."""
  kind: Literal['document-url'] = 'document-url'
"""Type identifier, this is available on all parts as a discriminator."""
  @property
  defmedia_type(self) -> str:
"""Return the media type of the document, based on the url."""
    type_, _ = guess_type(self.url)
    if type_ is None:
      raise RuntimeError(f'Unknown document file extension: {self.url}')
    return type_
  @property
  defformat(self) -> DocumentFormat:
"""The file format of the document.
    The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
    """
    return _document_format(self.media_type)

```
  
---|---  
####  url `instance-attribute`
```
url: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The URL of the document.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['document-url'] = 'document-url'

```

Type identifier, this is available on all parts as a discriminator.
####  media_type `property`
```
media_type: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return the media type of the document, based on the url.
####  format `property`
```
format: DocumentFormat

```

The file format of the document.
The choice of supported formats were based on the Bedrock Converse API. Other APIs don't require to use a format.
###  BinaryContent `dataclass`
Binary content, e.g. an audio or image file.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
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
```
| ```
@dataclass
classBinaryContent:
"""Binary content, e.g. an audio or image file."""
  data: bytes
"""The binary data."""
  media_type: AudioMediaType | ImageMediaType | DocumentMediaType | str
"""The media type of the binary data."""
  kind: Literal['binary'] = 'binary'
"""Type identifier, this is available on all parts as a discriminator."""
  @property
  defis_audio(self) -> bool:
"""Return `True` if the media type is an audio type."""
    return self.media_type.startswith('audio/')
  @property
  defis_image(self) -> bool:
"""Return `True` if the media type is an image type."""
    return self.media_type.startswith('image/')
  @property
  defis_document(self) -> bool:
"""Return `True` if the media type is a document type."""
    return self.media_type in {
      'application/pdf',
      'text/plain',
      'text/csv',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
      'text/html',
      'text/markdown',
      'application/vnd.ms-excel',
    }
  @property
  defformat(self) -> str:
"""The file format of the binary content."""
    if self.is_audio:
      if self.media_type == 'audio/mpeg':
        return 'mp3'
      elif self.media_type == 'audio/wav':
        return 'wav'
    elif self.is_image:
      return _image_format(self.media_type)
    elif self.is_document:
      return _document_format(self.media_type)
    raise ValueError(f'Unknown media type: {self.media_type}')

```
  
---|---  
####  data `instance-attribute`
```
data: bytes[](https://docs.python.org/3/library/stdtypes.html#bytes)

```

The binary data.
####  media_type `instance-attribute`
```
media_type: (
  AudioMediaType
  | ImageMediaType
  | DocumentMediaType
  | str[](https://docs.python.org/3/library/stdtypes.html#str)
)

```

The media type of the binary data.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['binary'] = 'binary'

```

Type identifier, this is available on all parts as a discriminator.
####  is_audio `property`
```
is_audio: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is an audio type.
####  is_image `property`
```
is_image: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is an image type.
####  is_document `property`
```
is_document: bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the media type is a document type.
####  format `property`
```
format: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The file format of the binary content.
###  UserPromptPart `dataclass`
A user prompt, generally written by the end user.
Content comes from the `user_prompt` parameter of [`Agent.run`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run), [`Agent.run_sync`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_sync), and [`Agent.run_stream`](https://ai.pydantic.dev/api/agent/#pydantic_ai.agent.Agent.run_stream).
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classUserPromptPart:
"""A user prompt, generally written by the end user.
  Content comes from the `user_prompt` parameter of [`Agent.run`][pydantic_ai.Agent.run],
  [`Agent.run_sync`][pydantic_ai.Agent.run_sync], and [`Agent.run_stream`][pydantic_ai.Agent.run_stream].
  """
  content: str | Sequence[UserContent]
"""The content of the prompt."""
  timestamp: datetime = field(default_factory=_now_utc)
"""The timestamp of the prompt."""
  part_kind: Literal['user-prompt'] = 'user-prompt'
"""Part type identifier, this is available on all parts as a discriminator."""
  defotel_event(self) -> Event:
    if isinstance(self.content, str):
      content = self.content
    else:
      # TODO figure out what to record for images and audio
      content = [part if isinstance(part, str) else {'kind': part.kind} for part in self.content]
    return Event('gen_ai.user.message', body={'content': content, 'role': 'user'})

```
  
---|---  
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str) | Sequence[](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")[UserContent]

```

The content of the prompt.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp of the prompt.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['user-prompt'] = 'user-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
###  ToolReturnPart `dataclass`
A tool return message, this encodes the result of running a tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
```
| ```
@dataclass
classToolReturnPart:
"""A tool return message, this encodes the result of running a tool."""
  tool_name: str
"""The name of the "tool" was called."""
  content: Any
"""The return value."""
  tool_call_id: str | None = None
"""Optional tool call identifier, this is used by some models including OpenAI."""
  timestamp: datetime = field(default_factory=_now_utc)
"""The timestamp, when the tool returned."""
  part_kind: Literal['tool-return'] = 'tool-return'
"""Part type identifier, this is available on all parts as a discriminator."""
  defmodel_response_str(self) -> str:
"""Return a string representation of the content for the model."""
    if isinstance(self.content, str):
      return self.content
    else:
      return tool_return_ta.dump_json(self.content).decode()
  defmodel_response_object(self) -> dict[str, Any]:
"""Return a dictionary representation of the content, wrapping non-dict types appropriately."""
    # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
    if isinstance(self.content, dict):
      return tool_return_ta.dump_python(self.content, mode='json') # pyright: ignore[reportUnknownMemberType]
    else:
      return {'return_value': tool_return_ta.dump_python(self.content, mode='json')}
  defotel_event(self) -> Event:
    return Event(
      'gen_ai.tool.message',
      body={'content': self.content, 'role': 'tool', 'id': self.tool_call_id, 'name': self.tool_name},
    )

```
  
---|---  
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The name of the "tool" was called.
####  content `instance-attribute`
```
content: Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")

```

The return value.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp, when the tool returned.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool-return'] = 'tool-return'

```

Part type identifier, this is available on all parts as a discriminator.
####  model_response_str
```
model_response_str() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return a string representation of the content for the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
277
278
279
280
281
282
```
| ```
defmodel_response_str(self) -> str:
"""Return a string representation of the content for the model."""
  if isinstance(self.content, str):
    return self.content
  else:
    return tool_return_ta.dump_json(self.content).decode()

```
  
---|---  
####  model_response_object
```
model_response_object() -> dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

Return a dictionary representation of the content, wrapping non-dict types appropriately.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
284
285
286
287
288
289
290
```
| ```
defmodel_response_object(self) -> dict[str, Any]:
"""Return a dictionary representation of the content, wrapping non-dict types appropriately."""
  # gemini supports JSON dict return values, but no other JSON types, hence we wrap anything else in a dict
  if isinstance(self.content, dict):
    return tool_return_ta.dump_python(self.content, mode='json') # pyright: ignore[reportUnknownMemberType]
  else:
    return {'return_value': tool_return_ta.dump_python(self.content, mode='json')}

```
  
---|---  
###  RetryPromptPart `dataclass`
A message back to a model asking it to try again.
This can be sent for a number of reasons:
  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * a tool raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry) exception
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError)
  * a result validator raised a [`ModelRetry`](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.ModelRetry) exception

Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
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
336
337
338
339
340
341
342
343
344
345
346
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
```
| ```
@dataclass
classRetryPromptPart:
"""A message back to a model asking it to try again.
  This can be sent for a number of reasons:
  * Pydantic validation of tool arguments failed, here content is derived from a Pydantic
   [`ValidationError`][pydantic_core.ValidationError]
  * a tool raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
  * no tool was found for the tool name
  * the model returned plain text when a structured response was expected
  * Pydantic validation of a structured response failed, here content is derived from a Pydantic
   [`ValidationError`][pydantic_core.ValidationError]
  * a result validator raised a [`ModelRetry`][pydantic_ai.exceptions.ModelRetry] exception
  """
  content: list[pydantic_core.ErrorDetails] | str
"""Details of why and how the model should retry.
  If the retry was triggered by a [`ValidationError`][pydantic_core.ValidationError], this will be a list of
  error details.
  """
  tool_name: str | None = None
"""The name of the tool that was called, if any."""
  tool_call_id: str | None = None
"""Optional tool call identifier, this is used by some models including OpenAI."""
  timestamp: datetime = field(default_factory=_now_utc)
"""The timestamp, when the retry was triggered."""
  part_kind: Literal['retry-prompt'] = 'retry-prompt'
"""Part type identifier, this is available on all parts as a discriminator."""
  defmodel_response(self) -> str:
"""Return a string message describing why the retry is requested."""
    if isinstance(self.content, str):
      description = self.content
    else:
      json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
      description = f'{len(self.content)} validation errors: {json_errors.decode()}'
    return f'{description}\n\nFix the errors and try again.'
  defotel_event(self) -> Event:
    if self.tool_name is None:
      return Event('gen_ai.user.message', body={'content': self.model_response(), 'role': 'user'})
    else:
      return Event(
        'gen_ai.tool.message',
        body={
          'content': self.model_response(),
          'role': 'tool',
          'id': self.tool_call_id,
          'name': self.tool_name,
        },
      )

```
  
---|---  
####  content `instance-attribute`
```
content: list[](https://docs.python.org/3/library/stdtypes.html#list)[ErrorDetails[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ErrorDetails "pydantic_core.ErrorDetails")] | str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Details of why and how the model should retry.
If the retry was triggered by a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError), this will be a list of error details.
####  tool_name `class-attribute` `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the tool that was called, if any.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp, when the retry was triggered.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['retry-prompt'] = 'retry-prompt'

```

Part type identifier, this is available on all parts as a discriminator.
####  model_response
```
model_response() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return a string message describing why the retry is requested.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
337
338
339
340
341
342
343
344
```
| ```
defmodel_response(self) -> str:
"""Return a string message describing why the retry is requested."""
  if isinstance(self.content, str):
    description = self.content
  else:
    json_errors = error_details_ta.dump_json(self.content, exclude={'__all__': {'ctx'}}, indent=2)
    description = f'{len(self.content)} validation errors: {json_errors.decode()}'
  return f'{description}\n\nFix the errors and try again.'

```
  
---|---  
###  ModelRequestPart `module-attribute`
```
ModelRequestPart = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[
    SystemPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.SystemPromptPart "pydantic_ai.messages.SystemPromptPart"),
    UserPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.UserPromptPart "pydantic_ai.messages.UserPromptPart"),
    ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "pydantic_ai.messages.ToolReturnPart"),
    RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "pydantic_ai.messages.RetryPromptPart"),
  ],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part sent by PydanticAI to a model.
###  ModelRequest `dataclass`
A request generated by PydanticAI and sent to a model, e.g. a message from the PydanticAI app to the model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
367
368
369
370
371
372
373
374
375
```
| ```
@dataclass
classModelRequest:
"""A request generated by PydanticAI and sent to a model, e.g. a message from the PydanticAI app to the model."""
  parts: list[ModelRequestPart]
"""The parts of the user message."""
  kind: Literal['request'] = 'request'
"""Message type identifier, this is available on all parts as a discriminator."""

```
  
---|---  
####  parts `instance-attribute`
```
parts: list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelRequestPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequestPart "pydantic_ai.messages.ModelRequestPart")]

```

The parts of the user message.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['request'] = 'request'

```

Message type identifier, this is available on all parts as a discriminator.
###  TextPart `dataclass`
A plain text response from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
378
379
380
381
382
383
384
385
386
387
388
389
390
```
| ```
@dataclass
classTextPart:
"""A plain text response from a model."""
  content: str
"""The text content of the response."""
  part_kind: Literal['text'] = 'text'
"""Part type identifier, this is available on all parts as a discriminator."""
  defhas_content(self) -> bool:
"""Return `True` if the text content is non-empty."""
    return bool(self.content)

```
  
---|---  
####  content `instance-attribute`
```
content: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The text content of the response.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['text'] = 'text'

```

Part type identifier, this is available on all parts as a discriminator.
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the text content is non-empty.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
388
389
390
```
| ```
defhas_content(self) -> bool:
"""Return `True` if the text content is non-empty."""
  return bool(self.content)

```
  
---|---  
###  ToolCallPart `dataclass`
A tool call from a model.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
```
| ```
@dataclass
classToolCallPart:
"""A tool call from a model."""
  tool_name: str
"""The name of the tool to call."""
  args: str | dict[str, Any]
"""The arguments to pass to the tool.
  This is stored either as a JSON string or a Python dictionary depending on how data was received.
  """
  tool_call_id: str | None = None
"""Optional tool call identifier, this is used by some models including OpenAI."""
  part_kind: Literal['tool-call'] = 'tool-call'
"""Part type identifier, this is available on all parts as a discriminator."""
  defargs_as_dict(self) -> dict[str, Any]:
"""Return the arguments as a Python dictionary.
    This is just for convenience with models that require dicts as input.
    """
    if isinstance(self.args, dict):
      return self.args
    args = pydantic_core.from_json(self.args)
    assert isinstance(args, dict), 'args should be a dict'
    return cast(dict[str, Any], args)
  defargs_as_json_str(self) -> str:
"""Return the arguments as a JSON string.
    This is just for convenience with models that require JSON strings as input.
    """
    if isinstance(self.args, str):
      return self.args
    return pydantic_core.to_json(self.args).decode()
  defhas_content(self) -> bool:
"""Return `True` if the arguments contain any data."""
    if isinstance(self.args, dict):
      # TODO: This should probably return True if you have the value False, or 0, etc.
      #  It makes sense to me to ignore empty strings, but not sure about empty lists or dicts
      return any(self.args.values())
    else:
      return bool(self.args)

```
  
---|---  
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The name of the tool to call.
####  args `instance-attribute`
```
args: str[](https://docs.python.org/3/library/stdtypes.html#str) | dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

The arguments to pass to the tool.
This is stored either as a JSON string or a Python dictionary depending on how data was received.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
####  part_kind `class-attribute` `instance-attribute`
```
part_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool-call'] = 'tool-call'

```

Part type identifier, this is available on all parts as a discriminator.
####  args_as_dict
```
args_as_dict() -> dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")]

```

Return the arguments as a Python dictionary.
This is just for convenience with models that require dicts as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
412
413
414
415
416
417
418
419
420
421
```
| ```
defargs_as_dict(self) -> dict[str, Any]:
"""Return the arguments as a Python dictionary.
  This is just for convenience with models that require dicts as input.
  """
  if isinstance(self.args, dict):
    return self.args
  args = pydantic_core.from_json(self.args)
  assert isinstance(args, dict), 'args should be a dict'
  return cast(dict[str, Any], args)

```
  
---|---  
####  args_as_json_str
```
args_as_json_str() -> str[](https://docs.python.org/3/library/stdtypes.html#str)

```

Return the arguments as a JSON string.
This is just for convenience with models that require JSON strings as input.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
423
424
425
426
427
428
429
430
```
| ```
defargs_as_json_str(self) -> str:
"""Return the arguments as a JSON string.
  This is just for convenience with models that require JSON strings as input.
  """
  if isinstance(self.args, str):
    return self.args
  return pydantic_core.to_json(self.args).decode()

```
  
---|---  
####  has_content
```
has_content() -> bool[](https://docs.python.org/3/library/functions.html#bool)

```

Return `True` if the arguments contain any data.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
432
433
434
435
436
437
438
439
```
| ```
defhas_content(self) -> bool:
"""Return `True` if the arguments contain any data."""
  if isinstance(self.args, dict):
    # TODO: This should probably return True if you have the value False, or 0, etc.
    #  It makes sense to me to ignore empty strings, but not sure about empty lists or dicts
    return any(self.args.values())
  else:
    return bool(self.args)

```
  
---|---  
###  ModelResponsePart `module-attribute`
```
ModelResponsePart = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "pydantic_ai.messages.TextPart"), ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart")],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_kind"),
]

```

A message part returned by a model.
###  ModelResponse `dataclass`
A response from a model, e.g. a message from the model to the PydanticAI app.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
```
| ```
@dataclass
classModelResponse:
"""A response from a model, e.g. a message from the model to the PydanticAI app."""
  parts: list[ModelResponsePart]
"""The parts of the model message."""
  model_name: str | None = None
"""The name of the model that generated the response."""
  timestamp: datetime = field(default_factory=_now_utc)
"""The timestamp of the response.
  If the model provides a timestamp in the response (as OpenAI does) that will be used.
  """
  kind: Literal['response'] = 'response'
"""Message type identifier, this is available on all parts as a discriminator."""
  defotel_events(self) -> list[Event]:
"""Return OpenTelemetry events for the response."""
    result: list[Event] = []
    defnew_event_body():
      new_body: dict[str, Any] = {'role': 'assistant'}
      ev = Event('gen_ai.assistant.message', body=new_body)
      result.append(ev)
      return new_body
    body = new_event_body()
    for part in self.parts:
      if isinstance(part, ToolCallPart):
        body.setdefault('tool_calls', []).append(
          {
            'id': part.tool_call_id,
            'type': 'function', # TODO https://github.com/pydantic/pydantic-ai/issues/888
            'function': {
              'name': part.tool_name,
              'arguments': part.args,
            },
          }
        )
      elif isinstance(part, TextPart):
        if body.get('content'):
          body = new_event_body()
        body['content'] = part.content
    return result

```
  
---|---  
####  parts `instance-attribute`
```
parts: list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart")]

```

The parts of the model message.
####  model_name `class-attribute` `instance-attribute`
```
model_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

The name of the model that generated the response.
####  timestamp `class-attribute` `instance-attribute`
```
timestamp: datetime[](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(default_factory=now_utc)

```

The timestamp of the response.
If the model provides a timestamp in the response (as OpenAI does) that will be used.
####  kind `class-attribute` `instance-attribute`
```
kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['response'] = 'response'

```

Message type identifier, this is available on all parts as a discriminator.
####  otel_events
```
otel_events() -> list[](https://docs.python.org/3/library/stdtypes.html#list)[Event]

```

Return OpenTelemetry events for the response.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
```
| ```
defotel_events(self) -> list[Event]:
"""Return OpenTelemetry events for the response."""
  result: list[Event] = []
  defnew_event_body():
    new_body: dict[str, Any] = {'role': 'assistant'}
    ev = Event('gen_ai.assistant.message', body=new_body)
    result.append(ev)
    return new_body
  body = new_event_body()
  for part in self.parts:
    if isinstance(part, ToolCallPart):
      body.setdefault('tool_calls', []).append(
        {
          'id': part.tool_call_id,
          'type': 'function', # TODO https://github.com/pydantic/pydantic-ai/issues/888
          'function': {
            'name': part.tool_name,
            'arguments': part.args,
          },
        }
      )
    elif isinstance(part, TextPart):
      if body.get('content'):
        body = new_event_body()
      body['content'] = part.content
  return result

```
  
---|---  
###  ModelMessage `module-attribute`
```
ModelMessage = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[ModelRequest[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest "pydantic_ai.messages.ModelRequest"), ModelResponse[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponse "pydantic_ai.messages.ModelResponse")],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("kind"),
]

```

Any message sent to or returned by a model.
###  ModelMessagesTypeAdapter `module-attribute`
```
ModelMessagesTypeAdapter = TypeAdapter[](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter "pydantic.TypeAdapter")(
  list[](https://docs.python.org/3/library/stdtypes.html#list)[ModelMessage[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelMessage "pydantic_ai.messages.ModelMessage")],
  config=ConfigDict[](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict "pydantic.ConfigDict")(
    defer_build=True, ser_json_bytes="base64"
  ),
)

```

Pydantic [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) for (de)serializing messages.
###  TextPartDelta `dataclass`
A partial update (delta) for a `TextPart` to append new text content.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
```
| ```
@dataclass
classTextPartDelta:
"""A partial update (delta) for a `TextPart` to append new text content."""
  content_delta: str
"""The incremental text content to add to the existing `TextPart` content."""
  part_delta_kind: Literal['text'] = 'text'
"""Part delta type identifier, used as a discriminator."""
  defapply(self, part: ModelResponsePart) -> TextPart:
"""Apply this text delta to an existing `TextPart`.
    Args:
      part: The existing model response part, which must be a `TextPart`.
    Returns:
      A new `TextPart` with updated text content.
    Raises:
      ValueError: If `part` is not a `TextPart`.
    """
    if not isinstance(part, TextPart):
      raise ValueError('Cannot apply TextPartDeltas to non-TextParts')
    return replace(part, content=part.content + self.content_delta)

```
  
---|---  
####  content_delta `instance-attribute`
```
content_delta: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

The incremental text content to add to the existing `TextPart` content.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['text'] = 'text'

```

Part delta type identifier, used as a discriminator.
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart")) -> TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "pydantic_ai.messages.TextPart")

```

Apply this text delta to an existing `TextPart`.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart")` |  The existing model response part, which must be a `TextPart`. |  _required_  
Returns:
Type | Description  
---|---  
`TextPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPart "pydantic_ai.messages.TextPart")` |  A new `TextPart` with updated text content.  
Raises:
Type | Description  
---|---  
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `part` is not a `TextPart`.  
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
```
| ```
defapply(self, part: ModelResponsePart) -> TextPart:
"""Apply this text delta to an existing `TextPart`.
  Args:
    part: The existing model response part, which must be a `TextPart`.
  Returns:
    A new `TextPart` with updated text content.
  Raises:
    ValueError: If `part` is not a `TextPart`.
  """
  if not isinstance(part, TextPart):
    raise ValueError('Cannot apply TextPartDeltas to non-TextParts')
  return replace(part, content=part.content + self.content_delta)

```
  
---|---  
###  ToolCallPartDelta `dataclass`
A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
```
| ```
@dataclass
classToolCallPartDelta:
"""A partial update (delta) for a `ToolCallPart` to modify tool name, arguments, or tool call ID."""
  tool_name_delta: str | None = None
"""Incremental text to add to the existing tool name, if any."""
  args_delta: str | dict[str, Any] | None = None
"""Incremental data to add to the tool arguments.
  If this is a string, it will be appended to existing JSON arguments.
  If this is a dict, it will be merged with existing dict arguments.
  """
  tool_call_id: str | None = None
"""Optional tool call identifier, this is used by some models including OpenAI.
  Note this is never treated as a delta — it can replace None, but otherwise if a
  non-matching value is provided an error will be raised."""
  part_delta_kind: Literal['tool_call'] = 'tool_call'
"""Part delta type identifier, used as a discriminator."""
  defas_part(self) -> ToolCallPart | None:
"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.
    Returns:
      A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.
    """
    if self.tool_name_delta is None or self.args_delta is None:
      return None
    return ToolCallPart(
      self.tool_name_delta,
      self.args_delta,
      self.tool_call_id,
    )
  @overload
  defapply(self, part: ModelResponsePart) -> ToolCallPart: ...
  @overload
  defapply(self, part: ModelResponsePart | ToolCallPartDelta) -> ToolCallPart | ToolCallPartDelta: ...
  defapply(self, part: ModelResponsePart | ToolCallPartDelta) -> ToolCallPart | ToolCallPartDelta:
"""Apply this delta to a part or delta, returning a new part or delta with the changes applied.
    Args:
      part: The existing model response part or delta to update.
    Returns:
      Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.
    Raises:
      ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.
      UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
    """
    if isinstance(part, ToolCallPart):
      return self._apply_to_part(part)
    if isinstance(part, ToolCallPartDelta):
      return self._apply_to_delta(part)
    raise ValueError(f'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas, not {part}')
  def_apply_to_delta(self, delta: ToolCallPartDelta) -> ToolCallPart | ToolCallPartDelta:
"""Internal helper to apply this delta to another delta."""
    if self.tool_name_delta:
      # Append incremental text to the existing tool_name_delta
      updated_tool_name_delta = (delta.tool_name_delta or '') + self.tool_name_delta
      delta = replace(delta, tool_name_delta=updated_tool_name_delta)
    if isinstance(self.args_delta, str):
      if isinstance(delta.args_delta, dict):
        raise UnexpectedModelBehavior(
          f'Cannot apply JSON deltas to non-JSON tool arguments ({delta=}, {self=})'
        )
      updated_args_delta = (delta.args_delta or '') + self.args_delta
      delta = replace(delta, args_delta=updated_args_delta)
    elif isinstance(self.args_delta, dict):
      if isinstance(delta.args_delta, str):
        raise UnexpectedModelBehavior(
          f'Cannot apply dict deltas to non-dict tool arguments ({delta=}, {self=})'
        )
      updated_args_delta = {**(delta.args_delta or {}), **self.args_delta}
      delta = replace(delta, args_delta=updated_args_delta)
    if self.tool_call_id:
      # Set the tool_call_id if it wasn't present, otherwise error if it has changed
      if delta.tool_call_id is not None and delta.tool_call_id != self.tool_call_id:
        raise UnexpectedModelBehavior(
          f'Cannot apply a new tool_call_id to a ToolCallPartDelta that already has one ({delta=}, {self=})'
        )
      delta = replace(delta, tool_call_id=self.tool_call_id)
    # If we now have enough data to create a full ToolCallPart, do so
    if delta.tool_name_delta is not None and delta.args_delta is not None:
      return ToolCallPart(
        delta.tool_name_delta,
        delta.args_delta,
        delta.tool_call_id,
      )
    return delta
  def_apply_to_part(self, part: ToolCallPart) -> ToolCallPart:
"""Internal helper to apply this delta directly to a `ToolCallPart`."""
    if self.tool_name_delta:
      # Append incremental text to the existing tool_name
      tool_name = part.tool_name + self.tool_name_delta
      part = replace(part, tool_name=tool_name)
    if isinstance(self.args_delta, str):
      if not isinstance(part.args, str):
        raise UnexpectedModelBehavior(f'Cannot apply JSON deltas to non-JSON tool arguments ({part=}, {self=})')
      updated_json = part.args + self.args_delta
      part = replace(part, args=updated_json)
    elif isinstance(self.args_delta, dict):
      if not isinstance(part.args, dict):
        raise UnexpectedModelBehavior(f'Cannot apply dict deltas to non-dict tool arguments ({part=}, {self=})')
      updated_dict = {**(part.args or {}), **self.args_delta}
      part = replace(part, args=updated_dict)
    if self.tool_call_id:
      # Replace the tool_call_id entirely if given
      if part.tool_call_id is not None and part.tool_call_id != self.tool_call_id:
        raise UnexpectedModelBehavior(
          f'Cannot apply a new tool_call_id to a ToolCallPartDelta that already has one ({part=}, {self=})'
        )
      part = replace(part, tool_call_id=self.tool_call_id)
    return part

```
  
---|---  
####  tool_name_delta `class-attribute` `instance-attribute`
```
tool_name_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Incremental text to add to the existing tool name, if any.
####  args_delta `class-attribute` `instance-attribute`
```
args_delta: str[](https://docs.python.org/3/library/stdtypes.html#str) | dict[](https://docs.python.org/3/library/stdtypes.html#dict)[str[](https://docs.python.org/3/library/stdtypes.html#str), Any[](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any")] | None = None

```

Incremental data to add to the tool arguments.
If this is a string, it will be appended to existing JSON arguments. If this is a dict, it will be merged with existing dict arguments.
####  tool_call_id `class-attribute` `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None = None

```

Optional tool call identifier, this is used by some models including OpenAI.
Note this is never treated as a delta — it can replace None, but otherwise if a non-matching value is provided an error will be raised.
####  part_delta_kind `class-attribute` `instance-attribute`
```
part_delta_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['tool_call'] = 'tool_call'

```

Part delta type identifier, used as a discriminator.
####  as_part
```
as_part() -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart") | None

```

Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.
Returns:
Type | Description  
---|---  
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart") | None` |  A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.  
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
555
556
557
558
559
560
561
562
563
564
565
566
567
568
```
| ```
defas_part(self) -> ToolCallPart | None:
"""Convert this delta to a fully formed `ToolCallPart` if possible, otherwise return `None`.
  Returns:
    A `ToolCallPart` if both `tool_name_delta` and `args_delta` are set, otherwise `None`.
  """
  if self.tool_name_delta is None or self.args_delta is None:
    return None
  return ToolCallPart(
    self.tool_name_delta,
    self.args_delta,
    self.tool_call_id,
  )

```
  
---|---  
####  apply
```
apply(part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart")) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart")

```

```
apply(
  part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta")

```

```
apply(
  part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta"),
) -> ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta")

```

Apply this delta to a part or delta, returning a new part or delta with the changes applied.
Parameters:
Name | Type | Description | Default  
---|---|---|---  
`part` |  `ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta")` |  The existing model response part or delta to update. |  _required_  
Returns:
Type | Description  
---|---  
`ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart") | ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta")` |  Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.  
Raises:
Type | Description  
---|---  
`ValueError[](https://docs.python.org/3/library/exceptions.html#ValueError)` |  If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.  
`UnexpectedModelBehavior[](https://ai.pydantic.dev/api/exceptions/#pydantic_ai.exceptions.UnexpectedModelBehavior "pydantic_ai.exceptions.UnexpectedModelBehavior")` |  If applying JSON deltas to dict arguments or vice versa.  
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
```
| ```
defapply(self, part: ModelResponsePart | ToolCallPartDelta) -> ToolCallPart | ToolCallPartDelta:
"""Apply this delta to a part or delta, returning a new part or delta with the changes applied.
  Args:
    part: The existing model response part or delta to update.
  Returns:
    Either a new `ToolCallPart` or an updated `ToolCallPartDelta`.
  Raises:
    ValueError: If `part` is neither a `ToolCallPart` nor a `ToolCallPartDelta`.
    UnexpectedModelBehavior: If applying JSON deltas to dict arguments or vice versa.
  """
  if isinstance(part, ToolCallPart):
    return self._apply_to_part(part)
  if isinstance(part, ToolCallPartDelta):
    return self._apply_to_delta(part)
  raise ValueError(f'Can only apply ToolCallPartDeltas to ToolCallParts or ToolCallPartDeltas, not {part}')

```
  
---|---  
###  ModelResponsePartDelta `module-attribute`
```
ModelResponsePartDelta = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[TextPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.TextPartDelta "pydantic_ai.messages.TextPartDelta"), ToolCallPartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPartDelta "pydantic_ai.messages.ToolCallPartDelta")],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("part_delta_kind"),
]

```

A partial update (delta) for any model response part.
###  PartStartEvent `dataclass`
An event indicating that a new part has started.
If multiple `PartStartEvent`s are received with the same index, the new one should fully replace the old one.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
```
| ```
@dataclass
classPartStartEvent:
"""An event indicating that a new part has started.
  If multiple `PartStartEvent`s are received with the same index,
  the new one should fully replace the old one.
  """
  index: int
"""The index of the part within the overall response parts list."""
  part: ModelResponsePart
"""The newly started `ModelResponsePart`."""
  event_kind: Literal['part_start'] = 'part_start'
"""Event type identifier, used as a discriminator."""

```
  
---|---  
####  index `instance-attribute`
```
index: int[](https://docs.python.org/3/library/functions.html#int)

```

The index of the part within the overall response parts list.
####  part `instance-attribute`
```
part: ModelResponsePart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePart "pydantic_ai.messages.ModelResponsePart")

```

The newly started `ModelResponsePart`.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['part_start'] = 'part_start'

```

Event type identifier, used as a discriminator.
###  PartDeltaEvent `dataclass`
An event indicating a delta update for an existing part.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
687
688
689
690
691
692
693
694
695
696
697
698
```
| ```
@dataclass
classPartDeltaEvent:
"""An event indicating a delta update for an existing part."""
  index: int
"""The index of the part within the overall response parts list."""
  delta: ModelResponsePartDelta
"""The delta to apply to the specified part."""
  event_kind: Literal['part_delta'] = 'part_delta'
"""Event type identifier, used as a discriminator."""

```
  
---|---  
####  index `instance-attribute`
```
index: int[](https://docs.python.org/3/library/functions.html#int)

```

The index of the part within the overall response parts list.
####  delta `instance-attribute`
```
delta: ModelResponsePartDelta[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelResponsePartDelta "pydantic_ai.messages.ModelResponsePartDelta")

```

The delta to apply to the specified part.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['part_delta'] = 'part_delta'

```

Event type identifier, used as a discriminator.
###  FinalResultEvent `dataclass`
An event indicating the response to the current model request matches the result schema.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
701
702
703
704
705
706
707
708
709
710
```
| ```
@dataclass
classFinalResultEvent:
"""An event indicating the response to the current model request matches the result schema."""
  tool_name: str | None
"""The name of the result tool that was called. `None` if the result is from text content and not from a tool."""
  tool_call_id: str | None
"""The tool call ID, if any, that this result is associated with."""
  event_kind: Literal['final_result'] = 'final_result'
"""Event type identifier, used as a discriminator."""

```
  
---|---  
####  tool_name `instance-attribute`
```
tool_name: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The name of the result tool that was called. `None` if the result is from text content and not from a tool.
####  tool_call_id `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) | None

```

The tool call ID, if any, that this result is associated with.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")['final_result'] = 'final_result'

```

Event type identifier, used as a discriminator.
###  ModelResponseStreamEvent `module-attribute`
```
ModelResponseStreamEvent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "pydantic_ai.messages.PartStartEvent"), PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "pydantic_ai.messages.PartDeltaEvent")],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the model response stream, either starting a new part or applying a delta to an existing one.
###  AgentStreamEvent `module-attribute`
```
AgentStreamEvent = Annotated[](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated")[
  Union[](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union")[PartStartEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartStartEvent "pydantic_ai.messages.PartStartEvent"), PartDeltaEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.PartDeltaEvent "pydantic_ai.messages.PartDeltaEvent"), FinalResultEvent[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.FinalResultEvent "pydantic_ai.messages.FinalResultEvent")],
  Discriminator[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Discriminator "pydantic.Discriminator")("event_kind"),
]

```

An event in the agent stream.
###  FunctionToolCallEvent `dataclass`
An event indicating the start to a call to a function tool.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
722
723
724
725
726
727
728
729
730
731
732
733
734
```
| ```
@dataclass
classFunctionToolCallEvent:
"""An event indicating the start to a call to a function tool."""
  part: ToolCallPart
"""The (function) tool call to make."""
  call_id: str = field(init=False)
"""An ID used for matching details about the call to its result. If present, defaults to the part's tool_call_id."""
  event_kind: Literal['function_tool_call'] = 'function_tool_call'
"""Event type identifier, used as a discriminator."""
  def__post_init__(self):
    self.call_id = self.part.tool_call_id or str(uuid.uuid4())

```
  
---|---  
####  part `instance-attribute`
```
part: ToolCallPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolCallPart "pydantic_ai.messages.ToolCallPart")

```

The (function) tool call to make.
####  call_id `class-attribute` `instance-attribute`
```
call_id: str[](https://docs.python.org/3/library/stdtypes.html#str) = field[](https://docs.python.org/3/library/dataclasses.html#dataclasses.field "dataclasses.field")(init=False)

```

An ID used for matching details about the call to its result. If present, defaults to the part's tool_call_id.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["function_tool_call"] = (
  "function_tool_call"
)

```

Event type identifier, used as a discriminator.
###  FunctionToolResultEvent `dataclass`
An event indicating the result of a function tool call.
Source code in `pydantic_ai_slim/pydantic_ai/messages.py`
```
737
738
739
740
741
742
743
744
745
746
```
| ```
@dataclass
classFunctionToolResultEvent:
"""An event indicating the result of a function tool call."""
  result: ToolReturnPart | RetryPromptPart
"""The result of the call to the function tool."""
  tool_call_id: str
"""An ID used to match the result to its original call."""
  event_kind: Literal['function_tool_result'] = 'function_tool_result'
"""Event type identifier, used as a discriminator."""

```
  
---|---  
####  result `instance-attribute`
```
result: ToolReturnPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ToolReturnPart "pydantic_ai.messages.ToolReturnPart") | RetryPromptPart[](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.RetryPromptPart "pydantic_ai.messages.RetryPromptPart")

```

The result of the call to the function tool.
####  tool_call_id `instance-attribute`
```
tool_call_id: str[](https://docs.python.org/3/library/stdtypes.html#str)

```

An ID used to match the result to its original call.
####  event_kind `class-attribute` `instance-attribute`
```
event_kind: Literal[](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal")["function_tool_result"] = (
  "function_tool_result"
)

```

Event type identifier, used as a discriminator.
© Pydantic Services Inc. 2024 to present 
