from leafnode import LeafNode
class TextNode():

    def __init__(self,text, text_type, url=None):

        self.text = text
        self.text_type=text_type
        self.url= url

    
    def __eq__(self, other) -> bool:
        return (self.text , self.text_type , self.url) == (other.text, other.text_type, other.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        convObj={
          "text" : LeafNode(None, self.text),
          "bold" : LeafNode('b',self.text),
          "italic" : LeafNode("i", self.text),
          "code" :LeafNode("code",self.text),
          "link": LeafNode("a",self.text, {"href":""}),
          "image": LeafNode("img", "", {"href":"", "alt":self.text})
        }
        
        if self.text_type not in convObj:
            raise Exception('Not a known text type')
        
        return convObj[self.text_type]