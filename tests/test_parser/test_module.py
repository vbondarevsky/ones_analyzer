from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserModule(TestCaseParser):
    def test_empty(self):
        self.parse_source("")
        self.assertNode(self.syntax_tree.declarations, [])
        self.assertNode(self.syntax_tree.methods, [])
        self.assertNode(self.syntax_tree.statements, [])

    def test_declarations(self):
        self.parse_source("Перем А")
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.methods, [])
        self.assertNode(self.syntax_tree.statements, [])

    def test_methods(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры
            Функция МояФункция()
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [])
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock, SyntaxKind.FunctionBlock])
        self.assertNode(self.syntax_tree.statements, [])

    def test_statements(self):
        self.parse_source("А=8+2;")
        self.assertNode(self.syntax_tree.declarations, [])
        self.assertNode(self.syntax_tree.methods, [])
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
        self.assertNode(self.syntax_tree.statements[0].semicolon_token, SyntaxKind.SemicolonToken)

    def test_declarations_and_methods(self):
        code = \
            """Перем А;
            Процедура МояПроцедура()
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.statements, [])

    def test_declarations_and_statements(self):
        code = \
            """Перем А;
            А=8"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.methods, [])
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])

    def test_methods_and_statements(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры
            А=8"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [])
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])

    def test_declarations_and_methods_and_statements(self):
        code = \
            """Перем А;
            Процедура МояПроцедура()
            КонецПроцедуры
            А=8"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.declarations, [SyntaxKind.VariableDeclaration])
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.statements, [SyntaxKind.ExpressionStatement])
