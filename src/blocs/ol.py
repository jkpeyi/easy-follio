from .__listnode import ListNode


class Ol(ListNode):

    def __init__(self, value: str, props=None):

        super().__init__("ol", value, props)

    
