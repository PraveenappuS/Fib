import random

def pivotplace(list, first, last):
    rindex = random.randint(first, last)
    list[rindex], list[last] = list[last], list[rindex]
    pivot = list[last]
    left = first
    right = last-1
    while True:
        while left<=right and list[left]<=pivot:
            left+=1
        while left<=right and list[right]>=pivot:
            right-=1
        if left>right:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[last], list[left] = list[left], list[last]
    return left

def quicksort(list, first, last):
    if first<last:
        p = pivotplace(list, first, last)
        quicksort(list, first, p-1)
        quicksort(list, p+1, last)

#main

list = [10,34,65, 67, 43, 9]
print("Unsorted List:")
print(list)
n = len(list)
quicksort(list, 0, n-1)
print("Sorted List:")
print(list)