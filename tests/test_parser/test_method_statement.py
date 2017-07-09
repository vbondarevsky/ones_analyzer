from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserMethodStatement(TestCaseParser):
    def test_procedure_with_export(self):
        code = \
            """Процедура МояПроцедура() Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.methods[0].begin.declaration_keyword, SyntaxKind.ProcedureKeyword)
        self.assertNode(self.syntax_tree.methods[0].begin.identifier, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.export, SyntaxKind.ExportKeyword)

    def test_procedure_without_export(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.methods[0].begin.declaration_keyword, SyntaxKind.ProcedureKeyword)
        self.assertNode(self.syntax_tree.methods[0].begin.identifier, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.export, SyntaxKind.Empty)

    def test_function_with_export(self):
        code = \
            """Функция МояПроцедура() Экспорт
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.FunctionBlock])
        self.assertNode(self.syntax_tree.methods[0].begin.declaration_keyword, SyntaxKind.FunctionKeyword)
        self.assertNode(self.syntax_tree.methods[0].begin.identifier, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.export, SyntaxKind.ExportKeyword)

    def test_function_without_export(self):
        code = \
            """Функция МояПроцедура()
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.FunctionBlock])
        self.assertNode(self.syntax_tree.methods[0].begin.declaration_keyword, SyntaxKind.FunctionKeyword)
        self.assertNode(self.syntax_tree.methods[0].begin.identifier, SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.export, SyntaxKind.Empty)
