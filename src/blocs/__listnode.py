from src.htmlnode import HTMLNode
from src.utils import text_to_textnodes


class ListNode(HTMLNode):

    def __init__(self,tag, value: str, props=None):

        items = list(
            map(lambda i: i.strip("* "), filter(lambda x: x, value.split("\n")))
        )
        children = list(map(
            lambda item: HTMLNode("li", children=text_to_textnodes(item)), items
        ))

        super().__init__(tag, children = children, props= props)

    
