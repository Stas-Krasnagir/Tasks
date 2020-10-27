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
    return new_string

def replace_str(string, old_value, new_value):
    index_of_old_value_in_string = string.find(old_value)
    len_of_old_value = len(old_value)
    new_string = string[ :index_of_old_value_in_string] + new_value + string[index_of_old_value_in_string + len_of_old_value : ]
    return new_string

string = "  Hello  new  World  "

print(len_string(string))
char = str(input("Searching symbol: "))
print(charAt(string, char))
print(trim(string))

old_value = "new"
new_value = "wonderful"
print(replace_str(string, old_value, new_value))
