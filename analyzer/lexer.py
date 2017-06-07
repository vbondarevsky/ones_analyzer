from analyzer.syntax_kind import SyntaxKind


class Lexer(object):
    @staticmethod
    def tokenize(source):
        c = None
        while True:
            if c is None:
                c = source.read(1)

            if c == '':
                return

            if c == '~':
                yield (SyntaxKind.TildeToken,)
            elif c == '%':
                yield (SyntaxKind.PercentToken,)
            elif c == '*':
                yield (SyntaxKind.AsteriskToken,)
            elif c == '(':
                yield (SyntaxKind.OpenParenToken,)
            elif c == ')':
                yield (SyntaxKind.CloseParenToken,)
            elif c == '-':
                yield (SyntaxKind.MinusToken,)
            elif c == '+':
                yield (SyntaxKind.PlusToken,)
            elif c == '=':
                yield (SyntaxKind.EqualsToken,)
            elif c == '[':
                yield (SyntaxKind.OpenBracketToken,)
            elif c == ']':
                yield (SyntaxKind.CloseBracketToken,)
            elif c == ':':
                yield (SyntaxKind.ColonToken,)
            elif c == ';':
                yield (SyntaxKind.SemicolonToken,)
            elif c == '<':
                yield (SyntaxKind.LessThanToken,)
            elif c == ',':
                yield (SyntaxKind.CommaToken,)
            elif c == '>':
                yield (SyntaxKind.GreaterThanToken,)
            elif c == '.':
                yield (SyntaxKind.DotToken,)
            elif c == '?':
                yield (SyntaxKind.QuestionToken,)
            elif c == '/':
                yield (SyntaxKind.SlashToken,)
            elif c == '#':
                yield (SyntaxKind.HashToken,)
            elif c == '&':
                yield (SyntaxKind.AmpersandToken,)
            elif c.isdigit():
                value = c
                while True:
                    c = source.read(1)
                    if c.isdigit():
                        value += c
                    elif c == '.' and '.' not in value:
                        value += c
                    else:
                        yield (SyntaxKind.NumericLiteralToken, value)
                        break
                continue
            c = source.read(1)
        return
