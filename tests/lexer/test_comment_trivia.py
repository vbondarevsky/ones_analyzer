import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerSingleLineCommentTrivia(unittest.TestCase):
    def test_single_line_comment(self):
        tokens = list(Lexer(Source(r"// какой-то комментарий")).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(SyntaxKind.SingleLineCommentTrivia, tokens[0][0])
        self.assertEqual(" какой-то комментарий", tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[1][0])

    def test_multi_line_comment(self):
        tokens = list(Lexer(Source("// первая строка комментария\n// вторая строка")).tokenize())
        self.assertEqual(4, len(tokens))
        self.assertEqual(SyntaxKind.SingleLineCommentTrivia, tokens[0][0])
        self.assertEqual(" первая строка комментария", tokens[0][1])
        self.assertEqual(SyntaxKind.EndOfLineTrivia, tokens[1][0])
        self.assertEqual(SyntaxKind.SingleLineCommentTrivia, tokens[2][0])
        self.assertEqual(" вторая строка", tokens[2][1])
        self.assertEqual(SyntaxKind.EndOfFileToken, tokens[3][0])

if __name__ == '__main__':
    unittest.main()
