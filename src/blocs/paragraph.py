from src.htmlnode import HTMLNode
from src.utils import text_to_textnodes


class Paragraph(HTMLNode):

    def __init__(self, value, props=None):

        children = text_to_textnodes(value)

        super().__init__("p", children=children, props=props)

    pass
