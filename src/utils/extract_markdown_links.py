import re

def extract_markdown_links(text: str):
    link_tuples = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return link_tuples