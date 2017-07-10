from analyzer.syntax_kind import SyntaxKind


class LiteralExpressionSyntax(object):
    def __init__(self, token):
        if token.kind == SyntaxKind.NumericLiteralToken:
            self.kind = SyntaxKind.NumericLiteralExpression
        elif token.kind == SyntaxKind.StringLiteralToken:
            self.kind = SyntaxKind.StringLiteralExpression
        elif token.kind == SyntaxKind.DateLiteralToken:
            self.kind = SyntaxKind.DateLiteralExpression
        elif token.kind == SyntaxKind.NullKeyword:
            self.kind = SyntaxKind.NullLiteralExpression
        elif token.kind == SyntaxKind.UndefinedKeyword:
            self.kind = SyntaxKind.UndefinedLiteralExpression
        elif token.kind == SyntaxKind.TrueKeyword:
            self.kind = SyntaxKind.TrueLiteralExpression
        elif token.kind == SyntaxKind.FalseKeyword:
            self.kind = SyntaxKind.FalseLiteralExpression
        self.token = token

    def __str__(self):
        return f"{self.token}"
