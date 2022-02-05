from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class Variable(Node):
    def __init__(self, v_type, identifier):
        self.v_type = v_type
        self.identifier = identifier
        self.local_offset = 0
        self.is_global = False
        self.is_in_class = False
        self.is_func_param = False

    def __str__(self):
        return "Var " + str(self.v_type) + str(self.identifier)

    def cgen(self, symbol_table: SymbolTable):
        print("var cgen")
        return CodeGenerator.new_variable(symbol_table, self)
