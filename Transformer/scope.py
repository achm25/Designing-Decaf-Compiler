
class Symbol:
    def __init__(self, name, value=None, label=None):
        self.name = name
        self.value = value
        self.label = label

    def set_value(self, value):
        self.value = value

    def set_label(self, label):
        self.label = label


class Scope:
    def __init__(self, name=None, parent_scope=None):
        self.name = name
        self.parent_scope = parent_scope
        self.symbols = dict()

    def add_symbol(self, symbol):
        self.symbols[symbol.name] = symbol

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.parent_scope is None:
            print(f"Error. Variable {name} not found.")
        else:
            return self.parent_scope.lookup(name)

    def push_symbol(self, symbol):
        self.symbols[symbol.identifier.name] = symbol

    def __str__(self):
        return self.symbols
