#============= 4. Somme qui vaut 42 ==============
print("#============= %s. %s ==============\n" %(4, 'Somme qui vaut 42'))
l=[17, 22, 5, 5, 33, 8]
m=[34, 8, 20]
for i in l:
    for j in m:
        somme42= i+j==42
        if somme42 == True:
            print(somme42)
            break
