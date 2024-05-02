from .__listnode import ListNode
import re

class Ol(ListNode):

    def __init__(self, value: str, props=None):

        pattern = r'\b\d+\.\s'
        value = re.sub(pattern,'',value)
        super().__init__("ol", value, props)

    
