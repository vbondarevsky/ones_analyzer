from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserVariableDeclaration(TestCaseParser):
    def test_one_declaration_one_variable(self):
        self.parse_source("Перем А")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.Empty)

    def test_one_declaration_two_variables(self):
        self.parse_source("Перем А, Б")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken,
                                                                     SyntaxKind.CommaToken,
                                                                     SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.Empty)

    def test_one_declaration_one_variable_with_semicolon(self):
        self.parse_source("Перем А;")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.SemicolonToken)

    def test_one_declaration_one_variable_with_export(self):
        self.parse_source("Перем А Экспорт")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.ExportKeyword)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.Empty)

    def test_one_declaration_one_variable_with_export_and_semicolon(self):
        self.parse_source("Перем А Экспорт;")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.ExportKeyword)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.SemicolonToken)

    def test_two_declarations_one_variable(self):
        code = \
            """Перем А Экспорт;
            Перем Б"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration, SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.declarations[0].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[0].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[0].export_token, SyntaxKind.ExportKeyword)
        self.assertNode(self.syntax_tree.declarations[0].semicolon_token, SyntaxKind.SemicolonToken)

        self.assertNode(self.syntax_tree.declarations[1].var_token, SyntaxKind.VarKeyword)
        self.assertNode(self.syntax_tree.declarations[1].variables, [SyntaxKind.IdentifierToken])
        self.assertNode(self.syntax_tree.declarations[1].export_token, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.declarations[1].semicolon_token, SyntaxKind.Empty)
