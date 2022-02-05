from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class WhileStatement(Node):
    def __init__(self, condition, block, while_id):
        self.condition = condition
        self.block = block
        self.while_id = while_id

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.while_statement(symbol_table, self)
