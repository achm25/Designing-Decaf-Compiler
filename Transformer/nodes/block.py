from Transformer.code_generator import CodeGenerator
from Transformer.nodes.node import Node
from Transformer.symbol_table import SymbolTable


class StatementBlock(Node):
    def __init__(self, block_statements):
        self.block_statements = block_statements

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.statement_block(symbol_table, self)
