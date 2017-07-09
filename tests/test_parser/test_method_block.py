from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserMethodBlock(TestCaseParser):
    def test_one_procedure(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock])
        self.assertNode(self.syntax_tree.methods[0].end, SyntaxKind.EndProcedureKeyword)

    def test_one_function(self):
        code = \
            """Функция МояПроцедура()
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.FunctionBlock])
        self.assertNode(self.syntax_tree.methods[0].end, SyntaxKind.EndFunctionKeyword)

    def test_two_methods(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры

            Функция МояФункция()
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods, [SyntaxKind.ProcedureBlock, SyntaxKind.FunctionBlock])
