from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerExpression(TestCaseLexer):
    def test_number_plus_number_equals_number_expression(self):
        self.tokenize_source("2+3=5;", 7)
        self.check_token(0, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(1, SyntaxKind.PlusToken, [], [])
        self.check_token(2, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(3, SyntaxKind.EqualsToken, [], [])
        self.check_token(4, SyntaxKind.NumericLiteralToken, [], [])
        self.check_token(5, SyntaxKind.SemicolonToken, [], [])
        self.check_token(6, SyntaxKind.EndOfFileToken, [], [])
