from src.parentnode import ParentNode
from src.utils import text_to_textnodes


class Paragraph(ParentNode):

    def __init__(self, value, props=None):

        children = text_to_textnodes(value)

        super().__init__("p", children=children, props=props)

    pass
