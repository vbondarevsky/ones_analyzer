import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.parser import Parser
from analyzer.syntax_kind import SyntaxKind


class TestParserExpression(unittest.TestCase):
    def test_numeric_literal_expression(self):
        lexer = Lexer(Source("2")).tokenize()
        parser = Parser(lexer)
        node = parser.parse()
        self.assertEqual(node.kind, SyntaxKind.NumericLiteralExpression)
        self.assertEqual(node.token.text, "2")


if __name__ == '__main__':
    unittest.main()
