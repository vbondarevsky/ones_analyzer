from analyzer.syntax_kind import SyntaxKind


class MemberAccessExpressionSyntax(object):
    def __init__(self, expression, operator_token, name):
        self.kind = SyntaxKind.MemberAccessExpression
        self.expression = expression
        self.operator_token = operator_token
        self.name = name

    def __str__(self):
        return f"{self.expression}{self.operator_token}{self.name}"
