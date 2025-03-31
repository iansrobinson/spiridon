from kaled.documents import DocBase, DocumentFactory, DocumentFactoryRegistration
from llama_index.core.schema import TextNode

class KaledDoc(DocBase):    
    def to_doc(self, s):
        return TextNode(text=s)


        