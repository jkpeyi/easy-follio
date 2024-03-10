import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p","cc", {"id":5, "class":"myclass"})
        
        print(node.to_html())


if __name__ == "__main__":
    unittest.main()