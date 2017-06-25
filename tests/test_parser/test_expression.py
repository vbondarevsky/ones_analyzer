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

    def test_add_expression(self):
        syntax_tree = parse_source("8+2")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.AddExpression)
        self.assertEqual(syntax_tree.body.statements[0].left.token.text, "8")
        self.assertEqual(syntax_tree.body.statements[0].operator_token.text, "+")
        self.assertEqual(syntax_tree.body.statements[0].right.token.text, "2")

    def test_subtract_expression(self):
        syntax_tree = parse_source("8-2")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.SubtractExpression)
        self.assertEqual(syntax_tree.body.statements[0].left.token.text, "8")
        self.assertEqual(syntax_tree.body.statements[0].operator_token.text, "-")
        self.assertEqual(syntax_tree.body.statements[0].right.token.text, "2")

    def test_multiply_expression(self):
        syntax_tree = parse_source("8*2")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.MultiplyExpression)
        self.assertEqual(syntax_tree.body.statements[0].left.token.text, "8")
        self.assertEqual(syntax_tree.body.statements[0].operator_token.text, "*")
        self.assertEqual(syntax_tree.body.statements[0].right.token.text, "2")

    def test_divide_expression(self):
        syntax_tree = parse_source("8/2")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.DivideExpression)
        self.assertEqual(syntax_tree.body.statements[0].left.token.text, "8")
        self.assertEqual(syntax_tree.body.statements[0].operator_token.text, "/")
        self.assertEqual(syntax_tree.body.statements[0].right.token.text, "2")

    def test_parenthesized_expression(self):
        syntax_tree = parse_source("(2+3)")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.ParenthesizedExpression)
        self.assertEqual(syntax_tree.body.statements[0].open_paren_token.kind, SyntaxKind.OpenParenToken)
        self.assertEqual(str(syntax_tree.body.statements[0].expression), "2+3")
        self.assertEqual(syntax_tree.body.statements[0].close_paren_token.kind, SyntaxKind.CloseParenToken)
