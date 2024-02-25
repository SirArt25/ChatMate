from abc import ABC, abstractmethod


class QueryRewriter(ABC):
    @abstractmethod
    def rewrite(self, query: str) -> str:
        pass
