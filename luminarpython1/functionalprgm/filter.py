lst=[1,2,3,4]
def even(num):
    return num%2==0
evens=list(map(even,lst))
print(evens)