f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    year=data[2]
    movie=data[1]
    if(year not in dict):
        dict[year]=movie
    else:
        dict[year]=movie
for k,v in dict.items():
    print(k," , ",v)

