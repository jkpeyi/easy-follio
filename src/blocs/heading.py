from src.htmlnode import HTMLNode

class Heading(HTMLNode):

    def __init__(self, value, props=None):
        hcount = len(value) - len(value.strip('#'))

        """  On peut laisser value peut etre et passer children"""
        super().__init__(f'h{hcount}', value.strip('# '), props=props)
    pass