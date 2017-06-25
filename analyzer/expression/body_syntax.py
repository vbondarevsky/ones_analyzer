from analyzer.syntax_kind import SyntaxKind


class BodySyntax(object):
    def __init__(self, statements):
        self.kind = SyntaxKind.Body
        self.statements = statements

    def __str__(self):
        return f"{''.join(map(str, self.statements))}"
