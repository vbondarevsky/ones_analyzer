import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerDateLiteralToken(unittest.TestCase):
    def test_empty_date(self):
        tokens = list(Lexer(Source("'00010101'")).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.DateLiteralToken, tokens[0][0])
        self.assertEqual("00010101", tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_empty_date_and_time(self):
        tokens = list(Lexer(Source("'00010101000000'")).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.DateLiteralToken, tokens[0][0])
        self.assertEqual("00010101000000", tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_not_date(self):
        tokens = list(Lexer(Source('''"ДФ=dd.MM.yyyy; ДП='Нет даты'"''')).tokenize())
        self.assertNotEqual(SyntaxKind.DateLiteralToken, tokens[0][0])


if __name__ == '__main__':
    unittest.main()
