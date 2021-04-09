#============= 2. Damier de nombres ==============
print("#============= %s. %s ==============\n" %(2, 'Damier de nombres'))
a=81
b=32
memeParite = a%2==b%2
print(memeParite)

n=7
a=4
b=2
for i in range(n):
    for i in range(n):
        if i%2==0:
            print(a, end=" ")
        else:
            print(b, end=" ")
    (a,b)=(b,a)
    print()
