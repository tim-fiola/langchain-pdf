from flask import current_app
from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamingHandler


# Make a Mixin Class that defines a single function (stream)
class StreamableChain:
    def stream(self, input):
        queue = Queue()
        handler = StreamingHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[handler])  # Runs the chain

        # A thread will allow the chain to start, but will then immediately move on to
        # the 'while' loop, instead of waiting for the chain to complete before moving on.
        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token
