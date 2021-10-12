def find_define_word(t):
    final_text = ""
    saved_list = []
    for line in t.splitlines():
        line = line.strip()
        temp_list = line.split(" ", 2)
        if "define" in temp_list:
            saved_list.append({"key": temp_list[1], "value": temp_list[2]})
            line = ""

        if line != "":
            final_text = final_text + line + "\n"

    return final_text, saved_list


def replace_define_word(t, word_list):
    for item in word_list:
        t = t.replace(item["key"], item["value"])
    return t


def handleDefine(t):
    text, word_list = find_define_word(t)
    return replace_define_word(text, word_list)