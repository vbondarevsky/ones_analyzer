from analyzer.syntax_kind import SyntaxKind


class ParameterListSyntax(object):
    def __init__(self, open_paren, parameters, close_paren):
        self.kind = SyntaxKind.ParameterList
        self.open_paren = open_paren
        self.parameters = parameters
        self.close_paren = close_paren

    def __str__(self):
        return f"{self.open_paren}{''.join(map(str, self.parameters))}{self.close_paren}"
