import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import parse_source


class TestParserDeclarations(unittest.TestCase):
    def test_empty(self):
        syntax_tree = parse_source("")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 0)

    def test_simple_declaration(self):
        syntax_tree = parse_source("Перем А")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 1)
        self.assertEqual(syntax_tree.declarations[0].kind, SyntaxKind.VariableDeclaration)
        self.assertEqual(len(syntax_tree.declarations[0].variables), 1)

    def test_one_declaration_with_several_variables(self):
        syntax_tree = parse_source("Перем А, Б;")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 1)
        self.assertEqual(syntax_tree.declarations[0].kind, SyntaxKind.VariableDeclaration)
        self.assertEqual(len(syntax_tree.declarations[0].variables), 3)

    def test_one_declaration_with_one_variable_and_export(self):
        syntax_tree = parse_source("Перем А Экспорт;")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 1)
        self.assertEqual(syntax_tree.declarations[0].kind, SyntaxKind.VariableDeclaration)
        self.assertEqual(len(syntax_tree.declarations[0].variables), 1)
        self.assertEqual(syntax_tree.declarations[0].export_token.kind, SyntaxKind.ExportKeyword)

    def test_two_declaration_with_one_variable_and_export(self):
        syntax_tree = parse_source("Перем А Экспорт;\nПерем Б Экспорт;")
        self.assertEqual(syntax_tree.kind, SyntaxKind.Module)
        self.assertEqual(len(syntax_tree.declarations), 2)
        self.assertEqual(syntax_tree.declarations[0].kind, SyntaxKind.VariableDeclaration)
        self.assertEqual(syntax_tree.declarations[1].kind, SyntaxKind.VariableDeclaration)
        self.assertEqual(len(syntax_tree.declarations[0].variables), 1)
        self.assertEqual(len(syntax_tree.declarations[1].variables), 1)
        self.assertEqual(syntax_tree.declarations[0].export_token.kind, SyntaxKind.ExportKeyword)
        self.assertEqual(syntax_tree.declarations[1].export_token.kind, SyntaxKind.ExportKeyword)
