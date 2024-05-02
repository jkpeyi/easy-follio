import unittest
from src.utils.extract_title import extract_title
class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):

        with open("./src/tests/content.md",'r') as md:

            text = md.read()

            print(extract_title(text))
