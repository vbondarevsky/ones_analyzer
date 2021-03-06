from enum import Enum


class SyntaxKind(Enum):
    # Punctuation
    TildeToken = 1000  # ~
    PercentToken = 1001  # %
    AsteriskToken = 1002  # *
    OpenParenToken = 1003  # (
    CloseParenToken = 1004  # )
    MinusToken = 1005  # -
    PlusToken = 1006  # +
    OpenBracketToken = 1008  # [
    CloseBracketToken = 1009  # ]
    ColonToken = 1010  # :
    SemicolonToken = 1011  # ;
    CommaToken = 1013  # ,
    DotToken = 1015  # .
    QuestionToken = 1016  # ?
    SlashToken = 1017  # /
    HashToken = 1018  # #
    AmpersandToken = 1019  # &

    # Other
    EndOfFileToken = 4000

    # Comparison operator
    EqualsToken = 1007  # =
    LessThanToken = 1012  # <
    GreaterThanToken = 1014  # >
    LessThanEqualsToken = 2000  # <=
    GreaterThanEqualsToken = 2001  # >=
    LessThanGreaterThanToken = 2002  # <>

    # Keywords
    IfKeyword = 3000
    ThenKeyword = 3001
    ElseIfKeyword = 3002
    ElseKeyword = 3003
    EndIfKeyword = 3004
    ForKeyword = 3005
    EachKeyword = 3006
    InKeyword = 3007
    ToKeyword = 3008
    WhileKeyword = 3009
    DoKeyword = 3010
    EndDoKeyword = 3011
    ProcedureKeyword = 3012
    FunctionKeyword = 3013
    EndProcedureKeyword = 3014
    EndFunctionKeyword = 3015
    VarKeyword = 3016
    GotoKeyword = 3017
    ReturnKeyword = 3018
    ContinueKeyword = 3019
    BreakKeyword = 3020
    AndKeyword = 3021
    OrKeyword = 3022
    NotKeyword = 3023
    TryKeyword = 3024
    ExceptKeyword = 3025
    RaiseKeyword = 3026
    EndTryKeyword = 3027
    NewKeyword = 3028
    ExecuteKeyword = 3029

    NullKeyword = 3030
    TrueKeyword = 3031
    FalseKeyword = 3032
    UndefinedKeyword = 3033

    ExportKeyword = 3034

    # Tokens
    BadToken = 5000
    IdentifierToken = 5001
    NumericLiteralToken = 5002
    DateLiteralToken = 5003
    StringLiteralToken = 5004

    # Trivia
    EndOfLineTrivia = 7000
    WhitespaceTrivia = 7001
    SingleLineCommentTrivia = 7002

    # syntax
    SubtractExpression = 9000
    AddExpression = 9001
    DivideExpression = 9002
    MultiplyExpression = 9003
    ModuloExpression = 9006

    NumericLiteralExpression = 9004
    StringLiteralExpression = 9015
    DateLiteralExpression = 9016
    UndefinedLiteralExpression = 9017
    NullLiteralExpression = 9018
    TrueLiteralExpression = 9019
    FalseLiteralExpression = 9020

    UnaryPlusExpression = 9005
    UnaryMinusExpression = 9006

    ParenthesizedExpression = 9007
    AssignmentExpression = 9300
    ExpressionStatement = 9400

    VariableDeclaration = 9008
    Module = 9009

    FunctionBlock = 111111
    ProcedureBlock = 11112

    FunctionStatement = 1
    ProcedureStatement = 2

    EndFunctionStatement = 3
    EndProcedureStatement = 4

    ParameterList = 9012
    Parameter = 9013

    EqualsValueClause = 9014

    Block = 9100
    Body = 9200
    Empty = 10000

    ReturnStatement = 11000
