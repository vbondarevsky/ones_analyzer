from analyzer.expression.assignment_expression_syntax import AssignmentExpressionSyntax
from analyzer.expression.binary_expression_syntax import BinaryExpressionSyntax
from analyzer.expression.empty_syntax import EmptySyntax
from analyzer.expression.equals_value_clause_syntax import EqualsValueClauseSyntax
from analyzer.expression.expression_statement_syntax import ExpressionStatementSyntax
from analyzer.expression.identifier_name_syntax import IdentifierNameSyntax
from analyzer.expression.literal_expression_syntax import LiteralExpressionSyntax
from analyzer.expression.member_access_expression_syntax import MemberAccessExpressionSyntax
from analyzer.expression.method_block_syntax import MethodBlockSyntax
from analyzer.expression.method_statement_syntax import MethodStatementSyntax
from analyzer.expression.module_syntax import ModuleSyntax
from analyzer.expression.parameter_list_syntax import ParameterListSyntax
from analyzer.expression.parameter_syntax import ParameterSyntax
from analyzer.expression.parenthesized_expression_syntax import ParenthesizedExpressionSyntax
from analyzer.expression.prefix_unary_expression_syntax import PrefixUnaryExpressionSyntax
from analyzer.expression.return_statement_syntax import ReturnStatementSyntax
from analyzer.expression.variable_declaration_syntax import VariableDeclarationSyntax
from analyzer.syntax_kind import SyntaxKind


