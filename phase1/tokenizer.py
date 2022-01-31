import ply.lex as lex
from phase1.constants import *

reserved = reserved_words

# List of token names.This is always required
tokens = [ID,
          HEXADECIMAL,
          FLOATNUMBER,
          INTNUMBER,
          STRINGLITERAL,
          BOOLEAN,
          EQUAL,
          NOTEQUAL,
          GREATEREQUALS,
          MINUSEQUAL,
          PLUSEQUAL,
          LESSEQUAL,
          AND,
          OR,
          MINUS,
          SIGNS,
          ] + list(reserved.values())

# Regular expression rules for simple tokens
t_SIGNS = r"[-@_!+#$%^&*()<>?/|}{~:=,;\[\]]"


# A regular expression rule with some action code

def t_COMMENT(t):
    r'//.*|(\/\*[\s\S]*?\*\/)'
    pass


def t_AND(t):
    r'\&&'
    return t


def t_OR(t):
    r'\|{2}'
    return t


def t_LESSEQUAL(t):
    r'\<='
    return t


def t_MINUSEQUAL(t):
    r'\-='
    return t


def t_GREATEREQUALS(t):
    r'\>='
    return t


def t_MINUS(t):
    r'\>='
    return t


def t_NOTEQUAL(t):
    r'\!='
    return t


def t_PLUSEQUAL(t):
    r'\+='
    return t


def t_EQUAL(t):
    r'={2}'
    return t


def t_HEXADECIMAL(t):
    r'\b0x[0-9A-z]+\b'
    return t


def t_FLOATNUMBER(t):
    r'\b[+]?\d+\.\d*[Ee][\+\-]?\d+\b|[+]?\d*\.\d*'
    t.value = t.value
    return t


def t_INTNUMBER(t):
    r'[+]?\d+'
    t.value = int(t.value)
    return t


def t_BOOLEAN(t):
    r'\btrue\b|\bfalse\b'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_STRINGLITERAL(t):
    r"'(\\'|[^'])*(?!<\\)'|\"(\\\"|[^\"])*(?!<\\)\""
    return t


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