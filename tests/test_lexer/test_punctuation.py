from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseLexer


class TestLexerPunctuationTokens(TestCaseLexer):
    def test_tilde_token(self):
        self.tokenize_source("~", 2)
        self.assertToken(0, SyntaxKind.TildeToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_percent_token(self):
        self.tokenize_source("%", 2)
        self.assertToken(0, SyntaxKind.PercentToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_asterisk_token(self):
        self.tokenize_source("*", 2)
        self.assertToken(0, SyntaxKind.AsteriskToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_open_paren_token(self):
        self.tokenize_source("(", 2)
        self.assertToken(0, SyntaxKind.OpenParenToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_close_paren_token(self):
        self.tokenize_source(")", 2)
        self.assertToken(0, SyntaxKind.CloseParenToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_minus_token(self):
        self.tokenize_source("-", 2)
        self.assertToken(0, SyntaxKind.MinusToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_plus_token(self):
        self.tokenize_source("+", 2)
        self.assertToken(0, SyntaxKind.PlusToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_open_bracket_token(self):
        self.tokenize_source("[", 2)
        self.assertToken(0, SyntaxKind.OpenBracketToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_close_bracket_token(self):
        self.tokenize_source("]", 2)
        self.assertToken(0, SyntaxKind.CloseBracketToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_colon_token(self):
        self.tokenize_source(":", 2)
        self.assertToken(0, SyntaxKind.ColonToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_semicolon_token(self):
        self.tokenize_source(";", 2)
        self.assertToken(0, SyntaxKind.SemicolonToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_comma_token(self):
        self.tokenize_source(",", 2)
        self.assertToken(0, SyntaxKind.CommaToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_dot_token(self):
        self.tokenize_source(".", 2)
        self.assertToken(0, SyntaxKind.DotToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_question_token(self):
        self.tokenize_source("?", 2)
        self.assertToken(0, SyntaxKind.QuestionToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_slash_token(self):
        self.tokenize_source("/", 2)
        self.assertToken(0, SyntaxKind.SlashToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_hash_token(self):
        self.tokenize_source("#", 2)
        self.assertToken(0, SyntaxKind.HashToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])

    def test_ampersand_token(self):
        self.tokenize_source("&", 2)
        self.assertToken(0, SyntaxKind.AmpersandToken, [], [])
        self.assertToken(1, SyntaxKind.EndOfFileToken, [], [])
