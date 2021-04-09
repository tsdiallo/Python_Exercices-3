#============= 16. Liste d'entiers en miroir ==============
print("#============= %s. %s ==============\n" %(16, "Liste d'entiers en miroir"))
l = [4, 2, 2, 4]
listeMiroir=False
for i in range(len(l)):
    if len(l)%2==0 and l[i]==l[len(l)-1-i]:
        listeMiroir=True
print(listeMiroir)
