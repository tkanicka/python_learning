import random


def swap(input_list, index1, index2):
    input_list[index1], input_list[index2] = input_list[index2], input_list[index1]


def quickSort1(input_list):
    if len(input_list) < 2:
        return input_list

    dividing1(input_list, 0, len(input_list) - 1)


def dividing1(input_list, start_index, end_index):

    diff = end_index - start_index
    if diff <= 1:
        return

    elif diff == 2:

        if input_list[start_index] > input_list[end_index]:
            swap(input_list, start_index, end_index)

    else:
        pivot_index = start_index + random.randint(0, diff)
        pivot = input_list[pivot_index]

        left = start_index
        right = end_index

        while left < right:
            ll = input_list[left] >= pivot
            rg = input_list[right] <= pivot

            if ll and rg:
                swap(input_list, left, right)
                left += 1
                right -= 1
                continue

            if ll:
                right -= 1

            if rg:
                left += 1

        dividing1(input_list, start_index, right)
        dividing1(input_list, left, end_index)


def quickSort2(inputList, start, end):

    if len(inputList) == 2:
        if inputList[start] > inputList[end]:
            swap(inputList, start, end)
            return inputList

    if start < end:
        pivot = dividing2(inputList, start, end)
        quickSort2(inputList, start, pivot - 1)
        quickSort2(inputList, pivot + 1, end)

    return inputList


def dividing2(inputList, start, end):

    random_pivotIndex = random.randint(start, end)
    swap(inputList, random_pivotIndex, end)
    pivot_index = start
    for i in range(start, end):
        if inputList[i] < inputList[end]:
            swap(inputList, i, pivot_index)
            pivot_index += 1
    swap(inputList, pivot_index, end)

    return pivot_index


def quickSort3(inputList, start, end):

    if start >= end:
        return inputList

    if end - start == 2:
        if inputList[start] > inputList[end]:
            swap(inputList, start, end)
            return inputList

    left = start
    right = end
    pivot = inputList[random.randint(start, end)]

    while left <= right:
        while inputList[left] < pivot:
            left += 1
        while inputList[right] > pivot:
            right -= 1
        if left <= right:
            swap(inputList, left, right)
            left += 1
            right -= 1

    quickSort3(inputList, start, right)
    quickSort3(inputList, left, end)


list_test = []
for x in range(10000):
    y = random.randint(0, 6500)
    list_test.append(y)

# quickSort1(list_test)
# quickSort2(list_test, 0, len(list_test)-1)
quickSort3(list_test, 0, len(list_test)-1)

print(list_test)

