class Function:
    def __init__(self, scope, name, return_type=None, func_vars = None):
        self.scope = scope
        self.name = name
        self.return_type = return_type
        self.func_vars = func_vars