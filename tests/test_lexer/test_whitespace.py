import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import tokenize_source


class TestLexerWhiteSpace(unittest.TestCase):
    def test_empty(self):
        tokens = tokenize_source("")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].kind, SyntaxKind.EndOfFileToken)

    def test_naive_whitespace(self):
        tokens = tokenize_source(" \t  \n  ")
        self.assertEqual(len(tokens), 4)
        self.assertEqual(tokens[0].kind, SyntaxKind.WhitespaceTrivia)
        self.assertEqual(tokens[1].kind, SyntaxKind.EndOfLineTrivia)
        self.assertEqual(tokens[2].kind, SyntaxKind.WhitespaceTrivia)
        self.assertEqual(tokens[3].kind, SyntaxKind.EndOfFileToken)
