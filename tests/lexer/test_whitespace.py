import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer


class TestLexerWhiteSpace(unittest.TestCase):
    def test_naive_whitespace(self):
        tokens = list(Lexer(Source("   \n  ")).tokenize())
        self.assertEqual(0, len(tokens))


if __name__ == '__main__':
    unittest.main()
