def max_element(list):
    max_result = list[0]
    for element in list:
        if element > max_result:
            max_result = element
    return max_result


def min_element(list):
    min_result = list[0]
    for element in list:
        if element < min_result:
            min_result = element
    return min_result


def contains(list, searth_element):
    if searth_element in list:
        print(True)
    else:
        print(False)
    return


def sum_element(list):
    count = 0
    for i in list:
        count = count + i
    return count


def bubble_sort(list):
    for j in range(len(list) - 1):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
    return list


list = [21, 4, 23, 35, -10, 44, 78, 9]
print(max_element(list))
print(min_element(list))
searth_element = int(input("Searching element: "))
print(contains(list, searth_element))
print(sum_element(list))
print(bubble_sort(list))
