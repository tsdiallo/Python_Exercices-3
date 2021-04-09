#============= 19. Suite croissante d'entiers consécutifs (avec `break`) ==============
print("#============= %s. %s ==============\n" %(19, "Suite croissante d'entiers consécutifs (avec `break`)"))
l=[81, 82, 83]
l=[2013, 2038, 3000]
consecutifs=True
for i in range(len(l)-1):
    if l[i+1]!=l[i]+1:
        consecutifs=False
    if i==len(l):
        break
print(consecutifs)
