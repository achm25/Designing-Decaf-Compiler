"""
    Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    lark link: https://lark-parser.readthedocs.io/en/latest/visitors.html
    sample code link: https://github.com/lark-parser/lark/blob/master/lark/visitors.py
"""

from lark import Transformer

class DecafVisitor(Transformer):
    def new_function__init__(self):
        super().__init__()
    
    def pass_up(self, args):
        return args

    def pass_up_first_element(self, args):
        if len(args) == 0:
            return None
        return args[0]

    def new_function(self, tree):
        return_type, function_identifier, function_parameters, function_body = tree
        code = [
            f"check:",
            "\tsubu $sp, $sp, 8\t# decrement sp to make space to save ra, fp",
            "\tsw $fp, 8($sp)\t# save fp",
            "\tsw $ra, 4($sp)\t# save ra",
            "\taddiu $fp, $sp, 8\t# set up new fp",
        ]
        return code


    #labels:
    # pass_up_first_element , new_variable,variable_definition,prim_type,named_type,array_type,new_function,new_void_function
    # pass_up,new_class,access_mode,statement_block,optional_expresion_statement,if_statement,while_statement,for_statement,return_statement
    # pass_up_first_element,break_statement,continue_statement,print_statement,logical_or,logical_and,equals_operation
    # not_equals_operation,lt_operation,lte_operation,gt_operation,gte_operation,addition_operation,add_plus,subtraction_operation,minus_plus,
    # multiplication_operation,mul_plus,division_operation,divide_plus,modulo_operation,baghi_plus,minus_operation,
    # not_operation,this_expression,read_integer,read_line,initiate_class,f,l,assignment,
    # identifier_l_value,member_access_l_value,array_access_l_value,identifier_l_value,
    # function_call,method_call,identifier,new_identifier,int_const,double_const,bool_const,null_const,string_const



    def pass_up_first_element(self, tree):
        pass

    def pass_up_first_element(self, tree):
        pass

    def new_variable(self, tree):
        pass

    def variable_definition(self, tree):
        pass

    def prim_type(self, tree):
        pass

    def named_type(self, tree):
        pass

    def array_type(self, tree):
        pass

    def new_function(self, tree):
        pass

    def new_void_function(self, tree):

        pass

    def pass_up(self, tree):
        pass

    def new_class(self, tree):
        pass

    def access_mode(self, tree):
        pass

    def statement_block(self, tree):
        pass

    def optional_expresion_statement(self, tree):
        pass

    def if_statement(self, tree):
        pass

    def while_statement(self, tree):
        pass

    def for_statement(self, tree):
        pass

    def return_statement(self, tree):

        pass

    def pass_up_first_element(self, tree):
        pass

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
        pass

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
        pass


    def identifier_l_value(self, tree):
        pass

    def member_access_l_value(self, tree):
        pass

    def array_access_l_value(self, tree):
        pass

    def identifier_l_value(self, tree):
        pass


    def function_call(self, tree):
        pass

    def method_call(self, tree):
        pass

    def identifier(self, tree):
        pass

    def new_identifier(self, tree):
        pass

    def int_const(self, tree):
        pass

    def double_const(self, tree):
        pass

    def bool_const(self, tree):
        pass

    def null_const(self, tree):
        pass

    def string_const (self, tree):

        pass
