# length() - размер строки
A = "Hello World"
def len_string (A):
    i = 0
    while A[i:]:
        i += 1
    return i
print(len_string(A))

# charAt() - первое вхождение элемента
# я хотел глянуть как рабоат метод ".find" для проверки работы функции
string1 = str(input("Type something: "))
serth_s1 = str(input("Searching symbol: "))
res1 = string1.find(serth_s1)
print(res1)


string = str(input("Type something: "))
serth_s = str(input("Searching symbol: "))
def charAt(string, serth_s):
    count = 0
    for value in string:
        if value ==serth_s:
            return count 
        count+=1
    return -1
res = charAt(string, serth_s)
print(res)

# trim() - удалить все лишние пробелы 
input_string = input()
i = 0
while input_string[i] == ' ':
    input_string = input_string[1:]
while input_string[len(input_string)-1] == ' ':
    input_string = input_string[:-1]
i = 1
while i < len(input_string)-1:
    if input_string[i] == ' ' and input_string[i+1] == ' ':
        input_string = input_string[:i+1] + input_string[i+2:]
    else:
        i += 1
print(input_string)
