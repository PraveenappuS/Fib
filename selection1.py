#Descending Order

l = [12, 47, 45, 54, 12]
for i in range(len(l)):
    max_val = max(l[i:])
    max_ind = l.index(max_val, i)
    l[i], l[max_ind] = l[max_ind], l[i]

print(l)