from .extract_markdown_images import extract_markdown_images
from .split_t import  split_t

from src.textnode import TextNode

def split_nodes_image(old_nodes: list[TextNode]):

    new_nodes = []
    for node in old_nodes:
        img_tuples = extract_markdown_images(node.text)

        if len(img_tuples)>0:
            result = split_t(node.text, "image")
            #print(result)
            new_nodes.extend(result)
        else:
            new_nodes.append(node)

    return new_nodes

