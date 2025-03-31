from llama_index.core.schema import TextNode

class KaledCore():
    
    def to_doc(self, s):
        return TextNode(text=s)
        