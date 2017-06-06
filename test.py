import unittest
from io import StringIO as Source

from lexer import Lexer
from syntax_kind import SyntaxKind


class TestLexer(unittest.TestCase):
    def test_empty_list(self):
        tokens = Lexer().tokenize(Source(""))
        self.assertNotEqual(tokens, None)
        self.assertFalse(tokens)

    def test_plus_token(self):
        tokens = Lexer().tokenize(Source("+"))
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.PlusToken, tokens[0][0])

    def test_minus_token(self):
        tokens = Lexer().tokenize(Source("-"))
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.MinusToken, tokens[0][0])
