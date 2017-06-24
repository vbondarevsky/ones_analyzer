import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import parse_source


class TestParserExpression(unittest.TestCase):
    def test_numeric_literal_expression(self):
        syntax_tree = parse_source("2")
        self.assertEqual(syntax_tree.kind, SyntaxKind.NumericLiteralExpression)
        self.assertEqual(syntax_tree.token.text, "2")

    def test_unary_minus_literal_expression(self):
        syntax_tree = parse_source("-2")
        self.assertEqual(syntax_tree.kind, SyntaxKind.UnaryMinusExpression)
        self.assertEqual(syntax_tree.operand.kind, SyntaxKind.NumericLiteralExpression)
        self.assertEqual(syntax_tree.operator_token.kind, SyntaxKind.MinusToken)
