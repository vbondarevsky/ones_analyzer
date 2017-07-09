from analyzer.expression.assignment_expression_syntax import AssignmentExpressionSyntax
from analyzer.expression.binary_expression_syntax import BinaryExpressionSyntax
from analyzer.expression.empty_syntax import EmptySyntax
from analyzer.expression.equals_value_clause_syntax import EqualsValueClauseSyntax
from analyzer.expression.expression_statement_syntax import ExpressionStatementSyntax
from analyzer.expression.literal_expression_syntax import LiteralExpressionSyntax
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
            export = self.token
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
            self.next_token()
            return EqualsValueClauseSyntax(equals_token, value)
        return EmptySyntax()

    def statements(self):
        statements = []
        statement = self.statement()
        if statement.kind != SyntaxKind.Empty:
            statements.append(statement)
        return statements

    def statement(self):
        if self.token.kind == SyntaxKind.ReturnKeyword:
            return self.return_statement()
        elif self.token.kind == SyntaxKind.IdentifierToken:
            expression = self.assignment_statement()
            semicolon_token = EmptySyntax()
            if self.token.kind == SyntaxKind.SemicolonToken:
                semicolon_token = self.eat(SyntaxKind.SemicolonToken)
            return ExpressionStatementSyntax(expression, semicolon_token)
        return self.expression()

    def return_statement(self):
        return_keyword = self.token
        self.eat(SyntaxKind.ReturnKeyword)
        expression = self.expression()
        semicolon_token = EmptySyntax()
        if self.token.kind == SyntaxKind.SemicolonToken:
            semicolon_token = self.token
            self.eat(SyntaxKind.SemicolonToken)
        return ReturnStatementSyntax(return_keyword, expression, semicolon_token)

    def assignment_statement(self):
        left = self.token
        self.eat(SyntaxKind.IdentifierToken)
        operator_token = self.token
        self.eat(SyntaxKind.EqualsToken)
        right = self.expression()
        return AssignmentExpressionSyntax(left, operator_token, right)

    def factor(self):
        token = self.token
        if token.kind == SyntaxKind.PlusToken:
            self.eat(SyntaxKind.PlusToken)
            return PrefixUnaryExpressionSyntax(SyntaxKind.UnaryPlusExpression, token, self.factor())
        elif token.kind == SyntaxKind.MinusToken:
            self.eat(SyntaxKind.MinusToken)
            return PrefixUnaryExpressionSyntax(SyntaxKind.UnaryMinusExpression, token, self.factor())
        elif token.kind == SyntaxKind.NumericLiteralToken:
            self.eat(SyntaxKind.NumericLiteralToken)
            return LiteralExpressionSyntax(token)
        elif token.kind == SyntaxKind.OpenParenToken:
            self.eat(SyntaxKind.OpenParenToken)
            node = self.expression()
            close_token = self.token
            self.eat(SyntaxKind.CloseParenToken)
            return ParenthesizedExpressionSyntax(token, node, close_token)
        else:
            return EmptySyntax()

    def term(self):
        node = self.factor()
        while self.token.kind in [SyntaxKind.AsteriskToken, SyntaxKind.SlashToken]:
            token = self.token
            if token.kind == SyntaxKind.SlashToken:
                self.eat(SyntaxKind.SlashToken)
            elif token.kind == SyntaxKind.AsteriskToken:
                self.eat(SyntaxKind.AsteriskToken)
            if token.kind == SyntaxKind.SlashToken:
                node = BinaryExpressionSyntax(SyntaxKind.DivideExpression, node, token, self.term())
            elif token.kind == SyntaxKind.AsteriskToken:
                node = BinaryExpressionSyntax(SyntaxKind.MultiplyExpression, node, token, self.term())
        return node

    def expression(self):
        node = self.term()
        while self.token.kind in [SyntaxKind.PlusToken, SyntaxKind.MinusToken]:
            token = self.token
            if token.kind == SyntaxKind.PlusToken:
                self.eat(SyntaxKind.PlusToken)
            elif token.kind == SyntaxKind.MinusToken:
                self.eat(SyntaxKind.MinusToken)
            if token.kind == SyntaxKind.PlusToken:
                node = BinaryExpressionSyntax(SyntaxKind.AddExpression, node, token, self.term())
            elif token.kind == SyntaxKind.MinusToken:
                node = BinaryExpressionSyntax(SyntaxKind.SubtractExpression, node, token, self.term())
        return node
