class BinaryExpressionSyntax(object):
    def __init__(self, kind, left, operator_token, right):
        self.kind = kind
        self.left = left
        self.operator_token = operator_token
        self.right = right

    def __str__(self):
        return f"{self.left}{self.operator_token}{self.right}"
