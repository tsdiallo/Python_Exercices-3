#============= 13. Listes « opposées » (boucle `while`) ==============
print("#============= %s. %s ==============\n" %(13, 'Listes « opposées » (boucle `while`)'))


L=[81, -12, -81, -31, 0]
M=[-81, 12, 81, 31, 0]

n=len(L)
m=len(M)
i=0
print(L)
print(M)
sontOpposees=True
while i<n and n==m and L[i]==-M[i]:
    i+=1
if i==n:
    print(sontOpposees)
else:
    sontOpposees=False
    print(sontOpposees)
