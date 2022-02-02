from .scope import Scope


class SymbolTable:
    def __init__(self):
        self.global_scope = Scope()
        self.current_scope = self.global_scope
        self.local_offset = 0

    def new_scope(self):
        new_scope = Scope(parent_scope=self.current_scope)
        self.current_scope = new_scope
        return new_scope


