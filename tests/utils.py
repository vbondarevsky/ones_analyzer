from io import StringIO as Source
from unittest import TestCase

from analyzer.lexer import Lexer
from analyzer.parser import Parser


class TestCaseParser(TestCase):
    def parse_source(self, code):
        self.syntax_tree = Parser(Lexer(Source(code)).tokenize()).parse()
        self.assertEqual(code, str(self.syntax_tree))

    def assertNode(self, node, kind_node):
        if isinstance(node, list):
            self.assertEqual(len(kind_node), len(node))
            for i in range(len(kind_node)):
                self.assertEqual(kind_node[i], node[i].kind)
        else:
            self.assertEqual(kind_node, node.kind)


class TestCaseLexer(TestCase):
    def tokenize_source(self, code, length):
        self.code = code
        self.tokens = list(Lexer(Source(code)).tokenize())
        self.assertEqual(length, len(self.tokens))
        self.assertEqual(code, ''.join(map(str, self.tokens)))

    def assertToken(self, index, kind, leading_trivia, trailing_trivia):
        token = self.tokens[index]
        self.assertEqual(kind, token.kind)
        self.assertEqual(len(leading_trivia), len(token.leading_trivia))
        self.assertEqual(len(trailing_trivia), len(token.trailing_trivia))
        for i in range(len(leading_trivia)):
            self.assertEqual(leading_trivia[i], token.leading_trivia[i].kind)
        for i in range(len(trailing_trivia)):
            self.assertEqual(trailing_trivia[i], token.trailing_trivia[i].kind)
