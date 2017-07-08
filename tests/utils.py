from io import StringIO as Source
from unittest import TestCase

from analyzer.lexer import Lexer
from analyzer.parser import Parser


def parse_source(code):
    return Parser(Lexer(Source(code)).tokenize()).parse()


class TestCaseLexer(TestCase):
    def tokenize_source(self, code, length):
        self.code = code
        self.tokens = list(Lexer(Source(code)).tokenize())
        self.assertEqual(len(self.tokens), length)

    def check_token(self, index, kind, leading_trivia, trailing_trivia):
        token = self.tokens[index]
        self.assertEqual(token.kind, kind)
        self.assertEqual(len(token.leading_trivia), len(leading_trivia))
        self.assertEqual(len(token.trailing_trivia), len(trailing_trivia))
        for i in range(len(leading_trivia)):
            self.assertEqual(token.leading_trivia[i].kind, leading_trivia[i])
        for i in range(len(trailing_trivia)):
            self.assertEqual(token.trailing_trivia[i].kind, trailing_trivia[i])
