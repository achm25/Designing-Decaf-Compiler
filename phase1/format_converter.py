from constants import *


def judgment_format(token):
    if token.type == ID:
        print("T_ID", token.value)
    elif token.type in reserved_words.values():
        print(token.value)
    elif token.type == INTNUMBER:
        print("T_INTLITERAL", token.value)
    elif token.type == STRINGLITERAL:
        print("T_STRINGLITERAL", token.value)
    elif token.type == FLOATNUMBER:
        print("T_DOUBLELITERAL", token.value)
    elif token.type == HEXADECIMAL:
        print("T_INTLITERAL", token.value)
    elif token.type == BOOLEAN:
        print("T_BOOLEANLITERAL", token.value)
    else:
        print(token.value)


def judgment_format_write(token):
    if token.type == ID:
        # print("T_ID", token.value)
        return "T_ID" + " " +str(token.value)
    elif token.type in reserved_words.values():
        # print(token.value)
        return str(token.value)
    elif token.type == INTNUMBER:
        # print("T_INTLITERAL", token.value)
        return "T_INTLITERAL" + " " + str(token.value)
    elif token.type == STRINGLITERAL:
        # print("T_STRINGLITERAL", token.value)
        return "T_STRINGLITERAL" + " " +str(token.value)
    elif token.type == FLOATNUMBER:
        # print("T_DOUBLELITERAL", token.value)
        return "T_DOUBLELITERAL" + " " +str(token.value)
    elif token.type == HEXADECIMAL:
        # print("T_INTLITERAL", token.value)
        return "T_INTLITERAL" + " " +str(token.value)
    elif token.type == BOOLEAN:
        # print("T_BOOLEANLITERAL", token.value)
        return "T_BOOLEANLITERAL" + " " +str(token.value)
    else:
        # print(token.value)
        return str(token.value)
