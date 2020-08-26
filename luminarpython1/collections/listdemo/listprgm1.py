lst=[2,4,6,8]
cnt=1
for i in lst:
    print(i**cnt)#2**1  4**2  6**3
    cnt+=1


######################################

cnt=len(lst)
print(cnt)
j=1
for i,j in range(0,(cnt)):#0 - 4
    res=lst[i]**j
    j+=1
    print(res)
