import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerStringLiteralToken(unittest.TestCase):
    def test_empty_string(self):
        tokens = list(Lexer(Source('""')).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.StringLiteralToken, tokens[0][0])
        self.assertEqual("", tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_simple_string(self):
        tokens = list(Lexer(Source('"какая-то строка"')).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.StringLiteralToken, tokens[0][0])
        self.assertEqual('какая-то строка', tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_string_with_quotation_mark(self):
        tokens = list(Lexer(Source('"какая-то ""строка"""')).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.StringLiteralToken, tokens[0][0])
        self.assertEqual('какая-то "строка"', tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_multiline_string(self):
        tokens = list(Lexer(Source('"многострочная\n|строка"')).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.StringLiteralToken, tokens[0][0])
        self.assertEqual('многострочная\n|строка', tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])


if __name__ == '__main__':
    unittest.main()
