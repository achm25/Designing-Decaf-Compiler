from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class ForStatement(Node):
    def __init__(self, init, condition, update, block, for_id):
        self.init = init
        self.condition = condition
        self.update = update
        self.block = block
        self.for_id = for_id

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.for_statement(symbol_table, self)
