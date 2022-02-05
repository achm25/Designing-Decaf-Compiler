from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class ReadInteger(Node):

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.read_integer()



class ReadLine(Node):

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.read_line()