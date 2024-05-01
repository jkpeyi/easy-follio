import unittest
from src.utils import text_to_textnodes , markdown_to_blocks
from src.textnode import TextNode


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_mardown_images(self):
        node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",'text')
       
       # print(split_nodes_image([node]))
       # split_nodes_image([node])


    def test_test_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        a=text_to_textnodes(text)

        #print(a)

    
    def test_markdown_to_blocks(self):
        
        with open("./src/tests/content.md",'r') as md:
           text = md.read()
           print(markdown_to_blocks(text))
           md.close()

        
# TODO: Separate test cases
        
        
    
if __name__ == "__main__":
    unittest.main()

""" TODO: Any challenges you face represent an assignment. Any bad you see you yourself playing point out to the original role you must be playing. A wish should originaly be a builder of lives. Someone perveted the role. A begger shuld be a provider. """