from kaled.documents import DocBase, DocumentFactory, DocumentFactoryRegistration
from llama_index.core.schema import TextNode

class ThalDoc(DocBase):  
    def to_doc(self, s):
        return TextNode(text=s.upper())
        
class ThalDocFactory(DocumentFactory, metaclass=DocumentFactoryRegistration):
    def try_create(self, s):
        if 'thal' in s:
            return ThalDoc
        else:
            return None
        