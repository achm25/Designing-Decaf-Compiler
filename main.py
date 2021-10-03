import ply.lex as lex

# define token name here
ID = 'ID'
HEXADECIMAL = 'HEXADECIMAL'
FLOATNUMBER = 'FLOATNUMBER'
INTNUMBER = 'INTNUMBER'
EQUAL = 'EQUAL'
NOTEQUAL = 'NOTEQUAL'
GREATEREQUALS = 'GREATEREQUALS'
LESSEQUAL = 'LESSEQUAL'
SIGNS = 'SIGNS'
AND = 'AND'
OR = 'OR'
MINUS = 'MINUS'
BOOLEAN = 'BOOLEAN'

reserved = {
    '__func__': '__func__',
    '__line__': '__line__',
    'bool': 'bool',
    'break': 'break',
    'btoi': 'btoi',
    'class': 'class',
    'continue': 'continue',
    'define': 'define',
    'double': 'double',
    'dtoi': 'dtoi',
    'else': 'else',
    'for': 'for',
    'if': 'if',
    'import': 'import',
    'int': 'int',
    'itob': 'itob',
    'itod': 'itod',
    'new': 'new',
    'NewArray': 'NewArray',
    'null': 'null',
    'Print': 'Print',
    'private': 'private',
    'public': 'public',
    'ReadInteger': 'ReadInteger',
    'ReadLine': 'ReadLine',
    'return': 'return',
    'string': 'string',
    'this': 'this',
    'void': 'void',
    'while': 'while',
}

# List of token names.This is always required
tokens = [ID,
          HEXADECIMAL,
          FLOATNUMBER,
          INTNUMBER,
          BOOLEAN,
          EQUAL,
          NOTEQUAL,
          GREATEREQUALS,
          LESSEQUAL,
          AND,
          OR,
          MINUS,
          SIGNS,
          ] + list(reserved.values())

# Regular expression rules for simple tokens
t_SIGNS = r"[@_!+#$%^&*()<>?/|}{~:=,;\[\]]"


# A regular expression rule with some action code

def t_AND(t):
    r'\&&'
    return t


def t_OR(t):
    r'\|{2}'
    return t


def t_LESSEQUAL(t):
    r'\<='
    return t


def t_GREATEREQUALS(t):
    r'-'
    return t


def t_MINUS(t):
    r'\>='
    return t


def t_NOTEQUAL(t):
    r'\!='
    return t


def t_EQUAL(t):
    r'={2}'
    return t


def t_HEXADECIMAL(t):
    r'\b0x[0-9A-z]+\b'
    return t


def t_FLOATNUMBER(t):
    r'[-+]?\d*\.\d*'
    t.value = float(t.value)
    return t


def t_INTNUMBER(t):
    r'[-+]?\d+'
    t.value = int(t.value)
    return t


def t_BOOLEAN(t):
    r'\btrue\b|\bfalse\b'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
{-123-a35,id3a,+*;}[||===!=()&&]<><=>==
    a[24]="7"; n!=if;
false,-if;true32;
forpar

'''

# Give the lexer some input
lexer.input(data)


def judgment_format(token):
    if token.type == ID:
        print("T_ID", tok.value)
    elif token.type in reserved.values():
        print(tok.value)
    elif token.type == INTNUMBER:
        print("T_INTLITERAL", tok.value)
    elif token.type == FLOATNUMBER:
        print("T_DOUBLELITERAL", tok.value)
    elif token.type == HEXADECIMAL:
        print("T_INTLITERAL", tok.value)
    elif token.type == BOOLEAN:
        print("T_BOOLEANLITERAL", tok.value)
    else:
        print(tok.value)


# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    # print(tok.type, tok.value, tok.lineno, tok.lexpos)  #more option for print
    judgment_format(tok)
