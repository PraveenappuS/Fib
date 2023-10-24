l = [10,34,65, 67, 43, 9]
for j in range(len(l) - 1):
    for i in range(len(l) - 1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
print(l)