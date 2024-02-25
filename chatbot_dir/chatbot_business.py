from langchain_openai import ChatOpenAI
from utilities.decorators import strict_classmethod
from utilities.vectordb import MiniDB
from utilities.loader import Loader
from utilities.logic_error import LogicError
from query_manipulators.rewriter.llm_query_rewriter import LLMQueryRewriter
from typing import Optional
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.language_models import BaseLanguageModel
from query_manipulators.retriever.mmr_query_retriever import MMRQueryRetriever

import datetime
import streamlit as st
import os


# we assume that ChatbotEngine can be more than one
class ChatbotEngine:

    def invoke(self, question: str):
        docs = self.__retriever.get_docs(question)

        return ""
        # return self.__qa_chain.invoke({"query": question})["result"]

    def __init__(self):
        pass

    @strict_classmethod
    @st.cache_resource
    def create_engine(self, k: int, fetch_k: int):
        temp = ChatbotEngine()
        temp.__initialize_llm()
        temp.__initialize_template()
        temp.__initialize_db()
        temp.__initialize_rewriter()
        temp.__initialize_retriever(fetch_k=fetch_k, k=k)
        return temp

    def __initialize_template(self, template: Optional[str] = None):
        if template is None:
            template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, 
                just say that you don't know, don't try to make up an answer.
                Use ten sentences maximum. Keep the answer as concise as possible.
                Always say "thanks for asking!" at the end of the answer. 
                        {context}
                        Question: {question}
                        Helpful Answer:"""

        self.__qa_chain_prompt = PromptTemplate.from_template(template)

    def __initialize_db(self, persist_directory: Optional[str] = 'docs/chroma/'):
        self.__mini_db = MiniDB(persist_directory)

        if not self.__mini_db.load():
            manual_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'manuals', 'git.pdf')

            r_splitter = RecursiveCharacterTextSplitter(
                chunk_size=450,
                chunk_overlap=100,
                separators=["\n\n", "\n", "(?<=\. )", " ", ""]
            )

            loader = Loader(manual_path)
            documents = loader.load_chunks(r_splitter)
            self.__mini_db.create(documents)

    def __initialize_llm(self, llm: Optional[BaseLanguageModel] = None):
        if llm is None:
            if datetime.datetime.now().date() < datetime.date(2023, 9, 2):
                llm_name = "gpt-3.5-turbo-0301"
            else:
                llm_name = "gpt-3.5-turbo"
            self.__llm = ChatOpenAI(model_name=llm_name, temperature=0)
        else:
            self.__llm = llm

    def __initialize_rewriter(self, llm: Optional[BaseLanguageModel] = None):
        if llm is None:
            try:
                self.__rewriter = LLMQueryRewriter(self.__llm)
            except AttributeError:
                raise LogicError("Called __initialize_rewriter without any llm model")
        else:
            self.__rewriter = LLMQueryRewriter(llm)

    def __initialize_retriever(self, fetch_k: int, k: int):
        try:
            self.__retriever = MMRQueryRetriever(self.__mini_db.get_vector_store(), fetch_k, k)
        except AttributeError:
            raise LogicError("MiniDb is not initialized")
