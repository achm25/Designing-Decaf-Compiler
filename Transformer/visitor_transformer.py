"""
    Transformers visit each node of the tree, and run the appropriate method on it according to the node's data.
    lark link: https://lark-parser.readthedocs.io/en/latest/visitors.html
    sample code link: https://github.com/lark-parser/lark/blob/master/lark/visitors.py
"""

from lark import Transformer

class DecafVisitor(Transformer):
    def new_function__init__(self):
        super().__init__()
    
    def pass_up(self, args):
        return args

    def pass_up_first_element(self, args):
        if len(args) == 0:
            return None
        return args[0]

    def new_function(self, args):
        return_type, function_identifier, function_parameters, function_body = args
        code = [
            f"check:",
            "\tsubu $sp, $sp, 8\t# decrement sp to make space to save ra, fp",
            "\tsw $fp, 8($sp)\t# save fp",
            "\tsw $ra, 4($sp)\t# save ra",
            "\taddiu $fp, $sp, 8\t# set up new fp",
        ]
        return code
        