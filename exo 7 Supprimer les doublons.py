L=[42, 81, 42, 65, 12, 81, 31, 42]
n=len(L)
sansdoublons=[]
for i in range (n):
   sansdoublons=list(set(L))
print L,"->", sansdoublons
print

L=[42]
n=len(L)
sansdoublons=[]
for i in range (n):
   sansdoublons=list(set(L))
print L,"->", sansdoublons
print
L=[42, 42, 42, 42, 42]
n=len(L)
sansdoublons=[]
for i in range (n):
   sansdoublons=list(set(L))
print L,"->", sansdoublons
print
