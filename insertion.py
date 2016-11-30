tab = [5,4,3,6,7]
n = len(tab)
for i in range(n):
    cle = tab[i]
    j = i
    while j > 0 and cle < tab[j-1] :
        tab[j] = tab[j - 1]
        j = j - 1
    tab[j] = cle

print tab
