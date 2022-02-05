"""
    Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    lark link: https://lark-parser.readthedocs.io/en/latest/visitors.html
    sample code link: https://github.com/lark-parser/lark/blob/master/lark/visitors.py
"""

from lark import Transformer

from Transformer.nodes.assignment import Assignment
from Transformer.nodes.block import StatementBlock
from Transformer.nodes.break_stm import BreakStatement
from Transformer.nodes.constant import Const
from Transformer.nodes.expression import Expression
from Transformer.nodes.for_stm import ForStatement
from Transformer.nodes.function import Function
from Transformer.nodes.identifier import Identifier, IdentifierLValue
from Transformer.nodes.if_stm import IfStatement
from Transformer.nodes.library_functions import ReadInteger
from Transformer.nodes.optional_expr import OptionalExpr
from Transformer.nodes.primitive_type import PrimType
from Transformer.nodes.print_node import PrintNode
from Transformer.nodes.return_stm import ReturnStatement
from Transformer.nodes.variable_decl import Variable
from Transformer.nodes.whlie_stm import WhileStatement
from phase3.symbol_table import SymbolTable


class DecafVisitor(Transformer):
    __number_of_ifs = 0
    __number_of_loops = 0

    def new_function__init__(self):
        super().__init__()

    def pass_up(self, args):
        return args

    def pass_up_first_element(self, tree):
        if len(tree) == 0:
            return None
        return tree[0]

    def new_function(self, tree):
        return_type = tree[0]
        func_identifier = tree[1]
        func_params = tree[2]
        func_block = tree[3]
        return Function(return_type, func_identifier, func_params, func_block)

    # labels:
    # pass_up_first_element , new_variable,variable_definition,prim_type,named_type,array_type,new_function,new_void_function
    # pass_up,new_class,access_mode,statement_block,optional_expression_statement,if_statement,while_statement,for_statement,return_statement
    # pass_up_first_element,break_statement,continue_statement,print_statement,logical_or,logical_and,equals_operation
    # not_equals_operation,lt_operation,lte_operation,gt_operation,gte_operation,addition_operation,add_plus,subtraction_operation,minus_plus,
    # multiplication_operation,mul_plus,division_operation,divide_plus,modulo_operation,baghi_plus,minus_operation,
    # not_operation,this_expression,read_integer,read_line,initiate_class,f,l,assignment,
    # identifier_l_value,member_access_l_value,array_access_l_value,identifier_l_value, var_assignment
    # function_call,method_call,identifier,new_identifier,int_const,double_const,bool_const,null_const,string_const

    def finalize(self, tree):
        symbol_table = SymbolTable()
        code = ["\t.globl main", "\t.text","main:"]
        for child in tree:
            print(child)
            code_part = child.cgen(symbol_table)
            code += code_part

        final_code = ["\t.data"]
        final_code += symbol_table.data_storage
        print(str(final_code))
        final_code += code
        return final_code

    def new_variable(self, tree):
        return tree[0]

    def var_assignment(self, tree):
        print("var_assignment")
        pass

    def variable_definition(self, tree):
        v_type = tree[0]
        v_ident = tree[1]
        return Variable(v_type, v_ident)

    def prim_type(self, tree):
        return PrimType(tree[0])

    def named_type(self, tree):
        print("named_type")
        pass

    def array_type(self, tree):
        print("array_type")
        pass

    def new_void_function(self, tree):
        print("new_void_function")
        pass

    def new_class(self, tree):
        print("new_class")
        pass

    def access_mode(self, tree):
        print("access_mode")
        pass

    @staticmethod
    def statement_block(tree):
        statements = []
        for child in tree:
            print(child)
            statements.append(child)
        return StatementBlock(statements)

    def if_statement(self, tree):
        self.__number_of_ifs += 1
        if_stm = IfStatement(tree[0], tree[1], self.__number_of_ifs)
        if len(tree) == 3:
            if_stm.else_block = tree[3]
        return if_stm

    def while_statement(self, tree):
        self.__number_of_loops += 1
        return WhileStatement(tree[0], tree[1], self.__number_of_loops)

    def for_statement(self, tree):
        self.__number_of_loops += 1
        return ForStatement(tree[0], tree[1], tree[2], tree[3], self.__number_of_loops)

    @staticmethod
    def return_statement(tree):
        return ReturnStatement(tree[0])

    def break_statement(self, tree):
        curr_loop = self.__number_of_loops
        return BreakStatement(curr_loop)

    def continue_statement(self, tree):
        print("continue_statement")
        pass

    def print_statement(self, tree):
        return PrintNode(tree)

    def logical_or(self, tree):
        print("logical_or")
        pass

    def logical_and(self, tree):
        print("logical_and")
        pass

    def equals_operation(self, tree):
        print("equals_operation")
        pass

    def not_equals_operation(self, tree):
        print("not_equals_operation")
        pass

    def lt_operation(self, tree):
        return Expression("lt", tree[0], tree[1])

    def lte_operation(self, tree):
        print("lte_operation")
        pass

    def gt_operation(self, tree):
        print("gt_operation")
        pass

    def gte_operation(self, tree):
        print("gte_operation")
        pass

    def addition_operation(self, tree):
        return Expression("add", tree[0], tree[1])

    def add_plus(self, tree):
        print("add_plus")
        pass

    def subtraction_operation(self, tree):
        print("subtraction_operation")
        pass

    def minus_plus(self, tree):
        print("minus_plus")
        pass

    def multiplication_operation(self, tree):
        print("multiplication_operation")
        pass

    def mul_plus(self, tree):
        print("mul_plus")
        pass

    def division_operation(self, tree):
        print("division_operation")
        pass

    def divide_plus(self, tree):
        print("divide_plus")
        pass

    def modulo_operation(self, tree):
        print("modulo_operation")
        pass

    def baghi_plus(self, tree):
        print("baghi_plus")
        pass

    def minus_operation(self, tree):
        print("minus_operation")
        pass

    def not_operation(self, tree):
        print("not_operation")
        pass

    def this_expression(self, tree):
        print("this_expression")
        pass

    def read_integer(self, tree):
        return ReadInteger()

    def read_line(self, tree):
        print("read_line")
        pass

    def initiate_class(self, tree):
        print("initiate_class")
        pass

    def f(self, tree):
        print("f")
        pass

    def l(self, tree):
        print("l")
        pass

    def assignment(self, tree):
        return Assignment(tree[0], tree[1])

    def identifier_l_value(self, tree):
        return IdentifierLValue(tree[0])

    def optional_expression_statement(self, tree):
        return OptionalExpr(tree[0])

    def member_access_l_value(self, tree):
        print("member_access_l_value")
        pass

    def array_access_l_value(self, tree):
        print("array_access_l_value")
        pass

    def function_call(self, tree):
        print("function_call")
        pass

    def method_call(self, tree):
        print("method_call")
        pass

    def new_identifier(self, tree):
        return Identifier(tree[0])

    def identifier(self, tree):
        return Identifier(tree[0])

    def int_const(self, tree):
        return Const("int", tree[0])

    def double_const(self, tree):
        return Const("double", tree[0])

    def bool_const(self, tree):
        return Const("bool", tree[0])

    def null_const(self, tree):
        return Const("null", tree[0])

    def string_const(self, tree):
        return Const("string", tree[0])
