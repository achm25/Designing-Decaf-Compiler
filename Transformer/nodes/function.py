from Transformer.code_generator import CodeGenerator
from Transformer.nodes.node import Node
from Transformer.symbol_table import SymbolTable


class Function(Node):
    def __init__(self, return_type, identifier, params, block, parent_class = None):
        self.return_type = return_type
        self.identifier = identifier
        self.params = params
        self.block = block
        self.label = identifier.name
        self.parent_class = parent_class

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.new_function(symbol_table, self)


