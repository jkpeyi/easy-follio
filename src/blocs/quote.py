from src.htmlnode import HTMLNode
from src.utils import text_to_textnodes
class Quote(HTMLNode):

    
    def __init__(self, value:str, props=None):

        children = text_to_textnodes(value.strip('>'))
        super().__init__('blockquote', children=children, props= props)
    pass