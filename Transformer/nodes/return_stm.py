from Transformer.nodes.node import Node


class ReturnStatement(Node):
    def __init__(self, expr):
        self.expr = expr
