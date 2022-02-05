from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class Const(Node):
    def __init__(self, v_type, value):
        self.v_type = v_type
        self.value = value

    def __str__(self):
        const = "Const " + self.v_type + " " + self.value
        return const

    def cgen(self, symbol_table: SymbolTable):
        if self.v_type == 'int':
            return CodeGenerator.int_const(self.value)
        elif self.v_type == 'bool':
            return CodeGenerator.bool_const(self.value)
        elif self.v_type == 'string':
            return CodeGenerator.string_const(self.value)
        elif self.v_type == 'double':
            return CodeGenerator.double_const(self.value)
        elif self.v_type == 'null':
            return CodeGenerator.null_const(symbol_table)
