import random


def quickSort(list1):

    if len(list1) == 0:
        return list1

    sort_num = list1[random.randint(0, len(list1) - 1)]

    smaller = []
    greater = []
    matches = []

    for element in list1:

        if element < sort_num:
            smaller.append(element)

        elif element > sort_num:
            greater.append(element)

        elif element == sort_num:
            matches.append(element)

    return quickSort(smaller) + matches + quickSort(greater)


list_test = [2, 5, 9, 4, 0, 36, 17, 19, 8, 124, 2, 9, 12, 10]
list_test = quickSort(list_test)
print(list_test)

list_test2 = []
for x in range(30):
    list_test2.append(random.random())

list_test2 = quickSort(list_test2)
print(list_test2)