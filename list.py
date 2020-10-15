A = [2, 1, 4, 23, 35, -10, -56, 44, 78, 9,]
A_max = A[0]
for element in A:
    if element > A_max:
        A_max = element
print(A_max)
A_min = A[0]
for element in A:
    if element < A_min:
        A_min = element
print(A_min)

x = int(input("Find number: "))
for i in A:
    if i == x:
        print(True)
        break
    else:
        print(False)
        break
s = 0
for o in A:
    s += o
    print(s)
