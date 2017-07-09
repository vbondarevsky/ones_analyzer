from analyzer.syntax_kind import SyntaxKind


class MethodBlockSyntax:
    def __init__(self, begin, declarations, statements, end):
        if begin.kind == SyntaxKind.FunctionStatement:
            self.kind = SyntaxKind.FunctionBlock
        else:
            self.kind = SyntaxKind.ProcedureBlock
        self.begin = begin
        self.declarations = declarations
        self.statements = statements
        self.end = end

    def __str__(self):
        to_str = lambda l: ''.join(map(str, l))
        return f"{self.begin}{to_str(self.declarations)}{to_str(self.statements)}{self.end}"
