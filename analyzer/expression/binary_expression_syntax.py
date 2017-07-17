from analyzer.syntax_kind import SyntaxKind


class BinaryExpressionSyntax(object):
    def __init__(self, left, operator_token, right):
        if operator_token.kind == SyntaxKind.MinusToken:
            self.kind = SyntaxKind.SubtractExpression
        elif operator_token.kind == SyntaxKind.PlusToken:
            self.kind = SyntaxKind.AddExpression
        elif operator_token.kind == SyntaxKind.AsteriskToken:
            self.kind = SyntaxKind.MultiplyExpression
        elif operator_token.kind == SyntaxKind.SlashToken:
            self.kind = SyntaxKind.DivideExpression
        elif operator_token.kind == SyntaxKind.PercentToken:
            self.kind = SyntaxKind.ModuloExpression
        self.left = left
        self.operator_token = operator_token
        self.right = right

    def __str__(self):
        return f"{self.left}{self.operator_token}{self.right}"
