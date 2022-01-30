class Class:
    def __init__(self, scope, name, variables = {} , functions = {}):
        self.scope = scope
        self.name = name
        self.variables = variables
        self.functions = functions