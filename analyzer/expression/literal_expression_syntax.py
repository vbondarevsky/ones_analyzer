class LiteralExpressionSyntax(object):
    def __init__(self, kind, token):
        self.kind = kind
        self.token = token

    def __str__(self):
        return f"{self.token.text}"
