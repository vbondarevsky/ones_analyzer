import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerComparisonOperatorToken(unittest.TestCase):
    def test_less_than_token(self):
        tokens = list(Lexer(Source("<")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_greater_than_token(self):
        tokens = list(Lexer(Source(">")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.GreaterThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_equals_token(self):
        tokens = list(Lexer(Source("=")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.EqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_less_than_equals_token(self):
        tokens = list(Lexer(Source("<=")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanEqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_greater_than_equals_token(self):
        tokens = list(Lexer(Source(">=")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.GreaterThanEqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_less_than_greater_than_token(self):
        tokens = list(Lexer(Source("<>")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanGreaterThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)


if __name__ == '__main__':
    unittest.main()
