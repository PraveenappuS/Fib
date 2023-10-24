def pivotplace(list, first, last):
    pivot = list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left = left + 1
        while left <= right and list[right] >= pivot:
            right = right - 1
        if left > right:
            break
        else:
            list[left], list[right] = list[right], list[left] 
    list[first], list[right] = list[right], list[first] #first is pivot
    return right

def quicksort(list, first, last):
    if first<last:  
        p = pivotplace(list, first, last)
        quicksort(list, first, p-1)
        quicksort(list, p+1, last)

#main
list = [10,34,65, 67, 43, 9]
print(list)
n = len(list)
quicksort(list,0,n-1)
print("Sorted list:",list)
