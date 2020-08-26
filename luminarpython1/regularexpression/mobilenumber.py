from re import*
rule='/d{9}'
mobno=input("enter mobile number")
matcher=fullmatch(rule,mobno)
if(matcher!=None):
    print("valid")
else:
    print("invalid")