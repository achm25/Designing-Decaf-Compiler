from Transformer.nodes.node import Node


class PrintNode(Node):
    def __init__(self, expr):
        self.expr = expr
