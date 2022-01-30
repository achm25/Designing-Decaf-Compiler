
from enum import Enum

PRIMITIVE_TYPES = {"int", "double", "bool", "string"}

class PrimitiveTypes(Enum):
    INT = "int"
    DOUBLE = "double"
    BOOL = "bool"
    STRING = "string"
    NULL = "null"

class Type:
    def __init__(self, name):
        self.name = name
    double = "double"
    int = "int"
    bool = "bool"
    string = "string"
    array = "array"
    null = "null"

    def __eq__(self, other):
        if isinstance(other, Type):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other
        elif isinstance(other, PrimitiveTypes):
            return self.name == other.value
        return False

    def is_primitive(self):
        return isinstance(PrimitiveTypes)
        #TODO CHECK


