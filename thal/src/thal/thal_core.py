from json2xml import json2xml
from json2xml.utils import readfromstring

class ThalCore():
    
    def to_xml(self, s):
        data = readfromstring(
            f'{"value":"{s}"}'
        )
        return json2xml.Json2xml(data).to_xml()
        