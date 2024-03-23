import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        
        node = ParentNode('div',
                          [
                              LeafNode("p","cc", {"id":5, "class":"myclass"}),
                              LeafNode(None,"Bonjour comment", {"id":5, "class":"myclass"})
                          ]
                )
        
        print(node.to_html())
        
if __name__ == "__main__":
    unittest.main()