lst=[]
even=[]
odd=[]
for i in range(50,70):
    lst.append(i)
print(lst)
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even=",even)
print("odd=",odd)

