import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerStringLiteralToken(unittest.TestCase):
    def test_empty_string(self):
        tokens = list(Lexer(Source('""')).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, "")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_simple_string(self):
        tokens = list(Lexer(Source('"какая-то строка"')).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'какая-то строка')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_string_with_quotation_mark(self):
        tokens = list(Lexer(Source('"какая-то ""строка"""')).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'какая-то "строка"')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_multiline_string(self):
        tokens = list(Lexer(Source('"многострочная\n|строка"')).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'многострочная\n|строка')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)


if __name__ == '__main__':
    unittest.main()
