from .extract_markdown_links import extract_markdown_links 
from .extract_markdown_images import extract_markdown_images
from src.textnode import TextNode

def split_t(text:str, type):
    new_nodes = []

    tuples = (
        extract_markdown_images(text)
        if type == "image"
        else extract_markdown_links(text)
    )

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

