import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerPunctuationTokens(unittest.TestCase):
    def test_empty_list(self):
        tokens = list(Lexer(Source("")).tokenize())
        self.assertNotEqual(tokens, None)
        self.assertFalse(tokens)

    def test_tilde_token(self):
        tokens = list(Lexer(Source("~")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.TildeToken, tokens[0][0])

    def test_percent_token(self):
        tokens = list(Lexer(Source("%")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.PercentToken, tokens[0][0])

    def test_asterisk_token(self):
        tokens = list(Lexer(Source("*")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.AsteriskToken, tokens[0][0])

    def test_open_paren_token(self):
        tokens = list(Lexer(Source("(")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.OpenParenToken, tokens[0][0])

    def test_close_paren_token(self):
        tokens = list(Lexer(Source(")")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.CloseParenToken, tokens[0][0])

    def test_minus_token(self):
        tokens = list(Lexer(Source("-")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.MinusToken, tokens[0][0])

    def test_plus_token(self):
        tokens = list(Lexer(Source("+")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.PlusToken, tokens[0][0])

    def test_open_bracket_token(self):
        tokens = list(Lexer(Source("[")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.OpenBracketToken, tokens[0][0])

    def test_close_bracket_token(self):
        tokens = list(Lexer(Source("]")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.CloseBracketToken, tokens[0][0])

    def test_colon_token(self):
        tokens = list(Lexer(Source(":")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.ColonToken, tokens[0][0])

    def test_semicolon_token(self):
        tokens = list(Lexer(Source(";")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.SemicolonToken, tokens[0][0])

    def test_comma_token(self):
        tokens = list(Lexer(Source(",")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.CommaToken, tokens[0][0])

    def test_dot_token(self):
        tokens = list(Lexer(Source(".")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.DotToken, tokens[0][0])

    def test_question_token(self):
        tokens = list(Lexer(Source("?")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.QuestionToken, tokens[0][0])

    def test_slash_token(self):
        tokens = list(Lexer(Source("/")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.SlashToken, tokens[0][0])

    def test_hash_token(self):
        tokens = list(Lexer(Source("#")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.HashToken, tokens[0][0])

    def test_ampersand_token(self):
        tokens = list(Lexer(Source("&")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.AmpersandToken, tokens[0][0])


if __name__ == '__main__':
    unittest.main()
