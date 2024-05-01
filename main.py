
from src.textnode import TextNode
from src.functions.copy_r import copy_r
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

if __name__=="__main__":

    main()