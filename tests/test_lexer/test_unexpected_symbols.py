from analyzer.lexer import UnexpectedSymbolError
from tests.utils import TestCaseLexer


class TestUnexpectedSymbols(TestCaseLexer):
    def test_unexpected_symbols(self):
        with self.assertRaises(UnexpectedSymbolError):
            self.tokenize_source("@", 2)
