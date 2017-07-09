from analyzer.syntax_kind import SyntaxKind


class MethodStatementSyntax:
    def __init__(self, declaration_keyword, identifier, parameter_list, export):
        if declaration_keyword.kind == SyntaxKind.FunctionKeyword:
            self.kind = SyntaxKind.FunctionStatement
        else:
            self.kind = SyntaxKind.ProcedureStatement
        self.declaration_keyword = declaration_keyword
        self.identifier = identifier
        self.parameter_list = parameter_list
        self.export = export

    def __str__(self):
        return f"{self.declaration_keyword}{self.identifier}{self.parameter_list}{self.export}"
