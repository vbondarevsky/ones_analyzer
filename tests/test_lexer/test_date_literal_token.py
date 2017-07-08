from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerDateLiteralToken(TestCaseLexer):
    def test_empty_date(self):
        self.tokenize_source("'00010101'", 2)
        self.assertToken(0, SyntaxKind.DateLiteralToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_empty_date_and_time(self):
        self.tokenize_source("'00010101000000'", 2)
        self.assertToken(0, SyntaxKind.DateLiteralToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_not_date(self):
        self.tokenize_source('''"ДФ=dd.MM.yyyy; ДП='Нет даты'"''', 2)
        self.assertToken(0, SyntaxKind.StringLiteralToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])
