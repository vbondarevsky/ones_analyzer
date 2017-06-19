import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerDateLiteralToken(unittest.TestCase):
    def test_empty_date(self):
        tokens = list(Lexer(Source("'00010101'")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)
        self.assertEqual(tokens[0].text, "00010101")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_empty_date_and_time(self):
        tokens = list(Lexer(Source("'00010101000000'")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)
        self.assertEqual(tokens[0].text, "00010101000000")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_not_date(self):
        tokens = list(Lexer(Source('''"ДФ=dd.MM.yyyy; ДП='Нет даты'"''')).tokenize())
        self.assertNotEqual(tokens[0].kind, SyntaxKind.DateLiteralToken)


if __name__ == '__main__':
    unittest.main()
