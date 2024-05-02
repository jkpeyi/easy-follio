from .markdown_to_html_node import markdown_to_html_node
from .extract_title import extract_title

def generate_page(from_path, template_path, dest_path):

    print(f"Gerating page from {from_path} to {dest_path} using {template_path}")

    markdown = None
    with open(from_path) as md:
        markdown = md.read()
        md.close()

    html_template = None
    with open(template_path) as html:
        html_template = html.read()
        html.close()

    html_content = markdown_to_html_node(markdown).to_html()
    page_title = extract_title(markdown)
    html_template=html_template.replace("{{ Title }}", page_title)
    html_template = html_template.replace("{{ Content }}", html_content)

    with open(dest_path, 'w') as output:

        output.write(html_template)
    
    pass

