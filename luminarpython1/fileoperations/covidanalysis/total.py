f=open("covid_19_india.csv","r")
dict={}
dict2={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    confirmed=death[6]
    if(state not in dict):
        dict[state]=death
        dict2[state]=confirmed
    else:
        dict[state]=death
        dict2[state]=confirmed
dsum=0
csum=0
for k,v in dict.items():
    dsum+=int(v)
    print(k,v)
for k,v in dict2.items():
    csum+=int(v)
print("total death:",dsum)
print("total confirmed",csum)