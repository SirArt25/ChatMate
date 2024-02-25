from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from utilities.decorators import strict_classmethod
from utilities.vectordb import MiniDB
from utilities.loader import Loader
from typing import Optional
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

import datetime
import streamlit as st
import os


# we assume that ChatbotEngine can be more than one
class ChatbotEngine:

    def ask(self, question: str):
        return self.__qa_chain.invoke({"query": question})["result"]

    @strict_classmethod
    @st.cache_resource
    def create_engine(self):
        temp = ChatbotEngine()
        temp.__initialize_template()
        temp.__initialize_db()
        temp.__initialize_core()
        return temp

    def __initialize_template(self, template: Optional[str] = None):
        if not template is None:
            template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, 
                just say that you don't know, don't try to make up an answer.
                Use ten sentences maximum. Keep the answer as concise as possible.
                Always say "thanks for asking!" at the end of the answer. 
                        {context}
                        Question: {question}
                        Helpful Answer:"""

        self.__qa_chain_prompt = PromptTemplate.from_template(template)

    def __initialize_db(self, persist_directory='docs/chroma/'):
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

    def __initialize_core(self):
        # Build prompt

        if datetime.datetime.now().date() < datetime.date(2023, 9, 2):
            self.__llm_name = "gpt-3.5-turbo-0301"
        else:
            self.__llm_name = "gpt-3.5-turbo"

        llm = ChatOpenAI(model_name=self.__llm_name, temperature=0)
        self.__qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=self.__mini_db.get_vector_store().as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.__qa_chain_prompt}
        )
