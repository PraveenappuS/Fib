def shellsort(list):
    gap = len(list)//2
    while gap>0:
        for i in range(gap, len(list)):
            c_ele = list[i]
            pos = i
            while c_ele<list[gap] and pos>=gap:
                list[pos] = list[pos-gap]
                pos = pos-gap
            list[pos] = c_ele
        gap = gap//2

list = [10,34,65, 67, 43, 9]
print("Unsorted shell list:")
print(list)
shellsort(list)
print("Sorted shell sort:")
print(list)