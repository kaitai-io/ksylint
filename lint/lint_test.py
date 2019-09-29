import unittest
import os
import os.path as path
from lint import lint


class TestValidation(unittest.TestCase):
    def test_valid(self):
        for file in os.listdir(path.join("test", "valid")):
            with self.subTest():
                ret_code = lint.lint_file(path.join("test", "valid", file))
                self.assertTrue(ret_code == 0, file)

    def test_invalid(self):
        for file in os.listdir(path.join("test", "invalid")):
            with self.subTest():
                ret_code = lint.lint_file(path.join("test", "invalid", file))
                self.assertTrue(ret_code > 0, file)
