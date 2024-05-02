
from src.textnode import TextNode
from src.functions.copy_r import copy_r
from src.utils.generate_page  import generate_page
from src.utils.generate_pages_recursive import generate_pages_recursive
import os
import shutil
def main():
    #text_node  = TextNode("This a link","bold","https://boot.dev")
    try:
        shutil.rmtree('./public/')
        os.mkdir('./public')
    except:
        pass

    copy_r("./static")
    #generate_page('./content/index.md','./template.html','./public/index.html')
    generate_pages_recursive('./content','template.html','./public')


if __name__=="__main__":

    main()