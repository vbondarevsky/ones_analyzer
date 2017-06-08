import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerDateLiteralToken(unittest.TestCase):
    # TODO: Поменять название на более адекватное
    def test_date_(self):
        tokens = list(Lexer(Source("'00010101'")).tokenize())
        self.assertEqual(1, len(tokens))
        self.assertEqual(SyntaxKind.DateLiteralToken, tokens[0][0])
        self.assertEqual("00010101", tokens[0][1])


if __name__ == '__main__':
    unittest.main()
