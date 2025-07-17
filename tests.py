# tests.py

import unittest
from functions.get_files_info import get_files_info


class Testget_files_info(unittest.TestCase):

    def test_current(self):
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        print(result)
        print("")

    def test_pkg(self):
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)

    def test_bin(self):
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)

    def test_slash(self):
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)

if __name__ == "__main__":
    unittest.main()
