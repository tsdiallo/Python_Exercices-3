#============= 14. Plus petit entier non nul (boucle ²while²) ==============
print("#============= %s. %s ==============\n" %(14, 'Plus petit entier non nul (boucle ²while²)'))
l = [5, 8, 0, 9, 12, 0, 6, 4]

l = [0, 0, 0, 4, 0, 3, 0]

i=0
plusPetitNonNul=0
while i in range(len(l)):
    if l[i]!=0:
        #print(i)
        k=i
        break
    i+=1
    
#print(k)

plusPetitNonNul=0
for i in range(k,len(l)):
    if l[i]!=0 and l[i]<l[k]:
        plusPetitNonNul=l[i]
print(plusPetitNonNul)
