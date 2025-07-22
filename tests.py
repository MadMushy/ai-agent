# tests.py

import unittest
from functions.get_files_info import run_python_file
from functions.config import *


class Testget_file_content(unittest.TestCase):

    def test_1(self):
        result = run_python_file("calculator", "main.py")
        print(result)

    def test_2(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)

    def test_3(self):
        result = run_python_file("calculator", "tests.py")
        print(result)

    def test_4(self):
        result = run_python_file("calculator", "../main.py")
        print(result)

    def test_5(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)


if __name__ == "__main__":
    unittest.main()
