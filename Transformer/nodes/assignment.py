from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class Assignment(Node):
    def __init__(self, l_value, expr):
        self.l_value = l_value
        self.expr = expr

    def cgen(self, symbol_table: SymbolTable):
        print("ASSIGN")
        return CodeGenerator.assignment(symbol_table, self)

