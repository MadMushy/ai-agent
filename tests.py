# tests.py

import unittest
from functions.get_files_info import get_file_content
from functions.config import *


class Testget_file_content(unittest.TestCase):

    def test_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_pkg(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

    def test_non_exsist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)

if __name__ == "__main__":
    unittest.main()
