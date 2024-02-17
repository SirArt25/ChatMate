import pypdf
from langchain_community.document_loaders import PyPDFLoader


class Loader:
    def __init__(self, path: str):
        self.__path = path

    def load_pages(self):
        return PyPDFLoader(self.__path).load()

    def load_chunks(self):
        return PyPDFLoader(self.__path).load_and_split()
