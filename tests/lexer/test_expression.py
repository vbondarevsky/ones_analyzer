import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerExpression(unittest.TestCase):
    def test_number_plus_number_equals_number_expression(self):
        tokens = list(Lexer.tokenize(Source("2 + 3 = 5;")))
        self.assertEqual(6, len(tokens))

        self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[0][0])
        self.assertEqual("2", tokens[0][1])

        self.assertEqual(SyntaxKind.PlusToken, tokens[1][0])

        self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[2][0])
        self.assertEqual("3", tokens[2][1])

        self.assertEqual(SyntaxKind.EqualsToken, tokens[3][0])

        self.assertEqual(SyntaxKind.NumericLiteralToken, tokens[4][0])
        self.assertEqual("5", tokens[4][1])

        self.assertEqual(SyntaxKind.SemicolonToken, tokens[5][0])


if __name__ == '__main__':
    unittest.main()
