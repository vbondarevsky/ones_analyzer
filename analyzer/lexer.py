from analyzer.syntax_kind import SyntaxKind


class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.character = None
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
                         'экспорт': SyntaxKind.ExportKeyword,
                         'export': SyntaxKind.ExportKeyword}

    def tokenize(self):
        while True:
            if self.character is None:
                self.next_character()

            if len(self.character) == 0:
                self.token = (SyntaxKind.EndOfFileToken,)
                break
            elif self.character.isspace():
                self.read_whitespace()
                continue
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
                    self.token = (SyntaxKind.SlashToken,)

            elif self.character == "'":
                self.read_date()
            elif self.character == '"':
                self.read_string()
            elif self.character.isalpha() or self.character == '_':
                self.read_identifier()
            else:
                raise Exception(f"Unexpected symbol: {self.character}, position: {self.position}")

            yield self.token

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

    def read_identifier(self):
        characters = [self.character]
        self.next_character()
        while True:
            if self.character.isalnum() or self.character == '_':
                characters.append(self.character)
                self.next_character()
            else:
                break
        lexeme = ''.join(characters)

        self.token = (self.keywords.get(lexeme.lower(), SyntaxKind.IdentifierToken), lexeme)

    def read_comment(self):
        characters = []
        self.next_character()
        while True:
            if self.character == '\n' or not len(self.character):
                self.next_character()
                break
            else:
                characters.append(self.character)
                self.next_character()
        self.token = (SyntaxKind.SingleLineCommentTrivia, ''.join(characters))

    def read_whitespace(self):
        self.next_character()
        while True:
            if not self.character.isspace() or not len(self.character):
                break
            else:
                self.next_character()

    def is_punctuation(self):
        return self.character in "~%*()-+[]:;,.?#&"

    def read_punctuation(self):
        self.token = (self.punctuation.get(self.character),)
        self.next_character()
