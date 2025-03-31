from kaled.schema import DocBase
from llama_index.core.schema import TextNode

class ThalDoc(DocBase):
    
    def to_doc(self, s):
        return TextNode(text=s.upper())
        