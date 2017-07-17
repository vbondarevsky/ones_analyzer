from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserExpressionStatement(TestCaseParser):
    def test_two_expression(self):
        self.parse_source("A=3;B=4")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement, SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.AssignmentExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.SemicolonToken)

        self.assertNode(self.syntax_tree.statements[1].expression, SyntaxKind.AssignmentExpression)
        self.assertNode(self.syntax_tree.statements[1].expression.left, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.statements[1].expression.operator_token, SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.statements[1].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[1].semicolon_token, SyntaxKind.Empty)

    def test_unary_minus(self):
        self.parse_source("-2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.UnaryMinusExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.MinusToken)
        self.assertNode(self.syntax_tree.statements[0].expression.operand, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_unary_plus(self):
        self.parse_source("+2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.UnaryPlusExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.PlusToken)
        self.assertNode(self.syntax_tree.statements[0].expression.operand, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_add_expression(self):
        self.parse_source("3+2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.AddExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.PlusToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_subtract_expression(self):
        self.parse_source("3-2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.SubtractExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.MinusToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_multiply_expression(self):
        self.parse_source("3*2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.MultiplyExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.AsteriskToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_divide_expression(self):
        self.parse_source("3/2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.DivideExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.SlashToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_modulo_expression(self):
        self.parse_source("3%2")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.ModuloExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.left, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.operator_token, SyntaxKind.PercentToken)
        self.assertNode(self.syntax_tree.statements[0].expression.right, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)

    def test_parenthesized_expression(self):
        self.parse_source("(3+2)")
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].expression, SyntaxKind.ParenthesizedExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.open_paren_token, SyntaxKind.OpenParenToken)
        self.assertNode(self.syntax_tree.statements[0].expression.expression, SyntaxKind.AddExpression)
        self.assertNode(self.syntax_tree.statements[0].expression.close_paren_token, SyntaxKind.CloseParenToken)
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.Empty)
