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
            elif self.character in '=<>':
                self.read_comparison_operator()
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
            elif self.character == ',':
                self.token = (SyntaxKind.CommaToken,)
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
                self.read_date()
            elif self.character == '"':
                self.read_string()
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

    def read_date(self):
        characters = []
        while True:
            self.next_character()
            if self.character.isdigit():
                characters.append(self.character)
            elif self.character == "'":
                self.token = (SyntaxKind.DateLiteralToken, ''.join(characters))
                break
            else:
                self.token = (SyntaxKind.BadToken,)
                break
        self.next_character()

    def read_comparison_operator(self):
        first_character = self.character
        self.next_character()

        if (first_character + self.character) == '<>':
            self.token = (SyntaxKind.LessThanGreaterThanToken,)
            self.next_character()
        elif (first_character + self.character) == '<=':
            self.token = (SyntaxKind.LessThanEqualsToken,)
            self.next_character()
        elif (first_character + self.character) == '>=':
            self.token = (SyntaxKind.GreaterThanEqualsToken,)
            self.next_character()
        elif first_character == '<':
            self.token = (SyntaxKind.LessThanToken,)
        elif first_character == '>':
            self.token = (SyntaxKind.GreaterThanToken,)
        elif first_character == '=':
            self.token = (SyntaxKind.EqualsToken,)

    def read_string(self):
        self.next_character()
        characters = []
        while True:
            if self.character == '"':
                self.next_character()
                if self.character == '"':
                    characters.append(self.character)
                    self.next_character()
                else:
                    self.token = (SyntaxKind.StringLiteralToken, ''.join(characters))
                    # self.next_character()
                    break
            else:
                characters.append(self.character)
                self.next_character()
