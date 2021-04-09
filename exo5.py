#============= 5. Afficher les effectifs d'une liste d'entiers ==============
print("#============= %s. %s ==============\n" %(5, "Afficher les effectifs d'une liste d'entiers"))
l = [81, 31, 81, 12, 81, 9, 12, 65]
dico={}
for i in l:
    dico[i]=0
print(l)
for i in l:
    dico[i]+=1
print(dico)
