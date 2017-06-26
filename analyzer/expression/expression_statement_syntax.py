from analyzer.syntax_kind import SyntaxKind


class ExpressionStatementSyntax(object):
    def __init__(self, expression, semicolon_token):
        self.kind = SyntaxKind.ExpressionStatement
        self.expression = expression
        self.semicolon_token = semicolon_token

    def __str__(self):
        return f"{self.expression}{self.semicolon_token}"
