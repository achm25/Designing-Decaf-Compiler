class Variable:
    def __init__(self, var_type, identifier):
        self.var_type = var_type
        self.identifier = identifier

    def __str__(self):
        return "Var " + self.var_type + " "
