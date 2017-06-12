import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerWhiteSpace(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer(Source("")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[0][0])

    def test_naive_whitespace(self):
        tokens = list(Lexer(Source(" \t  \n  ")).tokenize())
        self.assertEqual(4, len(tokens))
        self.assertEqual(SyntaxKind.WhitespaceTrivia, tokens[0][0])
        self.assertEqual(SyntaxKind.EndOfLineTrivia, tokens[1][0])
        self.assertEqual(SyntaxKind.WhitespaceTrivia, tokens[2][0])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[3][0])


if __name__ == '__main__':
    unittest.main()
