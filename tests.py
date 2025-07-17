# tests.py

import unittest
from functions.get_files_info import get_file_content
from functions.config import *


class Testget_file_content(unittest.TestCase):

    def test_current(self):
        result = get_file_content("calculator", "lorem.txt")
        print(result)

if __name__ == "__main__":
    unittest.main()
