import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import parse_source


class TestParserMethods(unittest.TestCase):
    def test_empty(self):
        syntax_tree = parse_source("")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 0)

    def test_only_one_method(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 1)
        self.assertEqual(len(syntax_tree.methods[0].parameter_list.parameters), 0)

    def test_only_two_methods(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры
            
            Функция МояФункция()
            КонецФункции"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 2)
        self.assertEqual(len(syntax_tree.methods[0].parameter_list.parameters), 0)
        self.assertEqual(len(syntax_tree.methods[1].parameter_list.parameters), 0)

    def test_one_method_with_two_parameters(self):
        code = \
            """Процедура МояПроцедура(Параметр1, Параметр2)
            КонецПроцедуры"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 1)
        self.assertEqual(len(syntax_tree.methods[0].parameter_list.parameters), 3)
