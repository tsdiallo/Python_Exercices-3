#============= 1. Répéter l'affichage du contenu d'une liste ==============
print("#============= %s. %s ==============\n" %(1, "Répéter l'affichage du contenu d'une liste"))
l=[4, 8, 0, 9, 6, 3, 2, 8]
n=6
for i in range(n):
    for i in l:
        print(i, end=" ")
    print()
