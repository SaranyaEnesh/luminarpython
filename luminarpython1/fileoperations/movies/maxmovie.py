f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(" ")
    year=data[2]
    movie=data[1]
for word in data:
    if(word not in dict):
        dict[word]=1
    else:
        dict[word]+=1
for k,v in dict.items():
    print(k,",",v)