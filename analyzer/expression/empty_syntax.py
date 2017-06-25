from analyzer.syntax_kind import SyntaxKind


class EmptySyntax(object):
    def __init__(self):
        self.kind = SyntaxKind.Empty

    def __str__(self):
        return ""
