class CompilationUnitSyntax(object):
    def __init__(self, members):
        self.members = members

    def __str__(self):
        return f"{''.join(self.members)}"
