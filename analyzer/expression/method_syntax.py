from analyzer.syntax_kind import SyntaxKind


class MethodSyntax(object):
    def __init__(self, begin, identifier, parameter_list, export, block, end):
        if begin.kind == SyntaxKind.FunctionKeyword:
            self.kind = SyntaxKind.Function
        else:
            self.kind = SyntaxKind.Procedure
        self.begin = begin
        self.identifier = identifier
        self.parameter_list = parameter_list
        self.export = export
        self.block = block
        self.end = end

    def __str__(self):
        return f"{self.begin}{self.identifier}{''.join(map(str, self.parameter_list))}{self.export}{self.end}"
