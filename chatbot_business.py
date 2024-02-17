from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI


import datetime
from vectordb import MiniDB
from loader import Loader
from langchain.prompts import PromptTemplate

class Chatbot:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):

        # Build prompt
        template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
        {context}
        Question: {question}
        Helpful Answer:"""
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

        if datetime.datetime.now().date() < datetime.date(2023, 9, 2):
            self.__llm_name = "gpt-3.5-turbo-0301"
        else:
            self.__llm_name = "gpt-3.5-turbo"
        self.__mini_db = MiniDB()
        self.__mini_db .create(Loader("manuals/git.pdf"))

        llm = ChatOpenAI(model_name=self.__llm_name, temperature=0)
        self.__qa_chain = RetrievalQA.from_chain_type(
            llm,
            retriever=self.__mini_db .get_vector_store().as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )

    def ask(self, question:str):
        return self.__qa_chain.invoke({"query": question})["result"]