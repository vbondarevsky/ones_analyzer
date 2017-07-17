from analyzer.syntax_kind import SyntaxKind


class ParenthesizedExpressionSyntax(object):
    def __init__(self, open_paren_token, expression, close_paren_token):
        self.kind = SyntaxKind.ParenthesizedExpression
        self.open_paren_token = open_paren_token
        self.expression = expression
        self.close_paren_token = close_paren_token

    def __str__(self):
        return f"{self.open_paren_token}{self.expression}{self.close_paren_token}"
