from Transformer.nodes.node import Node


class MinusExpression(Node):
    def __init__(self, expression):
        self.expression = expression
