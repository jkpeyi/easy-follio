from src.htmlnode import HTMLNode
from src.textnode import TextNode

class Code(HTMLNode):

    def __init__(self, value, props=None):

        children = [TextNode(value.strip('`'), 'code')]
        super().__init__('pre',  children = children, props = props)


    