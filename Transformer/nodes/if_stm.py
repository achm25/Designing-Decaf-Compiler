from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class IfStatement(Node):
    def __init__(self, condition, block, if_id, else_block=None):
        self.condition = condition
        self.block = block
        self.else_block = else_block
        self.if_id = if_id

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.if_statement(symbol_table, self)
