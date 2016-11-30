
t = [5,4,3,2,1]


def mergeSort(tab):
    n = len(tab)
    start = 0
    end = n-1
    mid = int(round((end - start + 1) / 2))
    if start < end:
        mergeSort(tab[start:mid])
        mergeSort(tab[mid:n])
        return merge(tab[start:mid], tab[mid:n])

def merge(tabA, tabB):
    if not tabA:
        return tabB
    if not tabB:
        return tabA
    if tabA[0] < tabB[0]:
        return [tabA[0]] + merge(tabA[1:], tabB)
    else:
        return [tabB[0]] + merge(tabA, tabB[1:])
    
        

print mergeSort(t)
    
    
    
    
