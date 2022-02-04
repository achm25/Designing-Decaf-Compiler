from Transformer.nodes.return_stm import ReturnStatement

int_size = 4
double_size = 8
string_size = 1
bool_size = 1


class CodeGenerator:

    @staticmethod
    def pass_up_first_element(symbol_table):
        pass

    @staticmethod
    def new_variable(symbol_table, variable):
        code = []
        current_scope = symbol_table.new_scope()
        current_scope.push_symbol(variable)

        size = int_size
        if variable.var_type == "double":
            size = 8

        if not (variable.is_global or variable.is_in_class or variable.is_func_param):
            variable.local_offset = symbol_table.local_offset
            symbol_table.local_offset += size
            code += [
                f"\tsubu $sp, $sp, {size}\t# Decrement sp to make space for variable {variable.identifier.name}."
            ]
        return code

    @staticmethod
    def variable_definition(symbol_table):
        pass

    @staticmethod
    def prim_type(symbol_table):
        pass

    @staticmethod
    def named_type(symbol_table):
        pass

    @staticmethod
    def array_type(symbol_table):
        pass

    @staticmethod
    def new_function(symbol_table, function):
        symbol_table.local_offset = 0
        if function.parent_class is not None:
            function.label = (
                f"{function.parent_class.identifier.name}_{function.identifier.name}"
            )
        curr_scope = symbol_table.new_scope()
        for param in function.params:
            curr_scope.push_symbol(param)
        code = [
            f"{function.label}:",
            "\tsubu $sp, $sp, 8\t# decrement sp to make space to save ra, fp",
            "\tsw $fp, 8($sp)\t# save fp",
            "\tsw $ra, 4($sp)\t# save ra",
            "\taddiu $fp, $sp, 8\t# set up new fp",
        ]
        code += function.block.cgen(symbol_table)
        code += [
            "\tmove $sp, $fp\t\t# pop callee frame off stack",
            "\tlw $ra, -4($fp)\t# restore saved ra",
            "\tlw $fp, 0($fp)\t# restore saved fp",
            "\tjr $ra\t\t# return from function",
        ]
        # Reset
        symbol_table.local_offset = 0
        symbol_table.current_scope = curr_scope.parent_scope
        return code

    @staticmethod
    def new_void_function(symbol_table):
        pass

    @staticmethod
    def pass_up(symbol_table):
        pass

    @staticmethod
    def new_class(symbol_table):
        pass

    @staticmethod
    def access_mode(symbol_table):
        pass

    @staticmethod
    def statement_block(symbol_table, block):
        curr_scope = symbol_table.new_scope()
        code = []

        for statement in block.block_statements:
            statement.cgen(symbol_table)
            if isinstance(statement, ReturnStatement):
                break

        # Pop variables in order to correct local offset
        # TODO
        # freed_space = symbol_table.pop_variables_till_block(
        #     symbol_table.get_current_scope(), curr_scope
        # )
        # code.append(f"\taddiu $sp, $sp, {freed_space} # Freed space")
        # Clean block scope cause we are out of the block
        symbol_table.current_scope = curr_scope.parent_scope
        return code

    @staticmethod
    def optional_expression_statement(symbol_table, node):
        pass

    @staticmethod
    def if_statement(symbol_table):
        pass

    @staticmethod
    def while_statement(symbol_table):
        pass

    @staticmethod
    def for_statement(symbol_table):
        pass

    @staticmethod
    def return_statement(symbol_table):
        pass

    @staticmethod
    def pass_up_first_element(symbol_table):
        pass

    @staticmethod
    def break_statement(symbol_table):
        pass

    @staticmethod
    def continue_statement(symbol_table):
        pass

    @staticmethod
    def print_statement(symbol_table):
        pass

    @staticmethod
    def logical_or(symbol_table):
        pass

    @staticmethod
    def logical_and(symbol_table):
        pass

    @staticmethod
    def equals_operation(symbol_table):
        pass

    @staticmethod
    def not_equals_operation(symbol_table):
        pass

    @staticmethod
    def lt_operation(symbol_table):
        pass

    @staticmethod
    def lte_operation(symbol_table):
        pass

    @staticmethod
    def gt_operation(symbol_table):
        pass

    @staticmethod
    def gte_operation(symbol_table):
        pass

    @staticmethod
    def addition_operation(symbol_table):
        pass

    @staticmethod
    def add_plus(symbol_table):
        pass

    @staticmethod
    def subtraction_operation(symbol_table):
        pass

    @staticmethod
    def minus_plus(symbol_table):
        pass

    @staticmethod
    def multiplication_operation(symbol_table):
        pass

    @staticmethod
    def mul_plus(symbol_table):
        pass

    @staticmethod
    def division_operation(symbol_table):
        pass

    @staticmethod
    def divide_plus(symbol_table):
        pass

    @staticmethod
    def modulo_operation(symbol_table):
        pass

    @staticmethod
    def baghi_plus(symbol_table):
        pass

    @staticmethod
    def minus_operation(symbol_table):
        pass

    @staticmethod
    def not_operation(symbol_table):
        pass

    @staticmethod
    def this_expression(symbol_table):
        pass

    @staticmethod
    def read_integer(symbol_table):
        pass

    @staticmethod
    def read_line(symbol_table):
        pass

    @staticmethod
    def initiate_class(symbol_table):
        pass

    @staticmethod
    def f(symbol_table):
        pass

    @staticmethod
    def l(self, symbol_table):
        pass

    @staticmethod
    def assignment(symbol_table):
        pass

    @staticmethod
    def identifier_l_value(symbol_table):
        pass

    @staticmethod
    def member_access_l_value(symbol_table):
        pass

    @staticmethod
    def array_access_l_value(symbol_table):
        pass

    @staticmethod
    def identifier_l_value(symbol_table):
        pass

    @staticmethod
    def function_call(symbol_table):
        pass

    @staticmethod
    def method_call(symbol_table):
        pass

    @staticmethod
    def identifier(symbol_table):
        pass

    @staticmethod
    def new_identifier(symbol_table):
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
        # todo handle .e and .
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
    def null_const(symbol_table):
        pass

    @staticmethod
    def string_const(value):
        code = (
            f"\t \t li $t0,{value} \t\t# load constant value to $t0",
            f"\tsw $t0, {bool_size}($sp)\t # add to stack",
        )
        return code
