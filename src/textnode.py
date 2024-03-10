class TextNode():

    def __init__(self,text, text_type, url=None):

        self.text = text
        self.text_type=text_type
        self.url= url

    
    def __eq__(self, other) -> bool:
        return (self.text , self.text_type , self.url) == (other.text, other.text_type, other.url)
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"