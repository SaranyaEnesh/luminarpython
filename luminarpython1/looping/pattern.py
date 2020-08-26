for i in range(1,4):#row i=1 i=2 i=3
    for j in range(1,(i+1)):#col j(1,2)  j(1,3)
        print(j,end="")#1  12  123
    print()

for i in range(1,4):#1
    for j in range(1,i+1):
        print(i,end="")
    print()