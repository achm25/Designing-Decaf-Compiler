class Scope:
    def __init__(self, name, parent_scope=None):
        self.name = name
        self.parent_scope = parent_scope
        self.symbols = {}

    def add_symbol(self, symbol):
        self.symbols[symbol.name] = symbol

    #TODO ID

    def __str__(self):
        return self.name