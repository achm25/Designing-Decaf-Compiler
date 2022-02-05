from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class Expression(Node):
    def __init__(self, operator, r_operand, l_operand):
        self.operator = operator
        self.l_operand = l_operand
        self.r_operand = r_operand

    def cgen(self, symbol_table: SymbolTable):

        l_operand_type = CodeGenerator.get_type(self.l_operand, symbol_table)
        r_operand_type = CodeGenerator.get_type(self.r_operand, symbol_table)

        if l_operand_type != r_operand_type:
            print("Semantic Error type2")
            return []

        if self.operator == 'add':
            return CodeGenerator.addition_operation(symbol_table, self)
        elif self.operator == 'sub':
            return CodeGenerator.subtraction_operation(symbol_table, self)
        elif self.operator == 'mult':
            return CodeGenerator.multiplication_operation(symbol_table, self)
        elif self.operator == 'div':
            return CodeGenerator.division_operation(symbol_table, self)
        elif self.operator == 'modulo':
            return CodeGenerator.modulo_operation(symbol_table, self)
        elif self.operator == 'lt':
            return CodeGenerator.lt_operation(symbol_table, self)
        elif self.operator == 'gt':
            return CodeGenerator.gt_operation(symbol_table, self)
        elif self.operator == 'gte':
            return CodeGenerator.gte_operation(symbol_table, self)
        elif self.operator == 'lte':
            return CodeGenerator.lte_operation(symbol_table, self)
        elif self.operator == 'and':
            return CodeGenerator.logical_and(symbol_table, self)
        elif self.operator == 'or':
            return CodeGenerator.logical_or(symbol_table, self)
        elif self.operator == 'equals':
            return CodeGenerator.equals_operation(symbol_table, self)
        elif self.operator == 'not_equals':
            return CodeGenerator.not_equals_operation(symbol_table, self)