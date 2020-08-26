f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    rating=data[3]
    movie=data[1]
    if(rating not in dict):
        dict[rating]=movie
    else:
        dict[rating]=movie
for k,v in dict.items():
    print(k," , ",v)

