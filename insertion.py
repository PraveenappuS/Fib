def insertion(list):
    for i in range(1, len(list)):
        c_element = list[i]
        pos = i
        while c_element < list[pos - 1] and pos>0:
            list[pos] = list[pos-1]
            pos = pos-1
        list[pos] = c_element

list = [10,34,65, 67, 43, 9]
print("Unsorted list:")
print(list)
insertion(list)
print("Sorted List:")
print(list)