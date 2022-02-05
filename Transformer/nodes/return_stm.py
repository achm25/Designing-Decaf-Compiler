from Transformer.nodes.node import Node


class ReturnStatement(Node):
    def __init__(self, statement=None):
        self.statement = statement
