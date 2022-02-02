from Transformer.nodes.node import Node


class PrimType(Node):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Prim " + self.name


