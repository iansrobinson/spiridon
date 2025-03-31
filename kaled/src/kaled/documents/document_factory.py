import abc

document_factory_registry = {}


class DocumentFactoryRegistration(type):
    def __init__(cls, name, bases, attrs):
        if DocumentFactory in bases:            
            document_factory_registry[name] = cls
        else:
            raise ValueError(f'Invalid type ({name}) – must implement DocumentFactory')
        
class DocumentFactory():

    @staticmethod
    def for_document(s):
        for name, c in document_factory_registry.items():
            document_factory = c()
            document = document_factory.try_create(s)
            if document:
                print(f'Creating doc with {name}')
                return document
        return None


    @abc.abstractmethod
    def try_create(self, s):
        raise NotImplementedException