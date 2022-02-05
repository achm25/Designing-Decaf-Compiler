from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class StatementBlock(Node):
    def __init__(self, block_statements):
        self.block_statements = block_statements

    def cgen(self, symbol_table: SymbolTable):
        print("block cgen")
        return CodeGenerator.statement_block(symbol_table, self)
