from re import *
#pattern="a+"#it check only the position of more than a
#pattern="a*"#it check all positions
#pattern="a?"#it check all position individually
#pattern="a{2}"#chk 2 num of a
pattern="a{2,3}"#mini 2 and max 3 num of a
matcher=finditer(pattern,"aabaaaabbabbaaaa")
count=0
for match in matcher:
    print(match.start())
    print(match.group())
    count+=1
print("count",count)
