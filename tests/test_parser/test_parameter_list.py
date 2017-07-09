from analyzer.syntax_kind import SyntaxKind
from tests.utils import TestCaseParser


class TestParserMethodParameterList(TestCaseParser):
    def test_empty_list(self):
        code = \
            """Процедура МояПроцедура()
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.open_paren, SyntaxKind.OpenParenToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.close_paren, SyntaxKind.CloseParenToken)

    def test_one_parameter(self):
        code = \
            """Процедура МояПроцедура(Параметр1)
            КонецПроцедуры"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.open_paren, SyntaxKind.OpenParenToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.close_paren, SyntaxKind.CloseParenToken)

    def test_two_parameters(self):
        code = \
            """Функция МояПроцедура(Параметр1, Параметр2)
            КонецФункции"""
        self.parse_source(code)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.open_paren, SyntaxKind.OpenParenToken)
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.parameters, [SyntaxKind.Parameter,
                                                                                      SyntaxKind.CommaToken,
                                                                                      SyntaxKind.Parameter])
        self.assertNode(self.syntax_tree.methods[0].begin.parameter_list.close_paren, SyntaxKind.CloseParenToken)
