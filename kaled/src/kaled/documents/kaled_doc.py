from .schema import DocBase
from .document_factory import DocumentFactory, DocumentFactoryRegistration
from llama_index.core.schema import TextNode

class KaledDoc(DocBase):    
    def to_doc(self, s):
        return TextNode(text=s)

class KaledDocFactory(DocumentFactory, metaclass=DocumentFactoryRegistration):
    def try_create(self, s):
        if 'kaled' in s:
            return KaledDoc
        else:
            return None


        