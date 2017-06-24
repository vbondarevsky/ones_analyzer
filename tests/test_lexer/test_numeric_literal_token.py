import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerNumericLiteralToken(unittest.TestCase):
    def test_number_one_digit(self):
        for digit in list("0123456789"):
            with self.subTest(digit):
                tokens = tokenize_source(digit)
                self.assertEqual(len(tokens), 2)
                self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
                self.assertEqual(tokens[0].text, digit)
                self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_many_digits(self):
        tokens = tokenize_source("554433")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "554433")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_dot_number(self):
        tokens = tokenize_source("3.14")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "3.14")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_dot_number_dot(self):
        tokens = tokenize_source("3.14.")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "3.14")
        self.assertEqual(tokens[1].kind, SyntaxKind.DotToken)
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)

    def test_unary_minus_number(self):
        tokens = tokenize_source("-4")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.MinusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[1].text, "4")
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)

    def test_unary_plus_number(self):
        tokens = tokenize_source("+4")
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.PlusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[1].text, "4")
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)
