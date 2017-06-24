import unittest

from analyzer.lexer import UnexpectedSymbolError
from tests.utils import tokenize_source


class TestUnexpectedSymbols(unittest.TestCase):
    def test_unexpected_symbols(self):
        with self.assertRaises(UnexpectedSymbolError):
            tokenize_source("@")
