from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerPunctuationTokens(TestCaseLexer):
    def test_tilde_token(self):
        self.tokenize_source("~", 2)
        self.check_token(0, SyntaxKind.TildeToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_percent_token(self):
        self.tokenize_source("%", 2)
        self.check_token(0, SyntaxKind.PercentToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_asterisk_token(self):
        self.tokenize_source("*", 2)
        self.check_token(0, SyntaxKind.AsteriskToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_open_paren_token(self):
        self.tokenize_source("(", 2)
        self.check_token(0, SyntaxKind.OpenParenToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_close_paren_token(self):
        self.tokenize_source(")", 2)
        self.check_token(0, SyntaxKind.CloseParenToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_minus_token(self):
        self.tokenize_source("-", 2)
        self.check_token(0, SyntaxKind.MinusToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_plus_token(self):
        self.tokenize_source("+", 2)
        self.check_token(0, SyntaxKind.PlusToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_open_bracket_token(self):
        self.tokenize_source("[", 2)
        self.check_token(0, SyntaxKind.OpenBracketToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_close_bracket_token(self):
        self.tokenize_source("]", 2)
        self.check_token(0, SyntaxKind.CloseBracketToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_colon_token(self):
        self.tokenize_source(":", 2)
        self.check_token(0, SyntaxKind.ColonToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_semicolon_token(self):
        self.tokenize_source(";", 2)
        self.check_token(0, SyntaxKind.SemicolonToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_comma_token(self):
        self.tokenize_source(",", 2)
        self.check_token(0, SyntaxKind.CommaToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_dot_token(self):
        self.tokenize_source(".", 2)
        self.check_token(0, SyntaxKind.DotToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_question_token(self):
        self.tokenize_source("?", 2)
        self.check_token(0, SyntaxKind.QuestionToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_slash_token(self):
        self.tokenize_source("/", 2)
        self.check_token(0, SyntaxKind.SlashToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_hash_token(self):
        self.tokenize_source("#", 2)
        self.check_token(0, SyntaxKind.HashToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])

    def test_ampersand_token(self):
        self.tokenize_source("&", 2)
        self.check_token(0, SyntaxKind.AmpersandToken, [], [])
        self.check_token(1, SyntaxKind.EndOfFileToken, [], [])
