from analyzer.syntax_kind import SyntaxKind


class EqualsValueClauseSyntax(object):
    def __init__(self, equals_token, value):
        self.kind = SyntaxKind.EqualsValueClause
        self.equals_token = equals_token
        self.value = value

    def __str__(self):
        return f"{self.equals_token}{self.value}"
