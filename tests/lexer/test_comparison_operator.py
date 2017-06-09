import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerComparisonOperatorToken(unittest.TestCase):
    def test_less_than_token(self):
        tokens = list(Lexer(Source("<")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.LessThanToken, tokens[0][0])

    def test_greater_than_token(self):
        tokens = list(Lexer(Source(">")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.GreaterThanToken, tokens[0][0])

    def test_equals_token(self):
        tokens = list(Lexer(Source("=")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.EqualsToken, tokens[0][0])

    def test_less_than_equals_token(self):
        tokens = list(Lexer(Source("<=")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.LessThanEqualsToken, tokens[0][0])

    def test_greater_than_equals_token(self):
        tokens = list(Lexer(Source(">=")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.GreaterThanEqualsToken, tokens[0][0])

    def test_less_than_greater_than_token(self):
        tokens = list(Lexer(Source("<>")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.LessThanGreaterThanToken, tokens[0][0])


if __name__ == '__main__':
    unittest.main()
