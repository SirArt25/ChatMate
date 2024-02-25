from typing import List
from langchain_core.documents import Document

class QueryRetriever:
    def get_docs(self, query: str) -> List[Document]:
        pass