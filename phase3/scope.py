class Scope:
    def __init__(self, name=None, parent_scope=None):
        self.name = name
        self.parent_scope = parent_scope
        self.symbols = {}

    def add_symbol(self, symbol):
        self.symbols[symbol.identifier.name] = symbol

    def find_symbol(self, symbol):
        if symbol in self.symbols:
            return self.symbols[symbol]
        if self.parent_scope is not None:
            return self.parent_scope.find_symbol(symbol)
        else:
            raise Exception("not found!")
