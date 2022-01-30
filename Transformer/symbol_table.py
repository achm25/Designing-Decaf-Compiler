from .scope import Scope


class Symbol:
    def __init__(self, name, type, value=None, scope=None, label=None):
        self.name = name
        self.type = type
        self.value = value
        self.scope = scope
        self.label = label
        if(scope):
            scope.add_symbol(self)

    def set_value(self, value):
        self.value = value

    def set_scope(self, scope):
        self.scope = scope
        scope.add_symbol(self)

    def set_label(self, label):
        self.label = label


class SymbolTable():
    def __init__(self):
        super().__init__()
        self.stack = []
        self.functions = {}
        self.classes = {}

    def push_scope(self, scope):
        self.stack.append(scope)

    def pop_scope(self):
        return self.stack.pop()

    def get_current_scope(self):
        return self.stack[-1]

    def push_symbol(self, symbol):
        cur_scope = self.get_current_scope()
        symbol.set_scope(cur_scope)
        cur_scope.add_symbol(symbol)

    def lookup_symbol(self, name):
        cur_scope = self.get_current_scope()
        search_stack = [cur_scope]
        while(len(search_stack) != 0):
            scope = search_stack.pop()
            if name in scope.symbols:
                return scope.symbols[name]
            #TODO search all parents
            search_stack.append(scope.parent_scope)
            #TODO raise error if not found

    def push_function(self, function):
        self.functions[function.name] = function

    def lookup_function(self, name):
        if name in self.functions:
            return self.functions[name]

    def push_class(self, class_obj):
        self.classes[class_obj.name] = class_obj

    def lookup_class(self, name):
        if name in self.classes:
            return self.classes[name]