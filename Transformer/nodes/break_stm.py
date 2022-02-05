from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class BreakStatement(Node):
    def __init__(self, break_id):
        self.break_id = break_id

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.break_statement(symbol_table, self)
