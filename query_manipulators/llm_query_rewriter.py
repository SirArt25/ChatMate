from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate

from query_manipulators.query_rewriter import QueryRewriter
from pyrsistent import freeze
class LLMQueryRewriter(QueryRewriter):
    def __init__(self, llm: BaseLanguageModel):
        self.__initializer(freeze(llm))

    def __initializer(self, llm: BaseLanguageModel):
        self.__template = """Use the following pieces of question to rewrite and correct the question at the end.
                        {question}"""
        self.__llm = llm
    def rewrite(self, query: str) -> str:
        query_prompt = PromptTemplate.from_template(self.__template)
        formated_query = query_prompt.format(question=query)
        return self.__llm.invoke(formated_query)