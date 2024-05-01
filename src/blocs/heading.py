from src.parentnode import ParentNode
from src.utils import text_to_textnodes
class Heading(ParentNode):

    def __init__(self, value, props=None):
        hcount = len(value) - len(value.strip('#'))

        """  On peut laisser value peut etre et passer children"""

        children = text_to_textnodes( value.strip('# '))
        super().__init__(f'h{hcount}',children=children, props=props)
    pass