f=open("temparaturedata","r")
dict={}
for lines in f:
    district,temp=lines.rstrip("\n").split(",")
    print(district)
    print(temp)
    if(district not in dict):
        dict[district]=temp
    else:
        old=dict[district]
        if(temp>old):
            dict[district]=temp
print(dict)