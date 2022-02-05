class Scope:
    # we need it to find out what decereation in this scope for which one , help us to add it to .data
    block_counter: int = 0
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

    def root_generator(self):

        if self.parent_scope is None:
            return self.name

        name = ""
        root = self.parent_scope
        while root is not None:
            name = root.name + "_" + name
            root = root.parent_scope

        return name + self.name