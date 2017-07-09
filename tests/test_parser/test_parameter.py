from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserParameter(TestCaseParser):
    def test_default_value_number(self):
        code = \
            """Процедура МояПроцедура(П = 9) Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.NumericLiteralExpression)

    def test_default_value_string(self):
        code = \
            """Процедура МояПроцедура(П = "строка") Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.StringLiteralExpression)

    def test_default_value_date(self):
        code = \
            """Процедура МояПроцедура(П = '20170710') Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.DateLiteralExpression)

    def test_default_value_undefined(self):
        code = \
            """Процедура МояПроцедура(П = Неопределено) Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.UndefinedLiteralExpression)

    def test_default_value_null(self):
        code = \
            """Процедура МояПроцедура(П = NULL) Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.NullLiteralExpression)

    def test_default_value_bool(self):
        code = \
            """Процедура МояПроцедура(П = Истина) Экспорт
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].identifier,
                        SyntaxKind.IdentifierToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default,
                        SyntaxKind.EqualsValueClause)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.equals_token,
                        SyntaxKind.EqualsToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters[0].default.value,
                        SyntaxKind.TrueLiteralExpression)
