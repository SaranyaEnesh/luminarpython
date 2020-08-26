from re import*
lst=[]
rule='[Kk][Ll][0-9]{2}[a-z]*\d{4}'
f=open("regno","r")
for line in f:
    data=line.rstrip("\n")
    matcher=fullmatch(rule,data)
    if(matcher!=None):
        print("valid")
        lst.append(data)
    else:
        print("invalid")
print("valid reg numbers are :",lst)