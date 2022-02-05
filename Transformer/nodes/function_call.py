from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable

class FunctionCall(Node):
    def __init__(self, identifier, params):
        self.identifier = identifier
        self.params = params


    def cgen(self, symbol_table: SymbolTable):
        print("function call cgen")
        return CodeGenerator.function_call(symbol_table, self)
