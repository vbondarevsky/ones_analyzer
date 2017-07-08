from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerSingleLineCommentTrivia(TestCaseLexer):
    def test_single_line_comment(self):
        self.tokenize_source("// какой-то комментарий", 1)
        self.assertToken(0, SyntaxKind.EndOfFileToken, [SyntaxKind.SingleLineCommentTrivia], [])

    def test_multi_line_comment(self):
        self.tokenize_source("// первая строка комментария\n// вторая строка", 1)
        self.assertToken(0, SyntaxKind.EndOfFileToken, [SyntaxKind.SingleLineCommentTrivia,
                                                        SyntaxKind.EndOfLineTrivia,
                                                        SyntaxKind.SingleLineCommentTrivia], [])
