from Transformer.code_generator import CodeGenerator
from Transformer.nodes.node import Node
from Transformer.symbol_table import SymbolTable


class Variable(Node):
    def __init__(self, var_type, identifier):
        self.var_type = var_type
        self.identifier = identifier
        self.local_offset = 0
        self.is_global = False
        self.is_in_class = False
        self.is_func_param = False

    def __str__(self):
        return "Var " + str(self.var_type) + str(self.identifier)

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.new_variable(symbol_table, self)
