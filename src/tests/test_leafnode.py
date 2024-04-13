import unittest

from src.leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        
        node = LeafNode("p","cc", {"id":5, "class":"myclass"})
        node2 = LeafNode(None,"cc", {"id":5, "class":"myclass"})

        self.assertEqual(node.to_html(),"<p id=5 class='myclass' > cc </p>")
        self.assertEqual(node2.to_html(),'cc')


if __name__ == "__main__":
    unittest.main()