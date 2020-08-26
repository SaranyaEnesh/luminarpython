#print numbers uptolow to up limit
low=int(input("enter low"))
upp=int(input("enter upp"))
evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum=oddsum+i
print(oddsum)
print(oddsum)
