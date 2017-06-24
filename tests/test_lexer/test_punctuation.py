import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerPunctuationTokens(unittest.TestCase):
    def test_tilde_token(self):
        tokens = list(Lexer(Source("~")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.TildeToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_percent_token(self):
        tokens = list(Lexer(Source("%")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.PercentToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_asterisk_token(self):
        tokens = list(Lexer(Source("*")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.AsteriskToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_open_paren_token(self):
        tokens = list(Lexer(Source("(")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.OpenParenToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_close_paren_token(self):
        tokens = list(Lexer(Source(")")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.CloseParenToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_minus_token(self):
        tokens = list(Lexer(Source("-")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.MinusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_plus_token(self):
        tokens = list(Lexer(Source("+")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.PlusToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_open_bracket_token(self):
        tokens = list(Lexer(Source("[")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.OpenBracketToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_close_bracket_token(self):
        tokens = list(Lexer(Source("]")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.CloseBracketToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_colon_token(self):
        tokens = list(Lexer(Source(":")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.ColonToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_semicolon_token(self):
        tokens = list(Lexer(Source(";")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.SemicolonToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_comma_token(self):
        tokens = list(Lexer(Source(",")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.CommaToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_dot_token(self):
        tokens = list(Lexer(Source(".")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.DotToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_question_token(self):
        tokens = list(Lexer(Source("?")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.QuestionToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_slash_token(self):
        tokens = list(Lexer(Source("/")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.SlashToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_hash_token(self):
        tokens = list(Lexer(Source("#")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.HashToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)

    def test_ampersand_token(self):
        tokens = list(Lexer(Source("&")).tokenize())
        self.assertEqual(len(tokens), 2)
        self.assertEqual(tokens[0].kind, SyntaxKind.AmpersandToken)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)
