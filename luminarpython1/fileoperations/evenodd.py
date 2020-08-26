f=open("number","r")
lst=[]
for i in f:
    lst.append(int(i))
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)