decaf_grammer = r"""
program : (decl)+
decl : variabledecl | functiondecl | classdecl
variabledecl :  variable";"
variable : type ident
type : "int" | "double" | "bool" | "string" | "ident" | type "[""]"
functiondecl : type ident "("formals")" stmtblock |"void" ident "("formals")" stmtblock
formals : variable+"," | 
classdecl : "class" ident "{" (field)* "}"
field : accessmode variabledecl | accessmode functiondecl
accessmode : "private" | "public" | 
stmtblock : "{"(variabledecl)* (stmt)*"}"
stmt : (expr)?";" | ifstmt | whilestmt | forstmt |breakstmt | continuestmt | returnstmt |printstmt | stmtblock
ifstmt : "if" "("expr")" stmt optional_else_expression
optional_else_expression: ("else"stmt)? -> pass_up_first_element
whilestmt : "while" "("expr")" stmt
forstmt : "for" "("optional_expression";" expr";"optional_expression")" stmt
optional_expression: (expr)? -> pass_up_first_element
returnstmt : "return" (expr)?";"
breakstmt : "break"";"
continuestmt : "continue"";"
printstmt : "Print" "("expr+","")"";" | "Print" "("expr+","")"";"
expr : lvalue "=" expr | lvalue "+=" expr | lvalue "−=" expr| lvalue "∗=" expr | lvalue "/=" expr | constant | lvalue | "this" | call | "("expr")" |expr "+" expr | expr "−" expr | expr "∗" expr | expr "/" expr |expr "%" expr | "−"expr | expr "<" expr | expr "<=" expr |expr ">" expr | expr ">=" expr | expr "==" expr | expr "!=" expr |expr "&&" expr | expr "||" expr | "!"expr | "ReadInteger" "(" ")" | "ReadLine" "(" ")" | "new"  ident | "NewArray" "(" expr "," type ")" | "itod" "(" expr ")" | "dtoi" "("expr")" | "itob" "(" expr ")" | "btoi" "(" expr ")" | "__func__" | "__line__"
lvalue : ident | expr "." ident | expr"["expr"]"
call : ident "("actuals")" | expr "." ident "("actuals")"
actuals : expr+"," | 
constant: INTEGER -> int_const
    | DOUBLE -> double_const
    | BOOL -> bool_const
    | NULL -> null_const
    | STRING -> string_const
ident: IDENTNAME -> new_identifier
IDENTNAME: /[a-zA-Z][a-zA-Z0-9_]{0,30}/
NULL.5: "null"
PRIM.2: "int"
    | "double"
    | "bool"
    | "string"
BOOL.2: "true"
    | "false"
DOUBLE.2: /(\d)+\.(\d)*(([Ee])(\+|\-)?(\d)+)?/
IDENT: /[a-zA-Z][a-zA-Z0-9_]{0,30}/
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
%ignore WS
"""