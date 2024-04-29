import unittest

from src.htmlnode import HTMLNode #absolute imports


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p")
        node.props = {"id":"my-id"}
        self.assertEqual(node.props_to_html(), "id='my-id'")


if __name__ == "__main__":
    unittest.main()
