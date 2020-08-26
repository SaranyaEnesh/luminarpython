employess=[[1001,"arun",15000],
           [1002,"arjun",20000],
           [1003,"vinu",25000],
           [1004,"binu",18000],
           ]
for emp in employess:
    if(emp[2]>17000):
        print(emp[1])
sum=0
for emp in employess:
    sum=sum+emp[2]
print(sum)