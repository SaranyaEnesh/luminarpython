lst=[1,2,3,4]
num=int(input("enter a element"))
low=0
upp=len(lst)-1
while(low<=upp):
    data=lst[low]+lst[upp]
    if(data==num):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(data>num):
        upp=upp-1
    else:
        low=low-1


