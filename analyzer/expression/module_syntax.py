from analyzer.syntax_kind import SyntaxKind


class ModuleSyntax:
    def __init__(self, declarations, methods, statements, end_of_file_token):
        self.kind = SyntaxKind.Module
        self.declarations = declarations
        self.methods = methods
        self.statements = statements
        self.end_of_file_token = end_of_file_token

    def __str__(self):
        to_str = lambda l: ''.join(map(str, l))
        return f"{to_str(self.declarations)}{to_str(self.methods)}{to_str(self.statements)}"
