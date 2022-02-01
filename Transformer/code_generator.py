int_size = 1
double_size = 1
string_size = 1
bool_size = 1

class CodeGenerator:

    @staticmethod
    def pass_up_first_element(tree):
        pass

    @staticmethod
    def new_variable(tree):
        pass

    @staticmethod
    def variable_definition(tree):
        pass

    @staticmethod
    def prim_type(tree):
        pass

    @staticmethod
    def named_type(tree):
        pass

    @staticmethod
    def array_type(tree):
        pass

    @staticmethod
    def new_function(tree):
        pass

    @staticmethod
    def new_void_function(tree):
        pass

    @staticmethod
    def pass_up(tree):
        pass

    @staticmethod
    def new_class(tree):
        pass

    @staticmethod
    def access_mode(tree):
        pass

    @staticmethod
    def statement_block(tree):
        pass

    @staticmethod
    def optional_expresion_statement(tree):
        pass

    @staticmethod
    def if_statement(tree):
        pass

    @staticmethod
    def while_statement(tree):
        pass

    @staticmethod
    def for_statement(tree):
        pass

    @staticmethod
    def return_statement(tree):
        pass

    @staticmethod
    def pass_up_first_element(tree):
        pass

    @staticmethod
    def break_statement(tree):
        pass

    @staticmethod
    def continue_statement(tree):
        pass

    @staticmethod
    def print_statement(tree):
        pass

    @staticmethod
    def logical_or(tree):
        pass

    @staticmethod
    def logical_and(tree):
        pass

    @staticmethod
    def equals_operation(tree):
        pass

    @staticmethod
    def not_equals_operation(tree):
        pass

    @staticmethod
    def lt_operation(tree):
        pass

    @staticmethod
    def lte_operation(tree):
        pass

    @staticmethod
    def gt_operation(tree):
        pass

    @staticmethod
    def gte_operation(tree):
        pass

    @staticmethod
    def addition_operation(tree):
        pass

    @staticmethod
    def add_plus(tree):
        pass

    @staticmethod
    def subtraction_operation(tree):
        pass

    @staticmethod
    def minus_plus(tree):
        pass

    @staticmethod
    def multiplication_operation(tree):
        pass

    @staticmethod
    def mul_plus(tree):
        pass

    @staticmethod
    def division_operation(tree):
        pass

    @staticmethod
    def divide_plus(tree):
        pass

    @staticmethod
    def modulo_operation(tree):
        pass

    @staticmethod
    def baghi_plus(tree):
        pass

    @staticmethod
    def minus_operation(tree):
        pass

    @staticmethod
    def not_operation(tree):
        pass

    @staticmethod
    def this_expression(tree):
        pass

    @staticmethod
    def read_integer(tree):
        pass

    @staticmethod
    def read_line(tree):
        pass

    @staticmethod
    def initiate_class(tree):
        pass

    @staticmethod
    def f(tree):
        pass

    @staticmethod
    def l(self, tree):
        pass

    @staticmethod
    def assignment(tree):
        pass

    @staticmethod
    def identifier_l_value(tree):
        pass

    @staticmethod
    def member_access_l_value(tree):
        pass

    @staticmethod
    def array_access_l_value(tree):
        pass

    @staticmethod
    def identifier_l_value(tree):
        pass

    @staticmethod
    def function_call(tree):
        pass

    @staticmethod
    def method_call(tree):
        pass

    @staticmethod
    def identifier(tree):
        pass

    @staticmethod
    def new_identifier(tree):
        pass

    @staticmethod
    def int_const(value):
        code = (
            f"\t \t li $t0,{value} \t\t# load constant value to $t0",
            f"\tsw $t0, {int_size}($sp)\t# add to stack",
        )
        return code

    @staticmethod
    def double_const(value):
        #todo handle .e and .
        code = (
            f"\t \t li $t0,{value} \t\t# load constant value to $t0",
            f"\tsw $t0, {double_size}($sp)\t# ladd to stack",
        )
        return code

    @staticmethod
    def bool_const(value):
        code = (
            f"\t \t li $t0,{value} \t\t# load constant value to $t0",
            f"\tsw $t0, {bool_size}($sp)\t # add to stack",
        )
        return code

    @staticmethod
    def null_const(tree):
        pass

    @staticmethod
    def string_const(value):
        code = (
            f"\t \t li $t0,{value} \t\t# load constant value to $t0",
            f"\tsw $t0, {bool_size}($sp)\t # add to stack",
        )
        return code
