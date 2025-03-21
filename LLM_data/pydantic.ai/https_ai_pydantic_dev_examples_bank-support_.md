[ Skip to content ](https://ai.pydantic.dev/examples/bank-support/#running-the-example)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Bank support 
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
    * Bank support  [ Bank support  ](https://ai.pydantic.dev/examples/bank-support/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/bank-support/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/bank-support/#example-code)
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
  * [ Running the Example  ](https://ai.pydantic.dev/examples/bank-support/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/bank-support/#example-code)


# Bank support
Small but complete example of using PydanticAI to build a support agent for a bank.
Demonstrates:
  * [dynamic system prompt](https://ai.pydantic.dev/agents/#system-prompts)
  * [structured `result_type`](https://ai.pydantic.dev/results/#structured-result-validation)
  * [tools](https://ai.pydantic.dev/tools/)


## Running the Example
With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/bank-support/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/bank-support/#__tabbed_1_2)
```
python-mpydantic_ai_examples.bank_support

```

```
uvrun-mpydantic_ai_examples.bank_support

```

(or `PYDANTIC_AI_MODEL=gemini-1.5-flash ...`)
## Example Code
bank_support.py```
fromdataclassesimport dataclass
frompydanticimport BaseModel, Field
frompydantic_aiimport Agent, RunContext

classDatabaseConn:
"""This is a fake database for example purposes.
  In reality, you'd be connecting to an external database
  (e.g. PostgreSQL) to get information about customers.
  """
  @classmethod
  async defcustomer_name(cls, *, id: int) -> str | None:
    if id == 123:
      return 'John'
  @classmethod
  async defcustomer_balance(cls, *, id: int, include_pending: bool) -> float:
    if id == 123 and include_pending:
      return 123.45
    else:
      raise ValueError('Customer not found')

@dataclass
classSupportDependencies:
  customer_id: int
  db: DatabaseConn

classSupportResult(BaseModel):
  support_advice: str = Field(description='Advice returned to the customer')
  block_card: bool = Field(description='Whether to block their card or not')
  risk: int = Field(description='Risk level of query', ge=0, le=10)

support_agent = Agent(
  'openai:gpt-4o',
  deps_type=SupportDependencies,
  result_type=SupportResult,
  system_prompt=(
    'You are a support agent in our bank, give the '
    'customer support and judge the risk level of their query. '
    "Reply using the customer's name."
  ),
)

@support_agent.system_prompt
async defadd_customer_name(ctx: RunContext[SupportDependencies]) -> str:
  customer_name = await ctx.deps.db.customer_name(id=ctx.deps.customer_id)
  return f"The customer's name is {customer_name!r}"

@support_agent.tool
async defcustomer_balance(
  ctx: RunContext[SupportDependencies], include_pending: bool
) -> str:
"""Returns the customer's current account balance."""
  balance = await ctx.deps.db.customer_balance(
    id=ctx.deps.customer_id,
    include_pending=include_pending,
  )
  return f'${balance:.2f}'

if __name__ == '__main__':
  deps = SupportDependencies(customer_id=123, db=DatabaseConn())
  result = support_agent.run_sync('What is my balance?', deps=deps)
  print(result.data)
"""
  support_advice='Hello John, your current account balance, including pending transactions, is $123.45.' block_card=False risk=1
  """
  result = support_agent.run_sync('I just lost my card!', deps=deps)
  print(result.data)
"""
  support_advice="I'm sorry to hear that, John. We are temporarily blocking your card to prevent unauthorized transactions." block_card=True risk=8
  """

```

© Pydantic Services Inc. 2024 to present 
