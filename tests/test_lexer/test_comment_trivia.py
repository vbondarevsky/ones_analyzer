import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerSingleLineCommentTrivia(unittest.TestCase):
    def test_single_line_comment(self):
        tokens = list(Lexer(Source(r"// какой-то комментарий")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[0].text, " какой-то комментарий")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_multi_line_comment(self):
        tokens = list(Lexer(Source("// первая строка комментария\n// вторая строка")).tokenize())
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[0].text, " первая строка комментария")
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfLineTrivia)
        self.assertEqual(tokens[2].kind, SyntaxKind.SingleLineCommentTrivia)
        self.assertEqual(tokens[2].text, " вторая строка")
        self.assertEqual(tokens[3].kind, SyntaxKind.EndOfFileToken)


if __name__ == '__main__':
    unittest.main()
