#for pattern matching
#we have to import re module
import re
matcher=re.finditer("ba","ababcbababababab")
count=0
for match in matcher:
    print(match.start())#to find position
    print(match.group())#matched object
    count+=1
print("count",count)