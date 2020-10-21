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
    i = 0
    while string[i] == ' ':
      string = string[1:]
    while string[len(string)-1] == ' ':
        string = string[:-1]
    i = 1
    while i < len(string)-1:
        if string[i] == ' ' and string[i+1] == ' ':
            string = string[:i+1] + string[i+2:]
        else:
            i += 1
    return string


string = "  Hello   World  "

print(len_string(string))
char = str(input("Searching symbol: "))
print(charAt(string, char))
print(trim(string))
