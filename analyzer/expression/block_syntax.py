from analyzer.syntax_kind import SyntaxKind


class BlockSyntax(object):
    def __init__(self, declarations, statements):
        self.kind = SyntaxKind.Block
        self.declarations = declarations
        self.statements = statements

    def __str__(self):
        return f"{''.join(map(str, self.declarations))}{''.join(map(str, self.statements))}"
