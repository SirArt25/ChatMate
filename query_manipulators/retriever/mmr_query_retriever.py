from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from query_manipulators.retriever.query_retriever import QueryRetriever
from pyrsistent import freeze


class MMRQueryRetriever(QueryRetriever):
    def __init__(self, vectorStore: Chroma, fetch_k: int, k: int):
        self.__initializer(freeze(vectorStore), fetch_k, k)

    def __initializer(self, vectorStore: Chroma, fetch_k: int, k: int):
        self.__vectorStore = vectorStore
        self.__fetch_k = fetch_k
        self.__k = k

    def get_docs(self, query: str):
        return self.__vectorStore.max_marginal_relevance_search(query, k=self.__k, fetch_k=self.__fetch_k)
