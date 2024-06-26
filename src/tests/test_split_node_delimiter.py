import unittest

from src import TextNode, ParentNode , utils  # I'm learning a lot here


class TestUtilsFunctions(unittest.TestCase):

    def test_split_node_delimiter(self):

        node = TextNode("This is **a text** node and a `code snipet`", "text")
        node2 = TextNode("This is a text node", "bold")
        
        nodes=utils.split_node_delimiter([node],'**','bold')

        nodes = utils.split_node_delimiter(nodes,'`', 'code')
        print(nodes)

if __name__ == "__main__":
    unittest.main()