import unittest
from src.parentnode import ParentNode
from src.leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        
        node = ParentNode('div',
                          [
                              LeafNode("p","cc", {"id":5, "class":"myclass"}),
                              LeafNode(None,"Bonjour comment", {"id":5, "class":"myclass"})
                          ]
                )
        
        self.assertEqual(node.to_html(), "<div><p id=5 class='myclass' > cc </p>Bonjour comment</div>")
        
if __name__ == "__main__":
    unittest.main()