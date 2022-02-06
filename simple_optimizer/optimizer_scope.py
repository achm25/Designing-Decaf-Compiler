class OptimizerScope:
    def __init__(self, label, parent_scope=None):
        self.label = label
        self.parents_scope = []
        self.symbols = {}
        if parent_scope is not None:
            self.parents_scope.append(parent_scope)


    def add_parent(self,parent_scope):
        self.parents_scope.append(parent_scope)


    def add_symbol(self, symbol):
        self.symbols[symbol.name] = symbol


    def find_symbol(self,symbol):
        if symbol in self.symbols:
            return self.symbols[symbol]
        if self.parent_scope is not None:
            return self.parent_scope.find_symbol(symbol)


    def __str__(self):
        return self.name



