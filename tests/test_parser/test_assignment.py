import unittest

from analyzer.syntax_kind import SyntaxKind
from tests.utils import parse_source


class TestParserAssignment(unittest.TestCase):
    def test_simple_assignment_statement(self):
        syntax_tree = parse_source("А=2;")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.ExpressionStatement)
        self.assertEqual(str(syntax_tree.body.statements[0]), "А=2;")

    def test_assignment_statement_and_expression(self):
        syntax_tree = parse_source("А=2+3;")
        self.assertEqual(syntax_tree.body.statements[0].kind, SyntaxKind.ExpressionStatement)
        self.assertEqual(str(syntax_tree.body.statements[0]), "А=2+3;")
