import unittest
from src.utils import markdown_to_blocks , block_to_block_type
from src.type import BlockType

class TestExtractMarkdownImages(unittest.TestCase):


    def test_bloc_to_bloc_type(self):
        with open("./src/tests/content.md",'r') as md:
           
           text = md.read()
           [p1, p2, ul ]= markdown_to_blocks(text)

           self.assertEqual(block_to_block_type(ul), BlockType.ul)
           self.assertEqual(block_to_block_type(p1),BlockType.paragraph)
           self.assertEqual(block_to_block_type(p2),BlockType.paragraph)

           print(list(map(lambda i: i.strip('* ') ,filter(lambda x: x,ul.split('\n')))))

           
           md.close()

