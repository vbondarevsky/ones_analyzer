import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerExpression(unittest.TestCase):
    def test_number_plus_number_equals_number_expression(self):
        tokens = list(Lexer(Source("2+3=5;")).tokenize())
        self.assertEqual(len(tokens), 7)

        self.assertEqual(tokens[0].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[0].text, "2")

        self.assertEqual(tokens[1].kind, SyntaxKind.PlusToken)

        self.assertEqual(tokens[2].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[2].text, "3")

        self.assertEqual(tokens[3].kind, SyntaxKind.EqualsToken)

        self.assertEqual(tokens[4].kind, SyntaxKind.NumericLiteralToken)
        self.assertEqual(tokens[4].text, "5")

        self.assertEqual(tokens[5].kind, SyntaxKind.SemicolonToken)
        self.assertEqual(tokens[6].kind, SyntaxKind.EndOfFileToken)


if __name__ == '__main__':
    unittest.main()
