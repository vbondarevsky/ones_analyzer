import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import parse_source


class TestParserExpression(unittest.TestCase):
    def test_numeric_literal_expression(self):
        syntax_tree = parse_source("2")
        self.assertEqual(len(syntax_tree.body.statements), 1)
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.NumericLiteralExpression)

    def test_unary_minus_literal_expression(self):
        syntax_tree = parse_source("-2")
        self.assertEqual(len(syntax_tree.body.statements), 1)
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.UnaryMinusExpression)
        self.assertEqual(syntax_tree.body.statements[0].operator_token.kind, SyntaxKind.MinusToken)

    def test_unary_plus_literal_expression(self):
        syntax_tree = parse_source("+2")
        self.assertEqual(len(syntax_tree.body.statements), 1)
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.UnaryPlusExpression)
        self.assertEqual(syntax_tree.body.statements[0].operator_token.kind, SyntaxKind.PlusToken)
