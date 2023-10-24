def insertion(list):
    for i in range(1, len(list)):
        c_ele = list[i]
        pos = i
        while c_ele > list[pos-1] and pos>0:
            list[pos] = list[pos-1]
            pos-=1
        list[pos] = c_ele

list = [10,34,65, 67, 43, 9]
print("Unsorted List in descending:")
print(list)
insertion(list)
print("Sorted list in descending:")
print(list)