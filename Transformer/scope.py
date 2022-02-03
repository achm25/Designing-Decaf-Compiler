class Scope:
    def __init__(self, name, parent_scope=None):
        self.name = name
        self.parent_scope = parent_scope
        self.symbols = {}

    def add_symbol(self, symbol):
        self.symbols[symbol.name] = symbol


    def find_symbol(self,symbol):
        if symbol in self.symbols:
            return symbols[symbol]
        if self.parent_scope is not None:
            return self.parent_scope.find_symbol(symbol)
        else:
            raise Exception("not found!")





    #TODO ID

    def __str__(self):
        return self.name