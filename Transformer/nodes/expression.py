from Transformer.nodes.node import Node


class Expression(Node):
    def __init__(self, operator, r_operand, l_operand):
        self.operator = operator
        self.l_operand = l_operand
        self.r_operand = r_operand

