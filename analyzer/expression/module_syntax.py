from analyzer.syntax_kind import SyntaxKind


class ModuleSyntax(object):
    def __init__(self, declarations, methods, body, end_of_file_token):
        self.kind = SyntaxKind.Module
        self.declarations = declarations
        self.methods = methods
        self.body = body
        self.end_of_file_token = end_of_file_token

    def __str__(self):
        return f"{''.join(map(str, self.declarations))}"
