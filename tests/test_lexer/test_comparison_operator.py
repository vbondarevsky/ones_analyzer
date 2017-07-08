from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerComparisonOperatorToken(TestCaseLexer):
    def test_less_than_token(self):
        self.tokenize_source("<", 2)
        self.check_token(0, SyntaxKind.LessThanToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_greater_than_token(self):
        self.tokenize_source(">", 2)
        self.check_token(0, SyntaxKind.GreaterThanToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_equals_token(self):
        self.tokenize_source("=", 2)
        self.check_token(0, SyntaxKind.EqualsToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_less_than_equals_token(self):
        self.tokenize_source("<=", 2)
        self.check_token(0, SyntaxKind.LessThanEqualsToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_greater_than_equals_token(self):
        self.tokenize_source(">=", 2)
        self.check_token(0, SyntaxKind.GreaterThanEqualsToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_less_than_greater_than_token(self):
        self.tokenize_source("<>", 2)
        self.check_token(0, SyntaxKind.LessThanGreaterThanToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])
