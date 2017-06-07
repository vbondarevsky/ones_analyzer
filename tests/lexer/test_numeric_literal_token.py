import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerNumericLiteralToken(unittest.TestCase):
    def test_number_one_digit(self):
        for digit in list("0123456789"):
            with self.subTest(digit):
                tokens = list(Lexer.tokenize(Source(digit)))
                self.assertEqual(1, len(tokens))
                self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[0][0])
                self.assertEqual(digit, tokens[0][1])

    def test_number_many_digits(self):
        tokens = list(Lexer.tokenize(Source("554433")))
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[0][0])
        self.assertEqual("554433", tokens[0][1])

    def test_number_dot_number(self):
        tokens = list(Lexer.tokenize(Source("3.14")))
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[0][0])
        self.assertEqual("3.14", tokens[0][1])


if __name__ == '__main__':
    unittest.main()
