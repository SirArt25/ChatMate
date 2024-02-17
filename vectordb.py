from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from loader import Loader
import os
import tiktoken


class MiniDB:
    __instance = None

    def load(self):
        if not os.path.exists(self.__persist_directory):
             return False

        self.__db = Chroma(
            embedding_function=OpenAIEmbeddings(),
            persist_directory=self.__persist_directory
        )
        return True

    def create(self, loader : Loader):
        self.__db = Chroma.from_documents(
            documents=loader.load_chunks(),
            embedding=OpenAIEmbeddings(),
            persist_directory=self.__persist_directory
        )
    def __init__(self, persist_directory = 'docs/chroma/'):
        self.__db = None
        self.__persist_directory = persist_directory

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
