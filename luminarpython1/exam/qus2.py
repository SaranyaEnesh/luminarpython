lst1=[1,2,3,4]
lst2=[]
for i in range(0,len(lst1)-1):
    lst=lst1[i],lst1[i+1]
    if lst not in lst2:
        lst2.append(lst)
    lst3=lst1[0],lst1[i-1]
    if lst3 not in lst2:
        lst2.append(lst)
print(lst2)
