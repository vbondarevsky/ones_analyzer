from analyzer.syntax_kind import SyntaxKind
from analyzer.syntax_token import SyntaxToken
from analyzer.syntax_trivia import SyntaxTrivia


class UnexpectedSymbolError(Exception):
    pass


class Lexer:
    def __init__(self, source):
        self.source = source
        self.character = ''
        self.token = None
        self.position = 0
        self.punctuation = {'~': SyntaxKind.TildeToken,
                            '%': SyntaxKind.PercentToken,
                            '*': SyntaxKind.AsteriskToken,
                            '(': SyntaxKind.OpenParenToken,
                            ')': SyntaxKind.CloseParenToken,
                            '[': SyntaxKind.OpenBracketToken,
                            ']': SyntaxKind.CloseBracketToken,
                            '-': SyntaxKind.MinusToken,
                            '+': SyntaxKind.PlusToken,
                            ':': SyntaxKind.ColonToken,
                            ';': SyntaxKind.SemicolonToken,
                            ',': SyntaxKind.CommaToken,
                            '.': SyntaxKind.DotToken,
                            '?': SyntaxKind.QuestionToken,
                            '#': SyntaxKind.HashToken,
                            '&': SyntaxKind.AmpersandToken}
        self.keywords = {'если': SyntaxKind.IfKeyword,
                         'if': SyntaxKind.IfKeyword,
                         'тогда': SyntaxKind.ThenKeyword,
                         'then': SyntaxKind.ThenKeyword,
                         'иначеесли': SyntaxKind.ElseIfKeyword,
                         'elsif': SyntaxKind.ElseIfKeyword,
                         'иначе': SyntaxKind.ElseKeyword,
                         'else': SyntaxKind.ElseKeyword,
                         'конецесли': SyntaxKind.EndIfKeyword,
                         'endif': SyntaxKind.EndIfKeyword,
                         'для': SyntaxKind.ForKeyword,
                         'for': SyntaxKind.ForKeyword,
                         'каждого': SyntaxKind.EachKeyword,
                         'each': SyntaxKind.EachKeyword,
                         'из': SyntaxKind.InKeyword,
                         'in': SyntaxKind.InKeyword,
                         'по': SyntaxKind.ToKeyword,
                         'to': SyntaxKind.ToKeyword,
                         'пока': SyntaxKind.WhileKeyword,
                         'while': SyntaxKind.WhileKeyword,
                         'цикл': SyntaxKind.DoKeyword,
                         'do': SyntaxKind.DoKeyword,
                         'конеццикла': SyntaxKind.EndDoKeyword,
                         'enddo': SyntaxKind.EndDoKeyword,
                         'продолжить': SyntaxKind.ContinueKeyword,
                         'continue': SyntaxKind.ContinueKeyword,
                         'прервать': SyntaxKind.BreakKeyword,
                         'break': SyntaxKind.BreakKeyword,
                         'процедура': SyntaxKind.ProcedureKeyword,
                         'procedure': SyntaxKind.ProcedureKeyword,
                         'конецпроцедуры': SyntaxKind.EndProcedureKeyword,
                         'endprocedure': SyntaxKind.EndProcedureKeyword,
                         'функция': SyntaxKind.FunctionKeyword,
                         'function': SyntaxKind.FunctionKeyword,
                         'конецфункции': SyntaxKind.EndFunctionKeyword,
                         'endfunction': SyntaxKind.EndFunctionKeyword,
                         'возврат': SyntaxKind.ReturnKeyword,
                         'return': SyntaxKind.ReturnKeyword,
                         'и': SyntaxKind.AndKeyword,
                         'and': SyntaxKind.AndKeyword,
                         'или': SyntaxKind.OrKeyword,
                         'or': SyntaxKind.OrKeyword,
                         'не': SyntaxKind.NotKeyword,
                         'not': SyntaxKind.NotKeyword,
                         'попытка': SyntaxKind.TryKeyword,
                         'try': SyntaxKind.TryKeyword,
                         'исключение': SyntaxKind.ExceptKeyword,
                         'except': SyntaxKind.ExceptKeyword,
                         'вызватьисключение': SyntaxKind.RaiseKeyword,
                         'raise': SyntaxKind.RaiseKeyword,
                         'конецпопытки': SyntaxKind.EndTryKeyword,
                         'endtry': SyntaxKind.EndTryKeyword,
                         'перем': SyntaxKind.VarKeyword,
                         'var': SyntaxKind.VarKeyword,
                         'перейти': SyntaxKind.GotoKeyword,
                         'goto': SyntaxKind.GotoKeyword,
                         'новый': SyntaxKind.NewKeyword,
                         'new': SyntaxKind.NewKeyword,
                         'выполнить': SyntaxKind.ExecuteKeyword,
                         'execute': SyntaxKind.ExecuteKeyword,
                         'null': SyntaxKind.NullKeyword,
                         'истина': SyntaxKind.TrueKeyword,
                         'true': SyntaxKind.TrueKeyword,
                         'ложь': SyntaxKind.FalseKeyword,
                         'false': SyntaxKind.FalseKeyword,
                         'неопределено': SyntaxKind.UndefinedKeyword,
                         'undefined': SyntaxKind.UndefinedKeyword,
                         'экспорт': SyntaxKind.ExportKeyword,
                         'export': SyntaxKind.ExportKeyword}
        self.next_character()

    def next_token(self):
        while True:
            if len(self.character) == 0:
                self.token = SyntaxToken(SyntaxKind.EndOfFileToken, "")
            elif self.character.isspace():
                self.read_whitespace()
            elif self.character.isdigit():
                self.read_number()
            elif self.is_punctuation():
                self.read_punctuation()
            elif self.character in '=<>':
                self.read_comparison_operator()
            elif self.character == '/':
                self.next_character()
                if self.character == '/':
                    self.read_comment()
                else:
                    self.token = SyntaxToken(SyntaxKind.SlashToken, "/")
            elif self.character == "'":
                self.read_date()
            elif self.character == '"':
                self.read_string()
            elif self.character.isalpha() or self.character == '_':
                self.read_identifier()
            else:
                raise UnexpectedSymbolError(f"Unexpected symbol: {self.character}, position: {self.position}")

            yield self.token

            if self.token.kind == SyntaxKind.EndOfFileToken:
                break

        return

    def tokenize(self):
        leading_trivia = []
        trailing_trivia = []
        syntax_token = None
        for token in self.next_token():
            if isinstance(token, SyntaxTrivia):
                if syntax_token:
                    if token.kind == SyntaxKind.EndOfLineTrivia:
                        trailing_trivia.append(token)

                        syntax_token.leading_trivia = leading_trivia
                        syntax_token.trailing_trivia = trailing_trivia
                        yield syntax_token
                        syntax_token = None
                        leading_trivia = []
                        trailing_trivia = []
                    else:
                        trailing_trivia.append(token)
                else:
                    leading_trivia.append(token)
            else:
                if syntax_token:
                    syntax_token.leading_trivia = leading_trivia
                    syntax_token.trailing_trivia = trailing_trivia
                    yield syntax_token
                    syntax_token = token
                    leading_trivia = []
                    trailing_trivia = []
                else:
                    syntax_token = token
        else:
            syntax_token.leading_trivia = leading_trivia
            syntax_token.trailing_trivia = trailing_trivia
            yield syntax_token

        return

    def next_character(self):
        self.character = self.source.read(1)
        self.position += 1

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
        self.token = SyntaxToken(SyntaxKind.NumericLiteralToken, ''.join(characters))

    def read_date(self):
        characters = [self.character]
        while True:
            self.next_character()
            if self.character.isdigit():
                characters.append(self.character)
            elif self.character == "'":
                characters.append(self.character)
                self.token = SyntaxToken(SyntaxKind.DateLiteralToken, ''.join(characters))
                break
        self.next_character()

    def read_comparison_operator(self):
        first_character = self.character
        self.next_character()

        if (first_character + self.character) == '<>':
            self.token = SyntaxToken(SyntaxKind.LessThanGreaterThanToken, "<>")
            self.next_character()
        elif (first_character + self.character) == '<=':
            self.token = SyntaxToken(SyntaxKind.LessThanEqualsToken, "<=")
            self.next_character()
        elif (first_character + self.character) == '>=':
            self.token = SyntaxToken(SyntaxKind.GreaterThanEqualsToken, ">=")
            self.next_character()
        elif first_character == '<':
            self.token = SyntaxToken(SyntaxKind.LessThanToken, "<")
        elif first_character == '>':
            self.token = SyntaxToken(SyntaxKind.GreaterThanToken, ">")
        elif first_character == '=':
            self.token = SyntaxToken(SyntaxKind.EqualsToken, "=")

    def read_string(self):
        characters = [self.character]
        self.next_character()
        while True:
            if self.character == '"':
                characters.append(self.character)
                self.next_character()
                if self.character == '"':
                    characters.append(self.character)
                    self.next_character()
                else:
                    self.token = SyntaxToken(SyntaxKind.StringLiteralToken, ''.join(characters))
                    break
            else:
                characters.append(self.character)
                self.next_character()

    def read_identifier(self):
        characters = [self.character]
        self.next_character()
        while True:
            if self.character.isalnum() or self.character == '_':
                characters.append(self.character)
                self.next_character()
            else:
                break
        text = ''.join(characters)

        self.token = SyntaxToken(self.keywords.get(text.lower(), SyntaxKind.IdentifierToken), text)

    def read_comment(self):
        characters = [r'//']
        self.next_character()
        while True:
            if self.character == '\n' or not len(self.character):
                break
            else:
                characters.append(self.character)
                self.next_character()
        self.token = SyntaxTrivia(SyntaxKind.SingleLineCommentTrivia, ''.join(characters))

    def read_whitespace(self):
        if self.character == '\n':
            self.token = SyntaxTrivia(SyntaxKind.EndOfLineTrivia, "\n")
            self.next_character()
            return

        characters = [self.character]
        self.next_character()
        while True:
            if not self.character.isspace() or self.character == '\n':
                self.token = SyntaxTrivia(SyntaxKind.WhitespaceTrivia, ''.join(characters))
                break
            else:
                characters.append(self.character)
                self.next_character()

    def is_punctuation(self):
        return self.character in "~%*()-+[]:;,.?#&"

    def read_punctuation(self):
        self.token = SyntaxToken(self.punctuation.get(self.character), self.character)
        self.next_character()
