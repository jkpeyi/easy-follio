from .extract_markdown_links import extract_markdown_links
from .split_t import split_t

def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if len (extract_markdown_links(node.text)) ==0:
            new_nodes.append(node)
        else:
            new_nodes.extend(split_t(node.text, "link"))

    return new_nodes
