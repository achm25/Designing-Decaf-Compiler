from phase3.scope import Scope


class SymbolTable:

    def __init__(self):
        self.global_scope = Scope(name= "root")
        self.current_scope = self.global_scope
        self.local_offset = 0
        self.data_storage = []

    def new_scope(self,name):
        new_scope = Scope(name=name, parent_scope=self.current_scope)
        self.current_scope = new_scope
        return new_scope

    def end_see_new_scope(self):
        self.current_scope = self.current_scope.parent_scope
        return

    def see_new_var(self,symbol):
        self.current_scope.add_symbol(symbol)


