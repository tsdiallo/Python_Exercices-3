L=[81,82,89]
compteur=0
consecutifs=True
while(compteur<len(L)-1 and L[compteur]==L[compteur+1]-1):
    compteur+=1
if (compteur==len(L)-2 or len(L)==1):
    consecutifs=True
else:
    consecutifs=False
print (consecutifs)

