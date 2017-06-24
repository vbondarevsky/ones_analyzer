from analyzer.expression.binary_expression_syntax import BinaryExpressionSyntax
from analyzer.expression.literal_expression_syntax import LiteralExpressionSyntax
from analyzer.expression.parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from analyzer.expression.prefix_unary_expression_syntax import PrefixUnaryExpressionSyntax
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

    def parse(self):
        node = self.expr()
        if self.token.kind != SyntaxKind.EndOfFileToken:
            raise InvalidSyntaxError('syntax error')

        return node
