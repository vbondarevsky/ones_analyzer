class SyntaxToken(object):
    def __init__(self, kind, text, leading_trivia=[], trailing_trivia=[]):
        self.kind = kind
        self.text = text
        self.leading_trivia = leading_trivia
        self.trailing_trivia = trailing_trivia

    def __str__(self):
        return f"{''.join(map(str, self.leading_trivia))}{self.text}{''.join(map(str, self.trailing_trivia))}"
