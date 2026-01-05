from langchain.chains import ConversationalRetrievalChain
from app.chat.chains.streamable import StreamableChain


# Uses the StreamableChain Mixin to add the 'stream' function
class StreamingConversationalRetrievalChain(
    StreamableChain, ConversationalRetrievalChain
):
    pass

