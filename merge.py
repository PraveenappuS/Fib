def merge(l):
    if len(l)>1:
        mid = len(l)//2
        l_l = l[:mid]
        r_l = l[mid:]
        merge(l_l)
        merge(r_l)
        i = 0 
        j = 0
        k = 0
        while i < len(l_l) and j < len(r_l):
            if l_l[i] < r_l[j]:
                l[k] = l_l[i]
                i+=1
                k+=1
            else:
                l[k] = r_l[j]
                j+=1
                k+=1

        while i<len(l_l):
            l[k] = l_l[i]
            i+=1
            k+=1
        while j<len(r_l):
            l[k] = r_l[j]
            j+=1
            k+=1



l = [10,34,65, 67, 43, 9]
print(l)
merge(l)
print(l)