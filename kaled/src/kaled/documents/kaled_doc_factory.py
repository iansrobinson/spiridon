from kaled.documenst import DocumentFactory, DocumentFactoryRegistration
from kaled.documents.kaled import KaledDoc

class KaledDocFactory(DocumentFactory, metaclass=DocumentFactoryRegistration):
    def try_create(self, s):
        if 'kaled' in s:
            return KaledDoc()
        else:
            return None


        