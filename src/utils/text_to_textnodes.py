from src.textnode import TextNode
from .split_nodes_image import  split_nodes_image 
from .split_nodes_link import split_nodes_link
from .split_node_delimiter import split_node_delimiter
from src.htmlnode import HTMLNode

def text_to_textnodes(text) -> list[HTMLNode]:

    delimiters = {
        "bold":"**",
        "italic":"*",
        "code" : "`"
    }

    nodes = [TextNode(text,'text')]

    for key in delimiters:
        nodes = split_node_delimiter(nodes,delimiters[key],key)
        
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes