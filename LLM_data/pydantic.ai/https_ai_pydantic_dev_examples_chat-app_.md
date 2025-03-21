[ Skip to content ](https://ai.pydantic.dev/examples/chat-app/#chat-app-with-fastapi)
[ ![logo](https://ai.pydantic.dev/img/logo-white.svg) ](https://ai.pydantic.dev/ "PydanticAI")
PydanticAI 
Chat App with FastAPI 
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
    * Chat App with FastAPI  [ Chat App with FastAPI  ](https://ai.pydantic.dev/examples/chat-app/) Table of contents 
      * [ Running the Example  ](https://ai.pydantic.dev/examples/chat-app/#running-the-example)
      * [ Example Code  ](https://ai.pydantic.dev/examples/chat-app/#example-code)
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
  * [ Running the Example  ](https://ai.pydantic.dev/examples/chat-app/#running-the-example)
  * [ Example Code  ](https://ai.pydantic.dev/examples/chat-app/#example-code)


# Chat App with FastAPI
Simple chat app example build with FastAPI.
Demonstrates:
  * [reusing chat history](https://ai.pydantic.dev/message-history/)
  * [serializing messages](https://ai.pydantic.dev/message-history/#accessing-messages-from-results)
  * [streaming responses](https://ai.pydantic.dev/results/#streamed-results)


This demonstrates storing chat history between requests and using it to give the model context for new responses.
Most of the complex logic here is between `chat_app.py` which streams the response to the browser, and `chat_app.ts` which renders messages in the browser.
## Running the Example
With [dependencies installed and environment variables set](https://ai.pydantic.dev/examples/#usage), run:
[pip](https://ai.pydantic.dev/examples/chat-app/#__tabbed_1_1)[uv](https://ai.pydantic.dev/examples/chat-app/#__tabbed_1_2)
```
python-mpydantic_ai_examples.chat_app

```

```
uvrun-mpydantic_ai_examples.chat_app

```

Then open the app at [localhost:8000](http://localhost:8000).
[![Example conversation](https://ai.pydantic.dev/img/chat-app-example.png)](https://ai.pydantic.dev/img/chat-app-example.png)
## Example Code
Python code that runs the chat app:
chat_app.py```
from__future__import annotations as _annotations
importasyncio
importjson
importsqlite3
fromcollections.abcimport AsyncIterator
fromconcurrent.futures.threadimport ThreadPoolExecutor
fromcontextlibimport asynccontextmanager
fromdataclassesimport dataclass
fromdatetimeimport datetime, timezone
fromfunctoolsimport partial
frompathlibimport Path
fromtypingimport Annotated, Any, Callable, Literal, TypeVar
importfastapi
importlogfire
fromfastapiimport Depends, Request
fromfastapi.responsesimport FileResponse, Response, StreamingResponse
fromtyping_extensionsimport LiteralString, ParamSpec, TypedDict
frompydantic_aiimport Agent
frompydantic_ai.exceptionsimport UnexpectedModelBehavior
frompydantic_ai.messagesimport (
  ModelMessage,
  ModelMessagesTypeAdapter,
  ModelRequest,
  ModelResponse,
  TextPart,
  UserPromptPart,
)
# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')
agent = Agent('openai:gpt-4o', instrument=True)
THIS_DIR = Path(__file__).parent

@asynccontextmanager
async deflifespan(_app: fastapi.FastAPI):
  async with Database.connect() as db:
    yield {'db': db}

app = fastapi.FastAPI(lifespan=lifespan)
logfire.instrument_fastapi(app)

@app.get('/')
async defindex() -> FileResponse:
  return FileResponse((THIS_DIR / 'chat_app.html'), media_type='text/html')

@app.get('/chat_app.ts')
async defmain_ts() -> FileResponse:
"""Get the raw typescript code, it's compiled in the browser, forgive me."""
  return FileResponse((THIS_DIR / 'chat_app.ts'), media_type='text/plain')

async defget_db(request: Request) -> Database:
  return request.state.db

@app.get('/chat/')
async defget_chat(database: Database = Depends(get_db)) -> Response:
  msgs = await database.get_messages()
  return Response(
    b'\n'.join(json.dumps(to_chat_message(m)).encode('utf-8') for m in msgs),
    media_type='text/plain',
  )

classChatMessage(TypedDict):
"""Format of messages sent to the browser."""
  role: Literal['user', 'model']
  timestamp: str
  content: str

defto_chat_message(m: ModelMessage) -> ChatMessage:
  first_part = m.parts[0]
  if isinstance(m, ModelRequest):
    if isinstance(first_part, UserPromptPart):
      assert isinstance(first_part.content, str)
      return {
        'role': 'user',
        'timestamp': first_part.timestamp.isoformat(),
        'content': first_part.content,
      }
  elif isinstance(m, ModelResponse):
    if isinstance(first_part, TextPart):
      return {
        'role': 'model',
        'timestamp': m.timestamp.isoformat(),
        'content': first_part.content,
      }
  raise UnexpectedModelBehavior(f'Unexpected message type for chat app: {m}')

@app.post('/chat/')
async defpost_chat(
  prompt: Annotated[str, fastapi.Form()], database: Database = Depends(get_db)
) -> StreamingResponse:
  async defstream_messages():
"""Streams new line delimited JSON `Message`s to the client."""
    # stream the user prompt so that can be displayed straight away
    yield (
      json.dumps(
        {
          'role': 'user',
          'timestamp': datetime.now(tz=timezone.utc).isoformat(),
          'content': prompt,
        }
      ).encode('utf-8')
      + b'\n'
    )
    # get the chat history so far to pass as context to the agent
    messages = await database.get_messages()
    # run the agent with the user prompt and the chat history
    async with agent.run_stream(prompt, message_history=messages) as result:
      async for text in result.stream(debounce_by=0.01):
        # text here is a `str` and the frontend wants
        # JSON encoded ModelResponse, so we create one
        m = ModelResponse(parts=[TextPart(text)], timestamp=result.timestamp())
        yield json.dumps(to_chat_message(m)).encode('utf-8') + b'\n'
    # add new messages (e.g. the user prompt and the agent response in this case) to the database
    await database.add_messages(result.new_messages_json())
  return StreamingResponse(stream_messages(), media_type='text/plain')

P = ParamSpec('P')
R = TypeVar('R')

@dataclass
classDatabase:
"""Rudimentary database to store chat messages in SQLite.
  The SQLite standard library package is synchronous, so we
  use a thread pool executor to run queries asynchronously.
  """
  con: sqlite3.Connection
  _loop: asyncio.AbstractEventLoop
  _executor: ThreadPoolExecutor
  @classmethod
  @asynccontextmanager
  async defconnect(
    cls, file: Path = THIS_DIR / '.chat_app_messages.sqlite'
  ) -> AsyncIterator[Database]:
    with logfire.span('connect to DB'):
      loop = asyncio.get_event_loop()
      executor = ThreadPoolExecutor(max_workers=1)
      con = await loop.run_in_executor(executor, cls._connect, file)
      slf = cls(con, loop, executor)
    try:
      yield slf
    finally:
      await slf._asyncify(con.close)
  @staticmethod
  def_connect(file: Path) -> sqlite3.Connection:
    con = sqlite3.connect(str(file))
    con = logfire.instrument_sqlite3(con)
    cur = con.cursor()
    cur.execute(
      'CREATE TABLE IF NOT EXISTS messages (id INT PRIMARY KEY, message_list TEXT);'
    )
    con.commit()
    return con
  async defadd_messages(self, messages: bytes):
    await self._asyncify(
      self._execute,
      'INSERT INTO messages (message_list) VALUES (?);',
      messages,
      commit=True,
    )
    await self._asyncify(self.con.commit)
  async defget_messages(self) -> list[ModelMessage]:
    c = await self._asyncify(
      self._execute, 'SELECT message_list FROM messages order by id'
    )
    rows = await self._asyncify(c.fetchall)
    messages: list[ModelMessage] = []
    for row in rows:
      messages.extend(ModelMessagesTypeAdapter.validate_json(row[0]))
    return messages
  def_execute(
    self, sql: LiteralString, *args: Any, commit: bool = False
  ) -> sqlite3.Cursor:
    cur = self.con.cursor()
    cur.execute(sql, args)
    if commit:
      self.con.commit()
    return cur
  async def_asyncify(
    self, func: Callable[P, R], *args: P.args, **kwargs: P.kwargs
  ) -> R:
    return await self._loop.run_in_executor( # type: ignore
      self._executor,
      partial(func, **kwargs),
      *args, # type: ignore
    )

if __name__ == '__main__':
  importuvicorn
  uvicorn.run(
    'pydantic_ai_examples.chat_app:app', reload=True, reload_dirs=[str(THIS_DIR)]
  )

```

Simple HTML page to render the app:
chat_app.html```
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Chat App</title>
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
 <style>
main{
max-width:700px;
}
#conversation.user::before{
content:'You asked: ';
font-weight:bold;
display:block;
}
#conversation.model::before{
content:'AI Response: ';
font-weight:bold;
display:block;
}
#spinner{
opacity:0;
transition:opacity500msease-in;
width:30px;
height:30px;
border:3pxsolid#222;
border-bottom-color:transparent;
border-radius:50%;
animation:rotation1slinearinfinite;
}
@keyframesrotation{
0%{transform:rotate(0deg);}
100%{transform:rotate(360deg);}
}
#spinner.active{
opacity:1;
}
</style>
</head>
<body>
 <main class="border rounded mx-auto my-5 p-4">
  <h1>Chat App</h1>
  <p>Ask me anything...</p>
  <div id="conversation" class="px-2"></div>
  <div class="d-flex justify-content-center mb-3">
   <div id="spinner"></div>
  </div>
  <form method="post">
   <input id="prompt-input" name="prompt" class="form-control"/>
   <div class="d-flex justify-content-end">
    <button class="btn btn-primary mt-2">Send</button>
   </div>
  </form>
  <div id="error" class="d-none text-danger">
   Error occurred, check the browser developer console for more information.
  </div>
 </main>
</body>
</html>
<script src="https://cdnjs.cloudflare.com/ajax/libs/typescript/5.6.3/typescript.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script type="module">
// to let me write TypeScript, without adding the burden of npm we do a dirty, non-production-ready hack
// and transpile the TypeScript code in the browser
// this is (arguably) A neat demo trick, but not suitable for production!
asyncfunctionloadTs(){
constresponse=awaitfetch('/chat_app.ts');
consttsCode=awaitresponse.text();
constjsCode=window.ts.transpile(tsCode,{target:"es2015"});
letscript=document.createElement('script');
script.type='module';
script.text=jsCode;
document.body.appendChild(script);
}
loadTs().catch((e)=>{
console.error(e);
document.getElementById('error').classList.remove('d-none');
document.getElementById('spinner').classList.remove('active');
});
</script>

```

TypeScript to handle rendering the messages, to keep this simple (and at the risk of offending frontend developers) the typescript code is passed to the browser as plain text and transpiled in the browser.
chat_app.ts```
// BIG FAT WARNING: to avoid the complexity of npm, this typescript is compiled in the browser
// there's currently no static type checking
import{marked}from'https://cdnjs.cloudflare.com/ajax/libs/marked/15.0.0/lib/marked.esm.js'
constconvElement=document.getElementById('conversation')
constpromptInput=document.getElementById('prompt-input')asHTMLInputElement
constspinner=document.getElementById('spinner')
// stream the response and render messages as each chunk is received
// data is sent as newline-delimited JSON
asyncfunctiononFetchResponse(response:Response):Promise<void>{
lettext=''
letdecoder=newTextDecoder()
if(response.ok){
constreader=response.body.getReader()
while(true){
const{done,value}=awaitreader.read()
if(done){
break
}
text+=decoder.decode(value)
addMessages(text)
spinner.classList.remove('active')
}
addMessages(text)
promptInput.disabled=false
promptInput.focus()
}else{
consttext=awaitresponse.text()
console.error(`Unexpected response: ${response.status}`,{response,text})
thrownewError(`Unexpected response: ${response.status}`)
}
}
// The format of messages, this matches pydantic-ai both for brevity and understanding
// in production, you might not want to keep this format all the way to the frontend
interfaceMessage{
role:string
content:string
timestamp:string
}
// take raw response text and render messages into the `#conversation` element
// Message timestamp is assumed to be a unique identifier of a message, and is used to deduplicate
// hence you can send data about the same message multiple times, and it will be updated
// instead of creating a new message elements
functionaddMessages(responseText:string){
constlines=responseText.split('\n')
constmessages:Message[]=lines.filter(line=>line.length>1).map(j=>JSON.parse(j))
for(constmessageofmessages){
// we use the timestamp as a crude element id
const{timestamp,role,content}=message
constid=`msg-${timestamp}`
letmsgDiv=document.getElementById(id)
if(!msgDiv){
msgDiv=document.createElement('div')
msgDiv.id=id
msgDiv.title=`${role} at ${timestamp}`
msgDiv.classList.add('border-top','pt-2',role)
convElement.appendChild(msgDiv)
}
msgDiv.innerHTML=marked.parse(content)
}
window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'})
}
functiononError(error:any){
console.error(error)
document.getElementById('error').classList.remove('d-none')
document.getElementById('spinner').classList.remove('active')
}
asyncfunctiononSubmit(e:SubmitEvent):Promise<void>{
e.preventDefault()
spinner.classList.add('active')
constbody=newFormData(e.targetasHTMLFormElement)
promptInput.value=''
promptInput.disabled=true
constresponse=awaitfetch('/chat/',{method:'POST',body})
awaitonFetchResponse(response)
}
// call onSubmit when the form is submitted (e.g. user clicks the send button or hits Enter)
document.querySelector('form').addEventListener('submit',(e)=>onSubmit(e).catch(onError))
// load messages on page load
fetch('/chat/').then(onFetchResponse).catch(onError)

```

© Pydantic Services Inc. 2024 to present 
