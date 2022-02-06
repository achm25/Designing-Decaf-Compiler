from optimizer_scope import *

class Optimizer:
    def __init__(self):
        self.global_scope = OptimizerScope(label="root",parent_scope=None)
        self.current_scope = self.global_scope
        self.scopes = {}



    def get_scope(self,label):
        return self.scopes[label]

    def add_scope(self,scope):
        self.scopes[scope.label] = scope

    def new_scope(self,name):
        new_scope = OptimizerScope(label=name,parent_scope=self.current_scope)
        self.current_scope = new_scope
        self.add_scope(new_scope)
        return new_scope


    def end_see_new_scope(self):
        self.current_scope = self.current_scope.parent_scope
        return


    def see_new_var(self,symbol):
        self.current_scope.add_symbol(symbol)