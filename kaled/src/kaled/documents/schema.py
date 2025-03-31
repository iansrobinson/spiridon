import abc  
from llama_index.core.schema import TextNode

class DocBase():
    @abc.abstractmethod
    def to_doc(self, s:str) -> TextNode:
        raise NotImplementedError
        