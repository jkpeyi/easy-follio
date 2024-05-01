from src.leafnode import LeafNode

class Quote(LeafNode):

    def __init__(self, value, props=None):
        super().__init__('blockquote', value, props)
    pass