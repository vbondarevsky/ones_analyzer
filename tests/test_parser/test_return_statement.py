from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserMethodReturnStatement(TestCaseParser):
    def test_procedure_and_return(self):
        code = \
            """Процедура МояПроцедура()
                Возврат
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].statements, [SyntaxKind.ReturnStatement])
        self.assertNode(self.syntax_tree.methods[0].statements[0].return_keyword, SyntaxKind.ReturnKeyword)
        self.assertNode(self.syntax_tree.methods[0].statements[0].expression, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.methods[0].statements[0].semicolon_token, SyntaxKind.Empty)

    def test_procedure_and_return_and_semicolon(self):
        code = \
            """Процедура МояПроцедура()
                Возврат;
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].statements, [SyntaxKind.ReturnStatement])
        self.assertNode(self.syntax_tree.methods[0].statements[0].return_keyword, SyntaxKind.ReturnKeyword)
        self.assertNode(self.syntax_tree.methods[0].statements[0].expression, SyntaxKind.Empty)
        self.assertNode(self.syntax_tree.methods[0].statements[0].semicolon_token, SyntaxKind.SemicolonToken)

    def test_function_and_return(self):
        code = \
            """Функция МояПроцедура()
                Возврат 2
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].statements, [SyntaxKind.ReturnStatement])
        self.assertNode(self.syntax_tree.methods[0].statements[0].return_keyword, SyntaxKind.ReturnKeyword)
        self.assertNode(self.syntax_tree.methods[0].statements[0].expression, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.methods[0].statements[0].semicolon_token, SyntaxKind.Empty)

    def test_function_and_return_and_semicolon(self):
        code = \
            """Функция МояПроцедура()
                Возврат 2;
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].statements, [SyntaxKind.ReturnStatement])
        self.assertNode(self.syntax_tree.methods[0].statements[0].return_keyword, SyntaxKind.ReturnKeyword)
        self.assertNode(self.syntax_tree.methods[0].statements[0].expression, SyntaxKind.NumericLiteralExpression)
        self.assertNode(self.syntax_tree.methods[0].statements[0].semicolon_token, SyntaxKind.SemicolonToken)
