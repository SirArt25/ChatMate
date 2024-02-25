from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from utilities.loader import Loader
from typing import Iterable
from utilities.logic_error import LogicError
from langchain_core.documents import Document

import os


class MiniDB:
    __instance = None

    def load(self) -> bool:
        if not os.path.exists(self.__persist_directory):
            return False

        self.__db = Chroma(
            embedding_function=OpenAIEmbeddings(),
            persist_directory=self.__persist_directory
        )
        return True

    def exist(self) -> bool:
        return os.path.exists(self.__persist_directory)

    def create(self, documents: Iterable[Document]):
        if os.path.exists(self.__persist_directory):
            raise LogicError("Cannot created twice")

        self.__db = Chroma.from_documents(
            documents=documents,
            embedding=OpenAIEmbeddings(),
            persist_directory=self.__persist_directory
        )

    def __init__(self, persist_directory='docs/chroma/'):
        self.__db = None
        self.__persist_directory = persist_directory

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_vector_store(self):
        return self.__db
