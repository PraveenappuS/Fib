l = [12, 47, 45, 54, 12]
for i in range(len(l) -1):
    m_ind = i
    for j in range(i+1, len(l)):
        if l[j] < l[m_ind]:
            m_ind = j
            
    if l[i] != l[m_ind]:
        l[i], l[m_ind] = l[m_ind], l[i]
print(l)