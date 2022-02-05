"""
    Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    lark link: https://lark-parser.readthedocs.io/en/latest/visitors.html
    sample code link: https://github.com/lark-parser/lark/blob/master/lark/visitors.py
"""

from lark import Transformer

from Transformer.nodes.array_type import ArrayType
from Transformer.nodes.assignment import Assignment
from Transformer.nodes.block import StatementBlock
from Transformer.nodes.break_stm import BreakStatement
from Transformer.nodes.constant import Const
from Transformer.nodes.expression import Expression
from Transformer.nodes.for_stm import ForStatement
from Transformer.nodes.function import Function
from Transformer.nodes.identifier import Identifier, IdentifierLValue
from Transformer.nodes.if_stm import IfStatement
from Transformer.nodes.library_functions import *
from Transformer.nodes.minus_expr import MinusExpression
from Transformer.nodes.named_type import NamedType
from Transformer.nodes.optional_expr import OptionalExpr
from Transformer.nodes.primitive_type import PrimType
from Transformer.nodes.print_node import PrintNode
from Transformer.nodes.read_line import ReadLine
from Transformer.nodes.return_stm import ReturnStatement
from Transformer.nodes.variable_decl import Variable
from Transformer.nodes.whlie_stm import WhileStatement
from phase3.symbol_table import SymbolTable
from phase3.reserved import *

class DecafVisitor(Transformer):
    __number_of_ifs = 0
    __number_of_loops = 0

    def new_function__init__(self):
        super().__init__()

    @staticmethod
    def pass_up_first_element(tree):
        if len(tree) == 0:
            return None
        return tree[0]

    @staticmethod
    def pass_up(args):
        return args

    @staticmethod
    def new_function(tree):
        return_type = tree[0]
        func_identifier = tree[1]
        func_params = tree[2]
        func_block = tree[3]
        return Function(func_identifier, func_params, func_block, return_type)

    # labels:
    # pass_up_first_element , new_variable,variable_definition,prim_type,named_type,array_type,new_function,new_void_function
    # pass_up,new_class,access_mode,statement_block,optional_expression_statement,if_statement,while_statement,for_statement,return_statement
    # pass_up_first_element,break_statement,continue_statement,print_statement,logical_or,logical_and,equals_operation
    # not_equals_operation,lt_operation,lte_operation,gt_operation,gte_operation,addition_operation,add_plus,subtraction_operation,minus_plus,
    # multiplication_operation,mul_plus,division_operation,divide_plus,modulo_operation,baghi_plus,minus_operation,
    # not_operation,this_expression,read_integer,read_line,initiate_class,f,l,assignment,
    # identifier_l_value,member_access_l_value,array_access_l_value,identifier_l_value, var_assignment
    # function_call,method_call,identifier,new_identifier,int_const,double_const,bool_const,null_const,string_const

    @staticmethod
    def finalize(tree):
        symbol_table = SymbolTable()
        code = ["\t.globl main", "\t.text"]
        for child in tree:
            code_part = child.cgen(symbol_table)
            code += code_part

        final_code = ["\t.data",reserved_data]
        final_code += symbol_table.data_storage
        final_code += code
        final_code.append(reserved_funcs)
        return final_code

    @staticmethod
    def new_variable(tree):
        return tree[0]

    @staticmethod
    def variable_definition(tree):
        v_type = tree[0]
        v_ident = tree[1]
        print("variable_definition")
        print(tree)
        v_ident.i_type = v_type.name
        print("cccccccc" , v_type.name)
        return Variable(v_type, v_ident)

    @staticmethod
    def prim_type(tree):
        return PrimType(tree[0])

    @staticmethod
    def named_type(tree):
        return NamedType(tree[0])

    @staticmethod
    def array_type(tree):
        return ArrayType(tree[0])

    @staticmethod
    def new_void_function(tree):
        func_identifier = tree[1]
        func_params = tree[2]
        func_block = tree[3]
        return Function(func_identifier, func_params, func_block)

    @staticmethod
    def new_class(tree):
        print("new_class")
        # TODO
        pass

    @staticmethod
    def statement_block(tree):
        statements = []
        for child in tree:
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
        print("FOR")
        print(tree)
        return ForStatement(tree[0], tree[1], tree[2], tree[3], self.__number_of_loops)

    @staticmethod
    def return_statement(tree):
        return ReturnStatement(tree[0])

    def break_statement(self, tree):
        curr_loop = self.__number_of_loops
        return BreakStatement(curr_loop)

    @staticmethod
    def print_statement(tree):
        return PrintNode(tree)

    @staticmethod
    def logical_or(tree):
        return Expression("or", tree[0], tree[1])

    @staticmethod
    def logical_and(tree):
        return Expression("and", tree[0], tree[1])

    @staticmethod
    def equals_operation(tree):
        return Expression("equals", tree[0], tree[1])

    @staticmethod
    def not_equals_operation(tree):
        return Expression("not_equals", tree[0], tree[1])

    @staticmethod
    def lt_operation(tree):
        return Expression("lt", tree[0], tree[1])

    @staticmethod
    def lte_operation(tree):
        return Expression("lte", tree[0], tree[1])

    @staticmethod
    def gt_operation(tree):
        return Expression("gt", tree[0], tree[1])

    @staticmethod
    def gte_operation(tree):
        return Expression("qte", tree[0], tree[1])

    @staticmethod
    def addition_operation(tree):
        return Expression("add", tree[0], tree[1])

    @staticmethod
    def add_equal(tree):
        return Expression("add_equal", tree[0], tree[1])

    @staticmethod
    def subtraction_operation(tree):
        return Expression("sub", tree[0], tree[1])

    @staticmethod
    def minus_operation(tree):
        return MinusExpression(tree[0])

    @staticmethod
    def minus_equal(tree):
        return Expression("minus_equal", tree[0], tree[1])

    @staticmethod
    def multiplication_operation(tree):
        return Expression("mult", tree[0], tree[1])

    @staticmethod
    def mult_equal(tree):
        return Expression("mult_equal", tree[0], tree[1])

    @staticmethod
    def division_operation(tree):
        return Expression("div", tree[0], tree[1])

    @staticmethod
    def divide_equal(tree):
        return Expression("divide_equal", tree[0], tree[1])

    @staticmethod
    def modulo_operation(tree):
        return Expression("modulo", tree[0], tree[1])

    @staticmethod
    def not_operation(tree):
        return Expression("not", tree[0], tree[1])

    @staticmethod
    def read_integer(tree):
        return ReadInteger()

    @staticmethod
    def read_line(tree):
        return ReadLine()

    def initiate_class(self, tree):
        print("initiate_class")
        pass

    @staticmethod
    def assignment(tree):
        return Assignment(tree[0], tree[1])

    @staticmethod
    def identifier_l_value(tree):
        print("identifier_l_value")
        print(tree)
        return IdentifierLValue(tree[0])

    @staticmethod
    def optional_expression_statement(tree):
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

    @staticmethod
    def new_identifier(tree):
        return Identifier(tree[0])

    @staticmethod
    def identifier(tree):
        print("identifier")
        print(tree)
        print()
        return Identifier(tree[0])

    @staticmethod
    def int_const(tree):
        return Const("int", tree[0])

    @staticmethod
    def double_const(tree):
        return Const("double", tree[0])

    @staticmethod
    def bool_const(tree):
        return Const("bool", tree[0])

    @staticmethod
    def null_const(tree):
        return Const("null", tree[0])

    @staticmethod
    def string_const(tree):
        return Const("string", tree[0])
