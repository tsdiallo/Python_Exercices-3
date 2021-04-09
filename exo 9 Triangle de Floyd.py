n=int(input("enter la valeur de n \t"))
triangle = ""
for i in range(1,n+2):
    for j in range(1,i):
        triangle = triangle + " " + "*"
    print(triangle)
    triangle = ""
 
