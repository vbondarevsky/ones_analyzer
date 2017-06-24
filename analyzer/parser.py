from analyzer.expression.binary_expression_syntax import BinaryExpressionSyntax
from analyzer.expression.literal_expression_syntax import LiteralExpressionSyntax
from analyzer.expression.module_syntax import ModuleSyntax
from analyzer.expression.parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from analyzer.expression.prefix_unary_expression_syntax import PrefixUnaryExpressionSyntax
from analyzer.expression.variable_declaration_syntax import VariableDeclarationSyntax
from analyzer.syntax_kind import SyntaxKind


class InvalidSyntaxError(Exception):
    pass


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = next(self.lexer)

    def next_token(self):
        self.token = next(self.lexer)

    def match(self, kind):
        if self.token.kind == kind:
            self.next_token()
        else:
            raise InvalidSyntaxError('syntax error')

    def factor(self):
        token = self.token
        if token.kind == SyntaxKind.PlusToken:
            self.match(SyntaxKind.PlusToken)
            return PrefixUnaryExpressionSyntax(SyntaxKind.UnaryPlusExpression, token, self.factor())
        elif token.kind == SyntaxKind.MinusToken:
            self.match(SyntaxKind.MinusToken)
            return PrefixUnaryExpressionSyntax(SyntaxKind.UnaryMinusExpression, token, self.factor())
        elif token.kind == SyntaxKind.NumericLiteralToken:
            self.match(SyntaxKind.NumericLiteralToken)
            return LiteralExpressionSyntax(SyntaxKind.NumericLiteralExpression, token)
        elif token.kind == SyntaxKind.OpenParenToken:
            self.match(SyntaxKind.OpenParenToken)
            node = self.expr()
            close_token = self.token
            self.match(SyntaxKind.CloseParenToken)
            return ParenthesizedExpressionSyntax(token, node, close_token)

    def term(self):
        node = self.factor()

        while self.token.kind in [SyntaxKind.AsteriskToken, SyntaxKind.SlashToken]:
            token = self.token
            if token.kind == SyntaxKind.SlashToken:
                self.match(SyntaxKind.SlashToken)
            elif token.kind == SyntaxKind.AsteriskToken:
                self.match(SyntaxKind.AsteriskToken)

            if token.kind == SyntaxKind.SlashToken:
                node = BinaryExpressionSyntax(SyntaxKind.DivideExpression, node, token, self.term())
            elif token.kind == SyntaxKind.AsteriskToken:
                node = BinaryExpressionSyntax(SyntaxKind.MultiplyExpression, node, token, self.term())
        return node

    def expr(self):

        node = self.term()

        while self.token.kind in [SyntaxKind.PlusToken, SyntaxKind.MinusToken]:
            token = self.token
            if token.kind == SyntaxKind.PlusToken:
                self.match(SyntaxKind.PlusToken)
            elif token.kind == SyntaxKind.MinusToken:
                self.match(SyntaxKind.MinusToken)

            if token.kind == SyntaxKind.PlusToken:
                node = BinaryExpressionSyntax(SyntaxKind.AddExpression, node, token, self.term())
            elif token.kind == SyntaxKind.MinusToken:
                node = BinaryExpressionSyntax(SyntaxKind.SubtractExpression, node, token, self.term())

        return node

    ########################################################################
    def skip_whitespace(self):
        while self.token.kind in [SyntaxKind.WhitespaceTrivia, SyntaxKind.EndOfLineTrivia]:
            self.next_token()

    def parse(self):
        return self.module()

    def module(self):
        declarations = self.declarations()
        methods = []
        body = None
        end_of_file_token = None
        return ModuleSyntax(declarations, methods, body, end_of_file_token)

    def declarations(self):
        declarations = []
        while self.token.kind == SyntaxKind.VarKeyword:
            declarations.append(self.variable_declaration())
        return declarations

    def variable_declaration(self):
        var_token = self.token
        variables = []
        export_token = None
        semicolon_token = None
        self.match(SyntaxKind.VarKeyword)
        self.skip_whitespace()
        while self.token.kind == SyntaxKind.IdentifierToken:
            variables.append(self.token)
            self.match(SyntaxKind.IdentifierToken)
            if self.token.kind == SyntaxKind.CommaToken:
                variables.append(self.token)
                self.match(SyntaxKind.CommaToken)
                self.skip_whitespace()
        self.skip_whitespace()
        if self.token.kind == SyntaxKind.ExportKeyword:
            export_token = self.token
            self.match(SyntaxKind.ExportKeyword)
        if self.token.kind == SyntaxKind.SemicolonToken:
            semicolon_token = self.token
            self.match(SyntaxKind.SemicolonToken)
        self.skip_whitespace()
        return VariableDeclarationSyntax(var_token, variables, export_token, semicolon_token)
