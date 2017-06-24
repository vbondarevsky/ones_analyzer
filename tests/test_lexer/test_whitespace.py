import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerWhiteSpace(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer(Source("")).tokenize())
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].kind, SyntaxKind.EndOfFileToken)

    def test_naive_whitespace(self):
        tokens = list(Lexer(Source(" \t  \n  ")).tokenize())
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].kind, SyntaxKind.WhitespaceTrivia)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfLineTrivia)
        self.assertEqual(tokens[2].kind, SyntaxKind.WhitespaceTrivia)
        self.assertEqual(tokens[3].kind, SyntaxKind.EndOfFileToken)
