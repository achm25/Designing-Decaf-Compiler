from Transformer.nodes.node import Node


class Const(Node):
    def __init__(self, const_type, value):
        self.const_type = const_type
        self.value = value

    def __str__(self):
        const = "Const " + self.const_type + " " + self.value
        return const

