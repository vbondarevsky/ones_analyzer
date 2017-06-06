from syntax_kind import SyntaxKind


class Lexer(object):
    @staticmethod
    def tokenize(source):
        tokens = []

        for c in source.read():
            if c == '+':
                tokens.append((SyntaxKind.PlusToken,))
            elif c == '-':
                tokens.append((SyntaxKind.MinusToken,))
        return tokens
