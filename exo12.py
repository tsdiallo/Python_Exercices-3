#============= 12. Que des 81 puis que des 12 ==============
print("#============= %s. %s ==============\n" %(12, 'Que des 81 puis que des 12'))
l=[81, 81, 81, 12, 12, 12, 12]
'''
indicePremier_12=0
for i in range(len(l)):
    if l[i]!=12:
        indicePremier_12+=1
print(indicePremier_12)
'''

indicePremier_12=0
i=0
while i in range(len(l)):
    if l[i]!=12:
        indicePremier_12+=1
    i+=1
print(l," -> ",indicePremier_12)
