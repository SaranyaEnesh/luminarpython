f=open("number","r")
lst=[]
for num in f:
    lst.append(int(num))#rstrip is used to remove last element and lstrip() is for remove frond data
res=sum(lst)
print(res)


