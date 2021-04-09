#============= 17. Pas d'impair (avec `break`) ==============
print("#============= %s. %s ==============\n" %(17, "Pas d'impair (avec `break`)"))
l=[82, 31, 82]
l=[82, 12, 46]
print(l)
queDesPairs=True
for i in l:
    if i%2!=0:
        queDesPairs=False
        break
print(queDesPairs)
