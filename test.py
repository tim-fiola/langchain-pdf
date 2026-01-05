from cgitb import handler
from typing import Optional, Union, Any
from langchain_core.outputs import LLMResult
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler
from dotenv import load_dotenv
from queue import Queue
from threading import Thread


load_dotenv()


class StreamingHandler(BaseCallbackHandler):
    def __init__(self, queue):
        self.queue = queue

    def on_llm_new_token(self, token: str, **kwargs) -> Any:
        self.queue.put(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        self.queue.put(None)

    def on_llm_error(self, error, **kwargs):
        self.queue.put(None)


# 'streaming=True' controls how OpenAI responds to LangChain; streaming=True
# makes OpenAI stream to LangChain no matter what
chat = ChatOpenAI(streaming=True)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])


# Make a Mixin Class that defines a single function (stream)
class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task():
            self(input, callbacks=[handler])  # Runs the chain

        # A thread will allow the chain to start, but will then immediately move on to
        # the 'while' loop, instead of waiting for the chain to complete before moving on.
        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token


# Now use the Mixin to pull in the function from the StreamableChain Class to
# extend the LLMChain Class.  The StreamableChain class ensures that the
# 'stream' function is present.  This allows us to more easily extend other chains,
# adding in the 'stream' function
class StreamingChain(StreamableChain, LLMChain):
    pass


chain = StreamingChain(llm=chat, prompt=prompt)

for output in chain.stream(input={"content": "tell me a joke"}):
    print(output)