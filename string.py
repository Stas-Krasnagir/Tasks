def len_string(string):
    i = 0
    while string[i:]:
        i += 1
    return i

def charAt(string, char):
    count = 0
    for value in string:
        if value == char:
            return count 
        count += 1
    return -1

def trim(string):
    new_string = ""
    for i, ch in enumerate(string):
        if ch == " ":
            if len(string) != i + 1 and string[i + 1] != " ":
                new_string = new_string + ch
        else:
            new_string = new_string + ch
    if new_string[0] == " ":
        new_string = new_string[1:]
    if new_string[-1] == " ":
        new_string = new_string[:-2]
    return new_string


def replace_str(string, old_value, new_value):
    new_string = ""
    len_ov = len(old_value)
    skip = 0
    len_st = len(string)
    for i in range(len_st):
        if skip == 0 and string[i: i + len_ov] == old_value:
            new_string = new_string + new_value
            skip = len_ov - 1
        elif skip != 0:
            skip -= 1
        else:
            new_string = new_string + string[i]
    return new_string

string = "  Hello  new  World  "

print(len_string(string))
char = str(input("Searching symbol: "))
print(charAt(string, char))
print(trim(string))

old_value = "new"
new_value = "wonderful"
print(replace_str(string, old_value, new_value))
