import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from app.chat.embeddings.openai import embeddings
from dotenv import load_dotenv

load_dotenv()

# start 'inv dev' in a new terminal when you change the .env file

pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

vector_store = PineconeVectorStore.from_existing_index(
    index_name=os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings
)


def build_retriever(chat_args):
    search_kwargs = {"filter": {"pdf_id": chat_args.pdf_id}}
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )