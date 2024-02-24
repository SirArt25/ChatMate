import pypdf
from langchain_community.document_loaders import PyPDFLoader
from typing import List
from langchain_core.documents import Document
from typing import Optional
from langchain.text_splitter import TextSplitter


class Loader:
    def __init__(self, path: str):
        self.__path = path

    def load_pages(self) -> List[Document]:
        return PyPDFLoader(self.__path).load()

    def load_chunks(self, text_splitter: Optional[TextSplitter] = None) -> List[Document]:
        return PyPDFLoader(self.__path).load_and_split(text_splitter)
