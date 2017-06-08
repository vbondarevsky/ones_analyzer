from analyzer.syntax_kind import SyntaxKind


class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.character = None
        self.token = None

    def tokenize(self):
        while True:
            if self.character is None:
                self.next_character()

            if len(self.character) == 0:
                self.token = (SyntaxKind.EndOfFileToken,)
                break
            elif self.character.isdigit():
                self.read_number()
            elif self.character == '~':
                self.token = (SyntaxKind.TildeToken,)
                self.next_character()
            elif self.character == '%':
                self.token = (SyntaxKind.PercentToken,)
                self.next_character()
            elif self.character == '*':
                self.token = (SyntaxKind.AsteriskToken,)
                self.next_character()
            elif self.character == '(':
                self.token = (SyntaxKind.OpenParenToken,)
                self.next_character()
            elif self.character == ')':
                self.token = (SyntaxKind.CloseParenToken,)
                self.next_character()
            elif self.character == '-':
                self.token = (SyntaxKind.MinusToken,)
                self.next_character()
            elif self.character == '+':
                self.token = (SyntaxKind.PlusToken,)
                self.next_character()
            elif self.character == '=':
                self.token = (SyntaxKind.EqualsToken,)
                self.next_character()
            elif self.character == '[':
                self.token = (SyntaxKind.OpenBracketToken,)
                self.next_character()
            elif self.character == ']':
                self.token = (SyntaxKind.CloseBracketToken,)
                self.next_character()
            elif self.character == ':':
                self.token = (SyntaxKind.ColonToken,)
                self.next_character()
            elif self.character == ';':
                self.token = (SyntaxKind.SemicolonToken,)
                self.next_character()
            elif self.character == '<':
                self.token = (SyntaxKind.LessThanToken,)
                self.next_character()
            elif self.character == ',':
                self.token = (SyntaxKind.CommaToken,)
                self.next_character()
            elif self.character == '>':
                self.token = (SyntaxKind.GreaterThanToken,)
                self.next_character()
            elif self.character == '.':
                self.token = (SyntaxKind.DotToken,)
                self.next_character()
            elif self.character == '?':
                self.token = (SyntaxKind.QuestionToken,)
                self.next_character()
            elif self.character == '/':
                self.token = (SyntaxKind.SlashToken,)
                self.next_character()
            elif self.character == '#':
                self.token = (SyntaxKind.HashToken,)
                self.next_character()
            elif self.character == '&':
                self.token = (SyntaxKind.AmpersandToken,)
                self.next_character()
            elif self.character == "'":
                value = ""
                while True:
                    self.next_character()
                    if self.character.isdigit():
                        value += self.character
                    elif self.character == "'":
                        self.token = (SyntaxKind.DateLiteralToken, value)
                        break
                self.next_character()
            else:
                raise Exception(f"Unexpected symbol: {self.character}")

            yield self.token

        return

    def next_character(self):
        self.character = self.source.read(1)

    def read_number(self):
        characters = [self.character]
        dot = 0
        while True:
            self.next_character()
            if self.character.isdigit() or self.character == '.' and not dot:
                if self.character == '.':
                    dot += 1
                characters.append(self.character)
            else:
                break

        self.token = (SyntaxKind.NumericLiteralToken, ''.join(characters))
