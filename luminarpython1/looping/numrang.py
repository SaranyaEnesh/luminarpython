#print numbers uptolow to up limit
low=int(input("enter low"))
upp=int(input("enter upp"))
for i in range(low,(upp+1)):
    if(i%2==0):
        print(i)