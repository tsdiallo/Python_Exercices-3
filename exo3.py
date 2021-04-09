#============= 3. Somme de sommes ==============
print("#============= %s. %s ==============\n" %(3, 'Somme de sommes'))
x=0
n=4
for i in range(n):
    x+=10**i
print("Pour n=",n," on a ",x)
print()
print()
n=20
somme=0
x=0
for i in range(n):
    x+=10**i
    somme+=x
print(somme)
