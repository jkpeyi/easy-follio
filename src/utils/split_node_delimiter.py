from src.textnode import TextNode
import re

def split_node_delimiter(olnodes: list[TextNode], delimiter: str, text_type: str):

    results = []
    def find_enclosed_texts(text, delimiter):

        pattern = re.compile(re.escape(delimiter) + r"(.*?)" + re.escape(delimiter))
        enclosed_texts = re.findall(pattern, text)
        return enclosed_texts

    def parseNode(node: TextNode, delimiter: str, text_type: str):
        values = node.text.split(delimiter)

        spec_texts = find_enclosed_texts(node.text, delimiter)

        

        text_nodes: list[TextNode] = []

        for value in values:
           
            if value in spec_texts:
                text_nodes.append(TextNode(value, text_type))
            elif value:
                text_nodes.append(TextNode(value, node.text_type if node.text_type else 'text'))

        return text_nodes
    

    for node in olnodes:
        results.extend(parseNode(node, delimiter, text_type))

    return results
