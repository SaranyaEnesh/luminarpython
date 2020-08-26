limit= int(input("How many terms? "))
n1=0
n2=1
count = 0
if limit<= 0:
   print("Please enter a positive integer")
else:
   print("Fibonacci sequence:")
   while count < limit:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1