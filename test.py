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

queue = Queue()


class StreamingHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> Any:
        queue.put(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> Any:
        queue.put(None)

    def on_llm_error(self, error, **kwargs):
        queue.put(None)


chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamingHandler()]
)  # Controls how OpenAI responds to LangChain; streaming=True makes OpenAI stream to LangChain no matter what

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])


class StreamingChain(LLMChain):
    def stream(self, input):
        def task():
            self(input)  # Runs the chain

        # A thread will allow the chain to start, but will then immediately move on to
        # the 'while' loop, instead of waiting for the chain to complete before moving on.
        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token


chain = StreamingChain(llm=chat, prompt=prompt)

for output in chain.stream(input={"content": "tell me a joke"}):
    print(output)