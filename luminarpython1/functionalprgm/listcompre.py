lst=[1,2,3,4,5,6]#single line
sq=[(i*i)for i in lst ]
print(sq)
#pairs
pairs=[(i,j)for i in lst for j in lst]
print(pairs)
#odd
odd=[i for i in lst if i%2==0]
print(odd)
