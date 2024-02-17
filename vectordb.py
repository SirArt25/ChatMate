from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from loader import Loader


class MiniDB:
    __instance = None

    def __init__(self, persist_directory: str, loader: Loader):
        self.__db = Chroma.from_documents(
            documents=loader.load_chunks(),
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_directory
        )

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
