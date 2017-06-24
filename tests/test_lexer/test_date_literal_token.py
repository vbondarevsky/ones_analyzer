import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerDateLiteralToken(unittest.TestCase):
    def test_empty_date(self):
        tokens = tokenize_source("'00010101'")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)
        self.assertEqual(tokens[0].text, "00010101")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_empty_date_and_time(self):
        tokens = tokenize_source("'00010101000000'")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)
        self.assertEqual(tokens[0].text, "00010101000000")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_not_date(self):
        tokens = tokenize_source('''"ДФ=dd.MM.yyyy; ДП='Нет даты'"''')
        self.assertNotEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)
