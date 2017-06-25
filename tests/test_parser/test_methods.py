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

    def test_one_method_with_five_parameters_and_different_default_value(self):
        code = \
            """Процедура МояПроцедура(П1 = 150.2, П2, П3 = "Строка", П4='20170605', П5 = Неопределено)
            КонецПроцедуры"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 1)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[0].kind, SyntaxKind.Parameter)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[0].default.kind, SyntaxKind.EqualsValueClause)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[0].default.value.token.text, "150.2")

        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[2].kind, SyntaxKind.Parameter)

        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[4].kind, SyntaxKind.Parameter)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[4].default.kind, SyntaxKind.EqualsValueClause)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[4].default.value.token.text, "Строка")

        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[6].kind, SyntaxKind.Parameter)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[6].default.kind, SyntaxKind.EqualsValueClause)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[6].default.value.token.text, "20170605")

        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[8].kind, SyntaxKind.Parameter)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[8].default.kind, SyntaxKind.EqualsValueClause)
        self.assertEqual(syntax_tree.methods[0].parameter_list.parameters[8].default.value.token.kind,
                         SyntaxKind.UndefinedKeyword)

    def test_one_method_and_block_with_declarations(self):
        code = \
            """Процедура МояПроцедура()
                Перем ЛокальнаяПеременная1, ЛокальнаяПеременная2;
            КонецПроцедуры"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 1)
        self.assertEqual(len(syntax_tree.methods[0].block.declarations), 1)
        self.assertEqual(len(syntax_tree.methods[0].block.statements), 0)

    def test_one_method_and_with_return(self):
        code = \
            """Процедура МояПроцедура()
                Возврат;
            КонецПроцедуры"""
        syntax_tree = parse_source(code)
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)
        self.assertEqual(len(syntax_tree.methods), 1)
        self.assertEqual(len(syntax_tree.methods[0].block.declarations), 0)
        self.assertEqual(len(syntax_tree.methods[0].block.statements), 1)
