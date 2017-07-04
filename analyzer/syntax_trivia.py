class SyntaxTrivia(object):
    def __init__(self, kind, text):
        self.kind = kind
        self.text = text

    def __str__(self):
        return f"{self.text}"
