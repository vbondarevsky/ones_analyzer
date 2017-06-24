from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.parser import Parser


def parse_source(code):
    return Parser(Lexer(Source(code)).tokenize()).parse()
