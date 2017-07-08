from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerStringLiteralToken(TestCaseLexer):
    def test_empty_string(self):
        self.tokenize_source('""', 2)
        self.check_token(0, SyntaxKind.StringLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_simple_string(self):
        self.tokenize_source('"какая-то строка"', 2)
        self.check_token(0, SyntaxKind.StringLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_string_with_quotation_mark(self):
        self.tokenize_source('"какая-то ""строка"""', 2)
        self.check_token(0, SyntaxKind.StringLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_multiline_string(self):
        self.tokenize_source('"многострочная\n|строка"', 2)
        self.check_token(0, SyntaxKind.StringLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])
