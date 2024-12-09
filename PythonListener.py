# Generated from Python.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParser import PythonParser
else:
    from PythonParser import PythonParser

# This class defines a complete listener for a parse tree produced by PythonParser.
class PythonListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParser#program.
    def enterProgram(self, ctx:PythonParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonParser#program.
    def exitProgram(self, ctx:PythonParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonParser#statement.
    def enterStatement(self, ctx:PythonParser.StatementContext):
        pass

    # Exit a parse tree produced by PythonParser#statement.
    def exitStatement(self, ctx:PythonParser.StatementContext):
        pass


    # Enter a parse tree produced by PythonParser#simple_stmt.
    def enterSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#simple_stmt.
    def exitSimple_stmt(self, ctx:PythonParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#compound_stmt.
    def enterCompound_stmt(self, ctx:PythonParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#compound_stmt.
    def exitCompound_stmt(self, ctx:PythonParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#break_stmt.
    def enterBreak_stmt(self, ctx:PythonParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#break_stmt.
    def exitBreak_stmt(self, ctx:PythonParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#continue_stmt.
    def enterContinue_stmt(self, ctx:PythonParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#continue_stmt.
    def exitContinue_stmt(self, ctx:PythonParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#if_stmt.
    def enterIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#if_stmt.
    def exitIf_stmt(self, ctx:PythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#elif_part.
    def enterElif_part(self, ctx:PythonParser.Elif_partContext):
        pass

    # Exit a parse tree produced by PythonParser#elif_part.
    def exitElif_part(self, ctx:PythonParser.Elif_partContext):
        pass


    # Enter a parse tree produced by PythonParser#else_part.
    def enterElse_part(self, ctx:PythonParser.Else_partContext):
        pass

    # Exit a parse tree produced by PythonParser#else_part.
    def exitElse_part(self, ctx:PythonParser.Else_partContext):
        pass


    # Enter a parse tree produced by PythonParser#while_stmt.
    def enterWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#while_stmt.
    def exitWhile_stmt(self, ctx:PythonParser.While_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#for_stmt.
    def enterFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#for_stmt.
    def exitFor_stmt(self, ctx:PythonParser.For_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#condition.
    def enterCondition(self, ctx:PythonParser.ConditionContext):
        pass

    # Exit a parse tree produced by PythonParser#condition.
    def exitCondition(self, ctx:PythonParser.ConditionContext):
        pass


    # Enter a parse tree produced by PythonParser#or_condition.
    def enterOr_condition(self, ctx:PythonParser.Or_conditionContext):
        pass

    # Exit a parse tree produced by PythonParser#or_condition.
    def exitOr_condition(self, ctx:PythonParser.Or_conditionContext):
        pass


    # Enter a parse tree produced by PythonParser#and_condition.
    def enterAnd_condition(self, ctx:PythonParser.And_conditionContext):
        pass

    # Exit a parse tree produced by PythonParser#and_condition.
    def exitAnd_condition(self, ctx:PythonParser.And_conditionContext):
        pass


    # Enter a parse tree produced by PythonParser#not_condition.
    def enterNot_condition(self, ctx:PythonParser.Not_conditionContext):
        pass

    # Exit a parse tree produced by PythonParser#not_condition.
    def exitNot_condition(self, ctx:PythonParser.Not_conditionContext):
        pass


    # Enter a parse tree produced by PythonParser#comparison.
    def enterComparison(self, ctx:PythonParser.ComparisonContext):
        pass

    # Exit a parse tree produced by PythonParser#comparison.
    def exitComparison(self, ctx:PythonParser.ComparisonContext):
        pass


    # Enter a parse tree produced by PythonParser#comparison_operator.
    def enterComparison_operator(self, ctx:PythonParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by PythonParser#comparison_operator.
    def exitComparison_operator(self, ctx:PythonParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_stmt.
    def enterAssignment_stmt(self, ctx:PythonParser.Assignment_stmtContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_stmt.
    def exitAssignment_stmt(self, ctx:PythonParser.Assignment_stmtContext):
        pass


    # Enter a parse tree produced by PythonParser#assignment_operator.
    def enterAssignment_operator(self, ctx:PythonParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by PythonParser#assignment_operator.
    def exitAssignment_operator(self, ctx:PythonParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by PythonParser#expr.
    def enterExpr(self, ctx:PythonParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParser#expr.
    def exitExpr(self, ctx:PythonParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParser#term.
    def enterTerm(self, ctx:PythonParser.TermContext):
        pass

    # Exit a parse tree produced by PythonParser#term.
    def exitTerm(self, ctx:PythonParser.TermContext):
        pass


    # Enter a parse tree produced by PythonParser#factor.
    def enterFactor(self, ctx:PythonParser.FactorContext):
        pass

    # Exit a parse tree produced by PythonParser#factor.
    def exitFactor(self, ctx:PythonParser.FactorContext):
        pass


    # Enter a parse tree produced by PythonParser#atom.
    def enterAtom(self, ctx:PythonParser.AtomContext):
        pass

    # Exit a parse tree produced by PythonParser#atom.
    def exitAtom(self, ctx:PythonParser.AtomContext):
        pass


    # Enter a parse tree produced by PythonParser#array.
    def enterArray(self, ctx:PythonParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonParser#array.
    def exitArray(self, ctx:PythonParser.ArrayContext):
        pass


    # Enter a parse tree produced by PythonParser#array_element.
    def enterArray_element(self, ctx:PythonParser.Array_elementContext):
        pass

    # Exit a parse tree produced by PythonParser#array_element.
    def exitArray_element(self, ctx:PythonParser.Array_elementContext):
        pass


    # Enter a parse tree produced by PythonParser#function_call.
    def enterFunction_call(self, ctx:PythonParser.Function_callContext):
        pass

    # Exit a parse tree produced by PythonParser#function_call.
    def exitFunction_call(self, ctx:PythonParser.Function_callContext):
        pass


    # Enter a parse tree produced by PythonParser#range_call.
    def enterRange_call(self, ctx:PythonParser.Range_callContext):
        pass

    # Exit a parse tree produced by PythonParser#range_call.
    def exitRange_call(self, ctx:PythonParser.Range_callContext):
        pass



del PythonParser