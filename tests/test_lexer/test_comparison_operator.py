import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerComparisonOperatorToken(unittest.TestCase):
    def test_less_than_token(self):
        tokens = tokenize_source("<")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_greater_than_token(self):
        tokens = tokenize_source(">")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.GreaterThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_equals_token(self):
        tokens = tokenize_source("=")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.EqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_less_than_equals_token(self):
        tokens = tokenize_source("<=")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanEqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_greater_than_equals_token(self):
        tokens = tokenize_source(">=")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.GreaterThanEqualsToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_less_than_greater_than_token(self):
        tokens = tokenize_source("<>")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.LessThanGreaterThanToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)
