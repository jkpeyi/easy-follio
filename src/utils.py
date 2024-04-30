from typing import List
from .textnode import TextNode
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


def extract_markdown_images(text: str):
    image_tuples = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_tuples


def extract_markdown_links(text: str):
    link_tuples = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_tuples


def split_nodes_image(old_nodes: List[TextNode]):

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


def split_nodes_link(old_nodes):

    new_nodes = []
    for node in old_nodes:
        if len (extract_markdown_links(node.text)) ==0:
            new_nodes.append(node)
        else:
            new_nodes.extend(split_t(node.text, "link"))

    return new_nodes


def split_t(text:str, type):
    new_nodes = []

    tuples = (
        extract_markdown_images(text)
        if type == "image"
        else extract_markdown_links(text)
    )

    
    # re.findall(r'!\[([^\]]+)\]\(([^)]+)\)', text)

    # Replace Markdown image syntax with the URLs
    
    for alt_text, url in tuples:
       
        data = {"image": f"![{alt_text}]({url})", "link": f"[{alt_text}]({url})"}
        text = text.replace(data[type], f"_limiter_{alt_text}|{url}_limiter_")

        

    for item in text.split("_limiter_"):
        _ = item.strip().split("|")
        if len(_) > 1:
            # link with alt text

            new_nodes.append(TextNode(_[0].strip(), type, _[1].strip()))
        else:
            # simple text
            if item.strip():
                
                new_nodes.append(TextNode(item.strip(), 'text'))

    return new_nodes



def text_to_textnodes(text):

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
