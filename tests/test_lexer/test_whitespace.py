from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerWhiteSpace(TestCaseLexer):
    def test_empty(self):
        self.tokenize_source("", 1)
        self.check_token(0, SyntaxKind.EndOfFileToken, [], [])

    def test_naive_whitespace(self):
        self.tokenize_source(" \t  \n  ", 1)
        self.check_token(0, SyntaxKind.EndOfFileToken, [SyntaxKind.WhitespaceTrivia,
                                                        SyntaxKind.EndOfLineTrivia,
                                                        SyntaxKind.WhitespaceTrivia], [])
