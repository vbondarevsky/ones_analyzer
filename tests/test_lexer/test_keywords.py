import unittest
from io import StringIO as Source

from analyzer.lexer import Lexer
from analyzer.syntax_kind import SyntaxKind


class TestLexerKeyword(unittest.TestCase):
    def test_keywords(self):
        self.run_test(["Если", "If"], SyntaxKind.IfKeyword)
        self.run_test(["Тогда", "Then"], SyntaxKind.ThenKeyword)
        self.run_test(["ИначеЕсли", "ElsIf"], SyntaxKind.ElseIfKeyword)
        self.run_test(["Иначе", "Else"], SyntaxKind.ElseKeyword)
        self.run_test(["КонецЕсли", "EndIf"], SyntaxKind.EndIfKeyword)

        self.run_test(["Для", "For"], SyntaxKind.ForKeyword)
        self.run_test(["Каждого", "Each"], SyntaxKind.EachKeyword)
        self.run_test(["Из", "In"], SyntaxKind.InKeyword)
        self.run_test(["По", "To"], SyntaxKind.ToKeyword)
        self.run_test(["Пока", "While"], SyntaxKind.WhileKeyword)
        self.run_test(["Цикл", "Do"], SyntaxKind.DoKeyword)
        self.run_test(["КонецЦикла", "EndDo"], SyntaxKind.EndDoKeyword)
        self.run_test(["Продолжить", "Continue"], SyntaxKind.ContinueKeyword)
        self.run_test(["Прервать", "Break"], SyntaxKind.BreakKeyword)

        self.run_test(["Процедура", "Procedure"], SyntaxKind.ProcedureKeyword)
        self.run_test(["КонецПроцедуры", "EndProcedure"], SyntaxKind.EndProcedureKeyword)
        self.run_test(["Функция", "Function"], SyntaxKind.FunctionKeyword)
        self.run_test(["КонецФункции", "EndFunction"], SyntaxKind.EndFunctionKeyword)
        self.run_test(["Возврат", "Return"], SyntaxKind.ReturnKeyword)

        self.run_test(["И", "And"], SyntaxKind.AndKeyword)
        self.run_test(["Или", "Or"], SyntaxKind.OrKeyword)
        self.run_test(["Не", "Not"], SyntaxKind.NotKeyword)

        self.run_test(["Попытка", "Try"], SyntaxKind.TryKeyword)
        self.run_test(["Исключение", "Except"], SyntaxKind.ExceptKeyword)
        self.run_test(["ВызватьИсключение", "Raise"], SyntaxKind.RaiseKeyword)
        self.run_test(["КонецПопытки", "EndTry"], SyntaxKind.EndTryKeyword)

        self.run_test(["Перем", "Var"], SyntaxKind.VarKeyword)
        self.run_test(["Перейти", "Goto"], SyntaxKind.GotoKeyword)

        self.run_test(["Новый", "New"], SyntaxKind.NewKeyword)
        self.run_test(["Выполнить", "Execute"], SyntaxKind.ExecuteKeyword)

        self.run_test(["Null"], SyntaxKind.NullKeyword)
        self.run_test(["Истина", "True"], SyntaxKind.TrueKeyword)
        self.run_test(["Ложь", "False"], SyntaxKind.FalseKeyword)

        self.run_test(["Экспорт", "Export"], SyntaxKind.ExportKeyword)

    def run_test(self, keywords, syntax_kind):
        code_list = []
        code_list.extend(keywords)
        code_list.extend(map(str.upper, keywords))
        code_list.extend(map(str.lower, keywords))
        for code in code_list:
            with self.subTest(code):
                tokens = list(Lexer(Source(code)).tokenize())
                self.assertEqual(len(tokens), 2)
                self.assertEqual(tokens[0].kind, syntax_kind)
                self.assertEqual(tokens[0].text, code)
                self.assertEqual(tokens[1].kind, SyntaxKind.EndOfFileToken)


if __name__ == '__main__':
    unittest.main()
