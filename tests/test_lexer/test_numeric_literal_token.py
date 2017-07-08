from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerNumericLiteralToken(TestCaseLexer):
    def test_number_one_digit(self):
        for digit in list("0123456789"):
            with self.subTest(digit):
                self.tokenize_source(digit, 2)
                self.check_token(0, SyntaxKind.NumericLiteralToken, [], [])
                self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_number_many_digits(self):
        self.tokenize_source("554433", 2)
        self.check_token(0, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_number_dot_number(self):
        self.tokenize_source("3.14", 2)
        self.check_token(0, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_number_dot_number_dot(self):
        self.tokenize_source("3.14.", 3)
        self.check_token(0, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(1, SyntaxKind.DotToken, [], [])
        self.check_token(2, SyntaxKind.EndOfFileToken, [], [])

    def test_unary_minus_number(self):
        self.tokenize_source("-4", 3)
        self.check_token(0, SyntaxKind.MinusToken, [], [])
        self.check_token(1, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(2, SyntaxKind.EndOfFileToken, [], [])

    def test_unary_plus_number(self):
        self.tokenize_source("+4", 3)
        self.check_token(0, SyntaxKind.PlusToken, [], [])
        self.check_token(1, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(2, SyntaxKind.EndOfFileToken, [], [])
