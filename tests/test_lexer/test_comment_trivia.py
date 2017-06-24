import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerSingleLineCommentTrivia(unittest.TestCase):
    def test_single_line_comment(self):
        tokens = tokenize_source(r"// какой-то комментарий")
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[0].text, " какой-то комментарий")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_multi_line_comment(self):
        tokens = tokenize_source("// первая строка комментария\n// вторая строка")
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[0].text, " первая строка комментария")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfLineTrivia)
        self.assertEqual(tokens[2].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[2].text, " вторая строка")
        self.assertEqual(tokens[3].kind, SyntaxKind.EndOfFileToken)
