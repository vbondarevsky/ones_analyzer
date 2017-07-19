from analyzer.syntax_kind import SyntaxKind


class IdentifierNameSyntax(object):
    def __init__(self, identifier):
        self.kind = SyntaxKind.IdentifierName
        self.identifier = identifier

    def __str__(self):
        return f"{self.identifier}"
