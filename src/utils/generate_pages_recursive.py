import os
import pathlib
from .generate_page import generate_page


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    contents = list(reversed(os.listdir(dir_path_content)))
   
    
    for content in contents:
       
        abs_dir_path_content = os.path.join(dir_path_content, content)

        if os.path.isfile(abs_dir_path_content):
            abs_dest_dir_path = os.path.join(
                dest_dir_path, content.replace('.md', '.html')
            )
        
            generate_page(abs_dir_path_content, template_path, abs_dest_dir_path)
        else:

            dir_path_content = os.path.join(dir_path_content, content)
            dest_dir_path = os.path.join(dest_dir_path, content)
            if not os.path.exists(dest_dir_path):
                os.mkdir(dest_dir_path)
        
            generate_pages_recursive(dir_path_content, template_path, dest_dir_path)
