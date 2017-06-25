from analyzer.syntax_kind import SyntaxKind


class ReturnStatementSyntax(object):
    def __init__(self, return_keyword, expression, semicolon_token):
        self.kind = SyntaxKind.ReturnStatement
        self.return_keyword = return_keyword
        self.expression = expression
        self.semicolon_token = semicolon_token

    def __str__(self):
        return f"{self.return_keyword}{self.expression}{self.semicolon_token}"
