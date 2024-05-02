
from src.textnode import TextNode
from src.functions.copy_r import copy_r
from src.utils.generate_page  import generate_page

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
    generate_page('./content/index.md','./template.html','./public/index.html')


if __name__=="__main__":

    main()