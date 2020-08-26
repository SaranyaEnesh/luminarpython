bdate=int(input("enter birth date"))
bmonth=int(input("enter birth month"))
byear=int(input("enter birth year"))

cdate=int(input("enter birth date"))
cmonth=int(input("enter birth month"))
cyear=int(input("enter birth year"))
age=cyear-byear
if(cmonth>=bmonth):
    age=age-1
print("u are",age,"years old")