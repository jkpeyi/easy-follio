import unittest
from src.utils import markdown_to_html_node

class TestMarkDownToHtmlNode(unittest.TestCase):

    def test_markdown_to_html_node(self):

        with open("./src/tests/content.md",'r') as md:
           
           text = md.read()
           print(markdown_to_html_node(text).to_html())