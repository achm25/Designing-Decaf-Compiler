import ply.lex as lex
from handle_define import handleDefine
from tokenizer import lexer
from format_converter import judgment_format



# Test it out
data = r'''
define SEMICOLON ;
define FOR100 for(i = 0; i < 100; i += 1)

FOR100
Print(i)SEMICOLON
'''


# Give the lexer some input
lexer.input(handleDefine(data))



# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)  #more option for print
    judgment_format(tok)
