from lark import Lark, UnexpectedInput
import re


def find_define_word(t):
    final_text = ""
    saved_list = []
    for line in t.splitlines():
        line = line.strip()
        temp_list = line.split(" ", 2)
        if "define" in temp_list:
            if len(temp_list) >= 2:
                saved_list.append({"key": temp_list[1], "value": temp_list[2]})
                line = ""

        if line != "":
            final_text = final_text + line + "\n"
    return final_text, saved_list


def replace_define_word(t, word_list):
    for item in word_list:
        match_reg = r"\b" + item["key"] + r"\b"
        t = re.sub(match_reg, item["value"], t)

    return t


def handleDefine(t):
    text, word_list = find_define_word(t)
    return replace_define_word(text, word_list)


decaf_parser = Lark(
    grammar=r"""
program: macro* (decl)+ -> finalize
macro : "import" STRING 
decl: variable_ass -> pass_up_first_element
    | accessmode variable_decl -> pass_up_first_element
    | accessmode function_decl -> pass_up_first_element
    | class_decl -> pass_up_first_element
    | interface_decl -> pass_up_first_element
    | variable_ass -> pass_up_first_element
variable_decl: variable ";" -> new_variable
variable: type new_identifier -> variable_definition
        | type new_identifier "=" constant

variable_ass: old_identifier "=" constant ";" -> var_assignment    

type: PRIM -> prim_type
    | identifier -> named_type
    | type "[]" | type "[ ]" | type "[  ]"-> array_type

function_decl: type new_identifier "(" formals ")" stmt_block -> new_function
    | "void" new_identifier "(" formals ")" stmt_block -> new_void_function

formals: variable ("," variable)* -> pass_up
    | -> pass_up
class_decl: "class" new_identifier extend_decl implement_decl "{" fields_decl "}" -> new_class
extend_decl: "extends" identifier -> pass_up_first_element
    | -> pass_up_first_element
implement_decl: "implements" identifier ("," identifier)* -> pass_up
    | -> pass_up
fields_decl: (field)* -> pass_up
field:accessmode variable_decl -> pass_up_first_element
    | accessmode function_decl -> pass_up_first_element
accessmode: "public" | "private" |  -> access_mode
interface_decl: "interface" new_identifier "{" (prototype)* "}"
prototype: type new_identifier "(" formals ")" ";"
    | "void" new_identifier "(" formals ")" ";"
stmt_block: "{" (variable_decl)* (stmt)* "}" -> statement_block
stmt: optional_expression ";" -> optional_expresion_statement
    | if_stmt -> pass_up_first_element
    | while_stmt -> pass_up_first_element
    | for_stmt -> pass_up_first_element
    | break_stmt -> pass_up_first_element
    | continue_stmt -> pass_up_first_element
    | return_stmt -> pass_up_first_element
    | print_stmt -> pass_up_first_element
    | stmt_block -> pass_up_first_element
if_stmt: "if" "(" expr ")" stmt ("else" stmt)? -> if_statement
while_stmt: "while" "(" expr ")" stmt -> while_statement
for_stmt: "for" "(" optional_expression ";" expr ";" optional_expression ")" stmt -> for_statement
return_stmt: "return" optional_expression ";" -> return_statement
optional_expression: (expr)? -> pass_up_first_element
break_stmt: "break" ";" -> break_statement
continue_stmt: "continue" ";" -> continue_statement
print_stmt : "Print" "(" expr ("," expr)* ")" ";" -> print_statement

expr: expr1 "||" expr -> logical_or
    | assignment -> pass_up_first_element
    | expr1 -> pass_up_first_element

expr1: expr2 "&&" expr1 -> logical_and
    | expr2 -> pass_up_first_element
expr2: expr3 "==" expr2 -> equals_operation
    | expr3 -> pass_up_first_element
expr3: expr4 "!=" expr3 -> not_equals_operation
    | expr4 -> pass_up_first_element
expr4: expr5 "<" expr4 -> lt_operation
    | expr5 -> pass_up_first_element
expr5: expr6 "<=" expr5 -> lte_operation
    | expr6 -> pass_up_first_element
expr6: expr7 ">" expr6 -> gt_operation
    | expr7 -> pass_up_first_element
expr7: expr8 ">=" expr7 -> gte_operation
    | expr8 -> pass_up_first_element
expr8: expr8plus "+" expr8 -> addition_operation
    | expr8plus -> pass_up_first_element
expr8plus : expr9 "+=" expr8plus -> add_plus
   | expr9 
expr9: expr9 "-" expr9plus -> subtraction_operation
    | expr9plus -> pass_up_first_element
expr9plus : expr10 "-=" expr9plus -> minus_plus
   | expr10 
expr10: expr10plus "*" expr10 -> multiplication_operation
    | expr10plus -> pass_up_first_element
expr10plus : expr11 "*=" expr10plus -> mul_plus
   | expr11 
expr11: expr11 "/" expr11plus -> division_operation
    | expr11plus -> pass_up_first_element
expr11plus : expr12 "/=" expr11plus -> divide_plus
   | expr12 
expr12: expr12 "%" expr12plus -> modulo_operation
    | expr12plus -> pass_up_first_element
expr12plus : expr13 "%=" expr12plus -> baghi_plus
   | expr13 
expr13: "-" expr13  -> minus_operation
    | expr14 -> pass_up_first_element
expr14: "!" expr15 -> not_operation
    | expr15 -> pass_up_first_element
expr15:  constant -> pass_up_first_element
    | "this" -> this_expression
    | call -> pass_up_first_element
    | "ReadInteger" "(" ")" -> read_integer
    | "ReadLine" "(" ")" -> read_line
    | "dtoi" "("expr")"
    | "btoi" "("expr")"
    | "itod" "("expr")"
    | "itob" "("expr")"
    | "new" CLASS_IDENT "("")"  -> initiate_class
    | "new" CLASS_IDENT    
    | l_value -> pass_up_first_element
    | "NewArray" "(" expr "," type ")" -> initiate_array
    | "__func__" ->f
    | "__line__" ->l

assignment: l_value "=" expr -> assignment
l_value: l_value_name -> identifier_l_value
    | expr15 "." identifier -> member_access_l_value
    | "(" expr ")" -> pass_up_first_element
    | "(" expr ")" l_value_name -> pass_up_first_element
l_value_name: l_value_name "[" expr "]" -> array_access_l_value
            | identifier -> identifier_l_value
            | "[" expr "]"

call: identifier "(" actuals ")" -> function_call
    | expr15 "." identifier "(" actuals ")" -> method_call
actuals:  expr ("," expr)* -> pass_up
    | -> pass_up
identifier: IDENT -> identifier
new_identifier: IDENT -> new_identifier
old_identifier: IDENT -> old_identifier
constant: INTEGER -> int_const
    | DOUBLE -> double_const
    | BOOL -> bool_const
    | NULL -> null_const
    | STRING -> string_const
NULL.5: "null"
PRIM.2: "int"
    | "double"
    | "bool"
    | "string"

BOOL.2: "true"
    | "false"

THIS_KW : "this"
DOUBLE.2: /(\d)+\.(\d)*(([Ee])(\+|\-)?(\d)+)?/
IDENT: /\b(?!(this|class|return|while|if|continue|string|string|__func__|itod|itob|dtoi|btoi|__line__|bool|break|else|for|private|public|void|int|double|true|false|bool|string)\b)[a-zA-Z][a-zA-Z0-9_]{0,50}/
CLASS_IDENT :  /\b(?!(int|double|true|false|bool|string)\b)[a-zA-Z][a-zA-Z0-9_]{0,50}/
//FUN_IDENT : /\b(?!(this|class)\b)[a-zA-Z][a-zA-Z0-9_]{0,50}/
STRING : /"(?:[^\\"]|\\.)*"/
HEXADECIMAL: /0[xX][0-9a-fA-F]+/
DECIMAL: /[0-9]+/
INTEGER: HEXADECIMAL
    | DECIMAL
INLINE_COMMENT : /\/\/.*/
MULTILINE_COMMENT : /\/\*(\*(?!\/)|[^*])*\*\//
%ignore INLINE_COMMENT
%ignore MULTILINE_COMMENT
%import common.WS
%import common.CNAME 
%ignore WS
""",
    start="program",
    parser="lalr",
)

if __name__ == '__main__':
    # test()
    test1 = r"""
            int a ;
            a   =   1;
    """

    try:
        # test1 = handleDefine(test1)
        #
        print(decaf_parser.parse(test1).pretty())


    except:
        print("Syntax Error")