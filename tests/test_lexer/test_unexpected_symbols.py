import unittest
from io import StringIO as Source

from analyzer.lexer import UnexpectedSymbolError, Lexer


class TestUnexpectedSymbols(unittest.TestCase):
    def test_unexpected_symbols(self):
        with self.assertRaises(UnexpectedSymbolError):
            list(Lexer(Source("@")).tokenize())
