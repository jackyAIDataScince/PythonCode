# The Merge Sort algorithm is a divide and conquer algorithm which takes an array as an input and then divides the complete array into sub-arrays of single elements.
# As a result, we are left with so many sorted arrays as the single element is always sorted. 
#Then we merge all the arrays by taking two arrays at a time until we get a final sorted array.
#Date : 31-Jan-2023
#Author : Jacky
#refence by : thecleverprogrammer

def merge(listA, listB):
    newlist = list()
    a = 0
    b = 0
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1
    while a < len(listA):
        newlist.append(listA[a])
        a += 1
    while b < len(listB):
        newlist.append(listB[b])
        b += 1
    return newlist

def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        mid = len(input_list) // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        newlist = merge(left, right)
        return newlist

a = [56, 89, 45, 34, 90, 32, 20, 67, 43]
print(merge_sort(a))
