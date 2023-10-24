#Ascending order
l = []
n = int(input())
for i in range(n):
    l.append(int(input()))
print("Unsorted list:",l)


for j in range(len(l)):
    min_val = min(l[j:]) #coz sorted list is separate
    min_ind = l.index(min_val)
    l[j], l[min_ind] = l[min_ind], l[j]

print("Sorted List",l)