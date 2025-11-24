import random


rn = random.Random()
list = []

for i in range(100):
    list.append(rn.randint(0, 100))
print(list)
print("\n\n")

def mergeSort(given_list):
    if len(given_list) <= 1:
        return given_list
    else:
        midpoint = (len(given_list) - 1) // 2
        left_half = given_list[0:midpoint + 1]
        right_half = given_list[midpoint + 1: len(given_list)]

        left_half = mergeSort(left_half)
        right_half = mergeSort(right_half)

        return merge(left_half, right_half)



def merge(list1, list2):
    index1 = 0
    index2 = 0
    new_list = []

    while index1 < len(list1) and index2 < len(list2):
        
        if list1[index1] < list2[index2]:
            new_list.append(list1[index1])
            index1 += 1
        else:
            new_list.append(list2[index2])
            index2 += 1

    while index1 < len(list1):
        new_list.append(list1[index1])
        index1 += 1
        
    while index2 < len(list2):
        new_list.append(list2[index2])
        index2 += 1


    return new_list



def quickSort(low, high, list):
    pivot = list[low]
    start = low - 1
    end = high
    if high <= low:
        return list
    else:
        while high >= low:
            while list[low] < pivot and low <= high:
                low += 1
            while list[high] > pivot and low <= high:
                high -= 1

        if low < high:
            temp = list[high]
            list[high] = list[low]
            list[low] = temp
        temp = list[high]
        list[high] = list[low]
        list[low] = temp


    

        quickSort(start, high - 1, list)
        quickSort(high + 1, end, list)


def binarySearch(list, low, high, item):
    midpoint = (high + low) // 2
    if list[midpoint] == item:
        return midpoint
    if low >= high:
        return -1 

    if item < list[midpoint]:
        return binarySearch(list, low, midpoint -1, item)
    else:
        return binarySearch(list, midpoint + 1, high, item)

list = mergeSort(list)
print(list)


index = binarySearch(list, 0, 99, 69)
print(index)
if index > 0:
    print(list[index])