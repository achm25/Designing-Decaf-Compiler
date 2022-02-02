from Transformer.nodes.node import Node


class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Identifier " + self.name


class IdentifierLValue(Node):
    def __init__(self, identifier):
        self.identifier = identifier
