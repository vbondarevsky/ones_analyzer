import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer


class TestLexerSingleLineCommentTrivia(unittest.TestCase):
    def test_single_line_comment(self):
        tokens = list(Lexer(Source(r"// какой-то комментарий")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(" какой-то комментарий", tokens[0][1])

    def test_multi_line_comment(self):
        tokens = list(Lexer(Source("// первая строка комментария\n// вторая строка")).tokenize())
        self.assertEqual(2, len(tokens))
        self.assertEqual(" первая строка комментария", tokens[0][1])
        self.assertEqual(" вторая строка", tokens[1][1])


if __name__ == '__main__':
    unittest.main()
