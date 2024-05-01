from src.parentnode import ParentNode
from src.textnode import TextNode

class Code(ParentNode):

    def __init__(self, value, props=None):

        children = [TextNode(value.strip('`'), 'code')]
        super().__init__('pre',  children = children, props = props)


    