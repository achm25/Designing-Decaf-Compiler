from Transformer.nodes.node import Node
from phase3.code_generator import CodeGenerator
from phase3.symbol_table import SymbolTable


class ReadInteger(Node):

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.read_integer()



class ReadLine(Node):
    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.read_line()


class Func_(Node):
    def __init__(self):
        self.name = "__func__"


    def __str__(self):
        const = "__func__"
        return const

    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.func_(symbol_table,self)


class Line_(Node):
    def __init__(self):
        self.name = "__line__"


    def __str__(self):
        const = "__line__"
        return const
    def cgen(self, symbol_table: SymbolTable):
        return CodeGenerator.line_(symbol_table,self)