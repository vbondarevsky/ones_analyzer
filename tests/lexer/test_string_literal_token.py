import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerStringLiteralToken(unittest.TestCase):
    def test_empty_string(self):
        tokens = list(Lexer(Source('""')).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.StringLiteralToken, tokens[0][0])
        self.assertEqual("", tokens[0][1])


if __name__ == '__main__':
    unittest.main()