class InvalidSyntaxError(Exception):
    pass


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.token = next(self.lexer)

    def next_token(self):
        self.token = next(self.lexer)

    def eat(self, kind):
        if not isinstance(kind, list):
            kind = [kind]
        token = self.token
        if self.token.kind in kind:
            self.next_token()
            return token
        else:
            raise InvalidSyntaxError('syntax error')

    def parse(self):
        return self.module()

    def module(self):
        declarations = self.declarations()
        methods = self.methods()
        statements = self.statements()
        end_of_file_token = self.token
        return ModuleSyntax(declarations, methods, statements, end_of_file_token)

    def declarations(self):
        declarations = []
        while self.token.kind == SyntaxKind.VarKeyword:
            declarations.append(self.variable_declaration())
        return declarations

    def variable_declaration(self):
        var_token = self.token
        variables = []
        export_token = EmptySyntax()
        semicolon_token = EmptySyntax()
        self.eat(SyntaxKind.VarKeyword)
        while self.token.kind == SyntaxKind.IdentifierToken:
            variables.append(self.token)
            self.eat(SyntaxKind.IdentifierToken)
            if self.token.kind == SyntaxKind.CommaToken:
                variables.append(self.token)
                self.eat(SyntaxKind.CommaToken)
        if self.token.kind == SyntaxKind.ExportKeyword:
            export_token = self.token
            self.eat(SyntaxKind.ExportKeyword)
        if self.token.kind == SyntaxKind.SemicolonToken:
            semicolon_token = self.token
            self.eat(SyntaxKind.SemicolonToken)
        return VariableDeclarationSyntax(var_token, variables, export_token, semicolon_token)

    def methods(self):
        methods = []
        while self.token.kind in [SyntaxKind.FunctionKeyword, SyntaxKind.ProcedureKeyword]:
            methods.append(self.method_block())
        return methods

    def method_block(self):
        begin = self.method_statement()
        declarations = self.declarations()
        statements = self.statements()
        end = self.eat([SyntaxKind.EndFunctionKeyword, SyntaxKind.EndProcedureKeyword])
        return MethodBlockSyntax(begin, declarations, statements, end)

    def method_statement(self):
        declaration_keyword = self.eat([SyntaxKind.FunctionKeyword, SyntaxKind.ProcedureKeyword])
        identifier = self.eat(SyntaxKind.IdentifierToken)
        parameter_list = self.parameter_list()
        if self.token.kind == SyntaxKind.ExportKeyword:
            export = self.eat(SyntaxKind.ExportKeyword)
        else:
            export = EmptySyntax()
        return MethodStatementSyntax(declaration_keyword, identifier, parameter_list, export)

    def parameter_list(self):
        open_paren = self.eat(SyntaxKind.OpenParenToken)
        parameters = []
        while self.token.kind == SyntaxKind.IdentifierToken:
            parameters.append(self.parameter())
            if self.token.kind == SyntaxKind.CommaToken:
                parameters.append(self.eat(SyntaxKind.CommaToken))
        if self.token.kind == SyntaxKind.CloseParenToken:
            close_paren = self.eat(SyntaxKind.CloseParenToken)
        return ParameterListSyntax(open_paren, parameters, close_paren)

    def parameter(self):
        identifier = self.eat(SyntaxKind.IdentifierToken)
        default = self.default()
        return ParameterSyntax(identifier, default)

    def default(self):
        if self.token.kind == SyntaxKind.EqualsToken:
            equals_token = self.eat(SyntaxKind.EqualsToken)
            value = LiteralExpressionSyntax(self.token)
            self.eat([SyntaxKind.NumericLiteralToken, SyntaxKind.StringLiteralToken,
                      SyntaxKind.DateLiteralToken, SyntaxKind.UndefinedKeyword,
                      SyntaxKind.NullKeyword, SyntaxKind.TrueKeyword, SyntaxKind.FalseKeyword])
            return EqualsValueClauseSyntax(equals_token, value)
        return EmptySyntax()

    def statements(self):
        statements = []
        statement = self.statement()
        if statement.kind != SyntaxKind.Empty:
            statements.append(statement)
        while self.token.kind == SyntaxKind.SemicolonToken:
            self.eat(SyntaxKind.SemicolonToken)
            statement = self.statement()
            if statement.kind != SyntaxKind.Empty:
                statements.append(statement)
        return statements

    def statement(self):
        if self.token.kind == SyntaxKind.ReturnKeyword:
            return self.return_statement()
        elif self.token.kind == SyntaxKind.IdentifierToken:
            expression = self.assignment_statement()
            semicolon_token = self.token if self.token.kind == SyntaxKind.SemicolonToken else EmptySyntax()
            return ExpressionStatementSyntax(expression, semicolon_token)
        elif self.token.kind in [SyntaxKind.NumericLiteralToken, SyntaxKind.OpenParenToken,
                                 SyntaxKind.MinusToken, SyntaxKind.PlusToken]:
            expression = self.expression()
            semicolon_token = self.token if self.token.kind == SyntaxKind.SemicolonToken else EmptySyntax()
            return ExpressionStatementSyntax(expression, semicolon_token)
        else:
            return EmptySyntax()

    def return_statement(self):
        return_keyword = self.eat(SyntaxKind.ReturnKeyword)
        expression = self.expression()
        semicolon_token = EmptySyntax()
        if self.token.kind == SyntaxKind.SemicolonToken:
            semicolon_token = self.token
        return ReturnStatementSyntax(return_keyword, expression, semicolon_token)

    def assignment_statement(self):
        node = self.factor()
        if self.token.kind == SyntaxKind.EqualsToken:
            return AssignmentExpressionSyntax(
                node,
                self.eat(SyntaxKind.EqualsToken),
                self.expression())
        else:
            return node

    def expression(self):
        node = self.term()
        while self.token.kind in [SyntaxKind.PlusToken, SyntaxKind.MinusToken]:
            node = BinaryExpressionSyntax(
                node,
                self.eat([SyntaxKind.PlusToken, SyntaxKind.MinusToken]),
                self.term())
        return node

    def term(self):
        node = self.unary()
        while self.token.kind in [SyntaxKind.AsteriskToken, SyntaxKind.SlashToken, SyntaxKind.PercentToken]:
            node = BinaryExpressionSyntax(
                node,
                self.eat([SyntaxKind.AsteriskToken, SyntaxKind.SlashToken, SyntaxKind.PercentToken]),
                self.unary())
        return node

    def unary(self):
        if self.token.kind == SyntaxKind.MinusToken:
            return PrefixUnaryExpressionSyntax(
                SyntaxKind.UnaryMinusExpression,
                self.eat(SyntaxKind.MinusToken),
                self.factor())
        elif self.token.kind == SyntaxKind.PlusToken:
            return PrefixUnaryExpressionSyntax(
                SyntaxKind.UnaryPlusExpression,
                self.eat(SyntaxKind.PlusToken),
                self.factor())
        else:
            return self.factor()

    def factor(self):
        if self.token.kind == SyntaxKind.OpenParenToken:
            return ParenthesizedExpressionSyntax(
                self.eat(SyntaxKind.OpenParenToken),
                self.expression(),
                self.eat(SyntaxKind.CloseParenToken))
        elif self.token.kind == SyntaxKind.NumericLiteralToken:
            return LiteralExpressionSyntax(self.eat(SyntaxKind.NumericLiteralToken))
        elif self.token.kind == SyntaxKind.IdentifierToken:
            node = IdentifierNameSyntax(self.eat(SyntaxKind.IdentifierToken))
            if self.token.kind == SyntaxKind.DotToken:
                return self.member_access()
            else:
                return IdentifierNameSyntax(token)
        else:
            return EmptySyntax()

    def member_access(self):
        node = self.factor()
        while self.token.kind == SyntaxKind.DotToken:
            node = MemberAccessExpressionSyntax(
                node,
                self.eat(SyntaxKind.DotToken),
                self.factor())
        return node
