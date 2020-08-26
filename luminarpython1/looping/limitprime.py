#prgm to check given num is prime or not in a given limit
#7=>1,7
low=int(input("enter a low limit"))#10
upp=int(input("enter a higher limit"))#20

for i in range(low,(upp+1)):# 10 ...20
    flg=0
    for j in range(2,i):#2...9
        if(i%j==0):
            flg=1
            break
    if(flg==0):
        print("prime=",i)


