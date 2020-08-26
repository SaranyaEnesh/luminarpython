from re import *
rule='[\w]*[@]gmail[.]com'
email=input("enter your email id")
matcher=fullmatch(rule,email)
if(matcher!=None):
    print("valid")
else:
    print("invalid")