from Transformer.nodes.node import Node


class Assignment(Node):
    def __init__(self, l_value, expr):
        self.l_value = l_value
        self.expr = expr
