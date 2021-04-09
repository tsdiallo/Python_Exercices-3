L=[-4, 2, -4, 1, 9, -6, -4]
somme0=False
for i in range (len(L)):
    for j in range (i,len(L)):
        s=0
        for k in range (i,j+1):
            s=s+L[k]
            if (s==0):
                somme0=True
print somme0 
            
L=[-4, 0, 5, 1]
somme0=False
for i in range (len(L)):
    for j in range (i,len(L)):
        s=0
        for k in range (i,j+1):
            s=s+L[k]
            if (s==0):
                somme0=True
print somme0 

L=[-3, 2, 4]
somme0=False

for i in range (len(L)):
    for j in range (i,len(L)):
        s=0
        for k in range (i,j+1):
            s=s+L[k]
            if (s==0):
                somme0=True
print somme0 
