from kaled.documents import DocumentFactory, DocumentFactoryRegistration
from kaled.documents.thal import ThalDoc

        
class ThalDocFactory(DocumentFactory, metaclass=DocumentFactoryRegistration):
    def try_create(self, s):
        if 'thal' in s:
            return ThalDoc()
        else:
            return None
        