class HTMLNode():
    def __init__(self,tag, value = None, children=None , props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        trans_list = []
        if self.props is None:
            return ""
        
        for key in self.props:
            
            trans_list.append(f"{key}='{self.props[key]}'")
        
        return " ".join(trans_list)
    
    def __repr__(self) -> str:
        
        return f"HTMLNode({self.tag}, {self.value}, {self.children} , {self.props})"

    
