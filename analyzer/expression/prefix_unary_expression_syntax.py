class PrefixUnaryExpressionSyntax(object):
    def __init__(self, kind, operator_token, operand):
        self.kind = kind
        self.operator_token = operator_token
        self.operand = operand

    def __str__(self):
        return f"{self.operator_token.text}{self.operand}"
