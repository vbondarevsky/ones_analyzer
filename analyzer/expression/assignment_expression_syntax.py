from analyzer.syntax_kind import SyntaxKind


class AssignmentExpressionSyntax(object):
    def __init__(self, left, operator_token, right):
        self.kind = SyntaxKind.AssignmentExpression
        self.left = left
        self.operator_token = operator_token
        self.right = right

    def __str__(self):
        return f"{self.left}{self.operator_token}{self.right}"
