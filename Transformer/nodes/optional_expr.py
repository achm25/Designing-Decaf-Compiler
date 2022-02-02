from Transformer.nodes.node import Node


class OptionalExpr(Node):
    def __init__(self, expr):
        self.expr = expr
