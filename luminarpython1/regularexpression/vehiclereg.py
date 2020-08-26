from re import*
rule='[Kk][Ll][0-9]{2}[a-z]*\d{4}'
regno=input("enter vehicle no.")
matcher=fullmatch(rule,regno)
if(matcher!=None):
    print("valid")
else:
    print("invalid")