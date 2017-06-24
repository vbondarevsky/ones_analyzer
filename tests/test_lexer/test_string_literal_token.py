import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerStringLiteralToken(unittest.TestCase):
    def test_empty_string(self):
        tokens = tokenize_source('""')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, "")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_simple_string(self):
        tokens = tokenize_source('"какая-то строка"')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'какая-то строка')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_string_with_quotation_mark(self):
        tokens = tokenize_source('"какая-то ""строка"""')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'какая-то "строка"')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_multiline_string(self):
        tokens = tokenize_source('"многострочная\n|строка"')
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.StringLiteralToken)
        self.assertEqual(tokens[0].text, 'многострочная\n|строка')
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)
