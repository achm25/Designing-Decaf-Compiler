from Transformer.nodes.node import Node


class Identifier(Node):
    def __init__(self, name, i_type=None):
        self.name = name
        self.i_type = i_type

    def __str__(self):
        return "Identifier " + self.name


class IdentifierLValue(Node):
    def __init__(self, identifier):
        self.identifier = identifier
