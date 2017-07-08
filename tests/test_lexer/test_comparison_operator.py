from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerComparisonOperatorToken(TestCaseLexer):
    def test_less_than_token(self):
        self.tokenize_source("<", 2)
        self.assertToken(0, SyntaxKind.LessThanToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_greater_than_token(self):
        self.tokenize_source(">", 2)
        self.assertToken(0, SyntaxKind.GreaterThanToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_equals_token(self):
        self.tokenize_source("=", 2)
        self.assertToken(0, SyntaxKind.EqualsToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_less_than_equals_token(self):
        self.tokenize_source("<=", 2)
        self.assertToken(0, SyntaxKind.LessThanEqualsToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_greater_than_equals_token(self):
        self.tokenize_source(">=", 2)
        self.assertToken(0, SyntaxKind.GreaterThanEqualsToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_less_than_greater_than_token(self):
        self.tokenize_source("<>", 2)
        self.assertToken(0, SyntaxKind.LessThanGreaterThanToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])
