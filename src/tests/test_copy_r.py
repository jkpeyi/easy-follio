import unittest
from src.functions.copy_r import copy_r

class TestCopyR(unittest.TestCase):

    def test_copy_r(self):
        copy_r('./static')

if __name__ == "__main__":
    unittest.main()