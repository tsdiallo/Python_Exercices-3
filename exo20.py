#============= 20. Calculer le nombre de chiffres d'un entier ==============
print("#============= %s. %s ==============\n" %(20, "Calculer le nombre de chiffres d'un entier"))
n=741520036365253625145211741523636854198541
nchiffres=1
while n//10!=0:
    n=n//10
    nchiffres+=1
print(nchiffres)
