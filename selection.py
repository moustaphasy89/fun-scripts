tab = [1,2,3,6,7]
n = len(tab)

for i in range(n - 1):
    mini = i
    for j in range(i+1,n):
        if tab[j] < tab[mini]:
            mini = j
    tmp = tab[i]
    tab[i] = tab[mini]
    tab[mini] = tmp
    

print tab
