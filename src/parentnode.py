from .htmlnode import HTMLNode
from .leafnode import LeafNode

from typing import List

class ParentNode(HTMLNode):

    def __init__(self, tag,  children : List[LeafNode] = [], props=None):

        if tag ==None:
            raise ValueError()
        self.tag = tag

        if len(children) == 0:
            raise ValueError('node Should have children')
        self.children = children
        
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        
        content = []

        for el in self.children:
            content.append(el.to_html())
        return f"<{self.tag}>{''.join(content)}</{self.tag}>"