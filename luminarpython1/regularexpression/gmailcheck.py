from re import*
lst=[]
rule='[\w]*[@]gmail[.]com'
f=open("email","r")
for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        print("valid")
        lst.append(data)
    else:
        print("invalid")
print("valid email id are:",lst)