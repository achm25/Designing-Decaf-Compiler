import ply.lex as lex

# List of token names.This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

reserved = {
    '__func__': '',
    '__line__': '',
    'bool': '',
    'break': '',
    'btoi': '',
    'class': '',
    'continue': '',
    'define': '',
    'double': '',
    'dtoi': '',
    'else': '',
    'for': '',
    'if': '',
    'import': '',
    'int': '',
    'itob': '',
    'itod': '',
    'new': '',
    'NewArray': '',
    'null': '',
    'Print': '',
    'private': '',
    'public': '',
    'ReadInteger': '',
    'ReadLine': '',
    'return': '',
    'string': '',
    'this': '',
    'void': '',
    'while': '',
}
