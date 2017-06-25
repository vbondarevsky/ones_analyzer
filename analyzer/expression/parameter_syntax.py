from analyzer.syntax_kind import SyntaxKind


class ParameterSyntax(object):
    def __init__(self, identifier, default):
        self.kind = SyntaxKind.Parameter
        self.identifier = identifier
        self.default = default

    def __str__(self):
        return f"{self.identifier}{self.default}"
