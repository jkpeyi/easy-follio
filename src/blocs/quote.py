from src.parentnode import ParentNode
from src.utils import text_to_textnodes
class Quote(ParentNode):

    
    def __init__(self, value:str, props=None):

        content = value.split('\n')
        content = list(map(lambda item:item.strip('> '), content))
        content = "\n".join(content)
        
        children = text_to_textnodes(content)
        super().__init__('blockquote', children=children, props= props)
    pass