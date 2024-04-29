import unittest
from src.utils import *


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_mardown_images(self):
        node = TextNode(
        "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",'text')
       
        print(split_nodes_image([node]))
       # split_nodes_image([node])


if __name__ == "__main__":
    unittest.main()

""" TODO: Any challenges you face represent an assignment. Any bad you see you yourself playing point out to the original role you must be playing. A wish should originaly be a builder of lives. Someone perveted the role. A begger shuld be a provider. """