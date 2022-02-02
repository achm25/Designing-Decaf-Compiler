"""
    Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    lark link: https://lark-parser.readthedocs.io/en/latest/visitors.html
    sample code link: https://github.com/lark-parser/lark/blob/master/lark/visitors.py
"""

from lark import Transformer

from Transformer.nodes.assignment import Assignment
from Transformer.nodes.block import StatementBlock
from Transformer.nodes.constant import Const
from Transformer.nodes.expression import Expression
from Transformer.nodes.function import Function
from Transformer.nodes.identifier import Identifier, IdentifierLValue
from Transformer.nodes.optional_expr import OptionalExpr
from Transformer.nodes.primitive_type import PrimType
from Transformer.nodes.return_stm import ReturnStatement
from Transformer.symbol_table import SymbolTable
from Transformer.nodes.variable_decl import Variable


class DecafVisitor(Transformer):
    def new_function__init__(self):
        super().__init__()

    def pass_up(self, args):
        print("pass up")
        print(args)
        return args

    def pass_up_first_element(self, tree):
        print("pass up first element -> done")
        if len(tree) == 0:
            return None
        return tree[0]

    def new_function(self, tree):
        print("new_function -> done")
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
        print("finalize -> done")
        symbol_table = SymbolTable()
        code = [".globl main", ".text"]
        for child in tree:
            print(child)
            code_part = child.cgen(symbol_table)
            print(code_part)
            code += code_part
        return code

    def new_variable(self, tree):
        print("new_variable -> done")
        return tree[0]

    def var_assignment(self, tree):
        print("var_assignment")
        pass

    def variable_definition(self, tree):
        print("variable_definition -> done")
        v_type = tree[0]
        v_ident = tree[1]
        return Variable(v_type, v_ident)

    def prim_type(self, tree):
        print("prim type -> done")
        return PrimType(tree[0])

    def named_type(self, tree):
        pass

    def array_type(self, tree):
        pass

    def new_void_function(self, tree):
        pass

    def new_class(self, tree):
        pass

    def access_mode(self, tree):
        pass

    def statement_block(self, tree):
        print("statement block -> done")
        statements = []
        for child in tree:
            statements.append(child)
        return StatementBlock(statements)

    def optional_expression_statement(self, tree):
        pass

    def if_statement(self, tree):
        pass

    def while_statement(self, tree):
        pass

    def for_statement(self, tree):
        pass

    def return_statement(self, tree):
        print("return_statement -> done")
        return ReturnStatement(tree[0])

    def break_statement(self, tree):
        pass

    def continue_statement(self, tree):
        pass

    def print_statement(self, tree):
        pass

    def logical_or(self, tree):
        pass

    def logical_and(self, tree):
        pass

    def equals_operation(self, tree):
        pass

    def not_equals_operation(self, tree):
        pass

    def lt_operation(self, tree):
        pass

    def lte_operation(self, tree):
        pass

    def gt_operation(self, tree):
        pass

    def gte_operation(self, tree):
        pass

    def addition_operation(self, tree):
        print("addition_operation -> done")
        return Expression("add", tree[0], tree[1])

    def add_plus(self, tree):
        pass

    def subtraction_operation(self, tree):
        pass

    def minus_plus(self, tree):
        pass

    def multiplication_operation(self, tree):
        pass

    def mul_plus(self, tree):
        pass

    def division_operation(self, tree):
        pass

    def divide_plus(self, tree):
        pass

    def modulo_operation(self, tree):
        pass

    def baghi_plus(self, tree):
        pass

    def minus_operation(self, tree):
        pass

    def not_operation(self, tree):
        pass

    def this_expression(self, tree):
        pass

    def read_integer(self, tree):
        pass

    def read_line(self, tree):
        pass

    def initiate_class(self, tree):
        pass

    def f(self, tree):
        pass

    def l(self, tree):
        pass

    def assignment(self, tree):
        print("assignment -> done")
        return Assignment(tree[0], tree[1])

    def identifier_l_value(self, tree):
        print("identifier_l_value -> done")
        return IdentifierLValue(tree[0])

    def optional_expression_statement(self, tree):
        print("optional_expression_statement -> done")
        return OptionalExpr(tree[0])

    def member_access_l_value(self, tree):
        pass

    def array_access_l_value(self, tree):
        pass

    def function_call(self, tree):
        pass

    def method_call(self, tree):
        pass


    def new_identifier(self, tree):
        print("new identifier -> done")
        return Identifier(tree[0])

    def identifier(self, tree):
        print("old_identifier -> done")
        return Identifier(tree[0])

    def int_const(self, tree):
        print("int const -> done")
        return Const("int", tree[0])

    def double_const(self, tree):
        pass

    def bool_const(self, tree):
        pass

    def null_const(self, tree):
        pass

    def string_const(self, tree):
        pass
