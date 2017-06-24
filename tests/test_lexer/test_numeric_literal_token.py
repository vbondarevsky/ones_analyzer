import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerNumericLiteralToken(unittest.TestCase):
    def test_number_one_digit(self):
        for digit in list("0123456789"):
            with self.subTest(digit):
                tokens = list(Lexer(Source(digit)).tokenize())
                self.assertEqual(len(tokens), 2)
                self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
                self.assertEqual(tokens[0].text, digit)
                self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_many_digits(self):
        tokens = list(Lexer(Source("554433")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "554433")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_dot_number(self):
        tokens = list(Lexer(Source("3.14")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "3.14")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_number_dot_number_dot(self):
        tokens = list(Lexer(Source("3.14.")).tokenize())
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "3.14")
        self.assertEqual(tokens[1].kind, SyntaxKind.DotToken)
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)

    def test_unary_minus_number(self):
        tokens = list(Lexer(Source("-4")).tokenize())
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.MinusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[1].text, "4")
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)

    def test_unary_plus_number(self):
        tokens = list(Lexer(Source("+4")).tokenize())
        self.assertEqual(len(tokens), 3)
        self.assertEqual(tokens[0].kind, SyntaxKind.PlusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[1].text, "4")
        self.assertEqual(tokens[2].kind, SyntaxKind.EndOfFileToken)
