import re

def extract_markdown_images(text: str):
    image_tuples = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return image_tuples
