from analyzer.syntax_kind import SyntaxKind


class VariableDeclarationSyntax(object):
    def __init__(self, var_token, variables, export_token, semicolon_token):
        self.kind = SyntaxKind.VariableDeclaration
        self.var_token = var_token
        self.variables = variables
        self.export_token = export_token
        self.semicolon_token = semicolon_token

    def __str__(self):
        return f"{self.var_token}{''.join(map(str, self.variables))}{self.export_token}{self.semicolon_token}"
