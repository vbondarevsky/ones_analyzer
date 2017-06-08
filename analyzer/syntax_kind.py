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
    EqualsToken = 1007  # =
    OpenBracketToken = 1008  # [
    CloseBracketToken = 1009  # ]
    ColonToken = 1010  # :
    SemicolonToken = 1011  # ;
    LessThanToken = 1012  # <
    CommaToken = 1013  # ,
    GreaterThanToken = 1014  # >
    DotToken = 1015  # .
    QuestionToken = 1016  # ?
    SlashToken = 1017  # /
    HashToken = 1018  # #
    AmpersandToken = 1019  # &

    # Other
    EndOfFileToken = 4000

    # Compound punctuation
    LessThanEqualsToken = 2000  # <=
    GreaterThanEqualsToken = 2001  # >=
    LessThanGreaterThanToken = 2002  # <>

    # Tokens
    BadToken = 5000

    NumericLiteralToken = 5002
    DateLiteralToken = 5003
    StringLiteralToken = 5004
