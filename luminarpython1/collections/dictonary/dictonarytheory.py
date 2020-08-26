#define dictonary  dict={}
#datas are stored in the form of ker,value pairs
#rol:"ajay"
#key-rol
#value-ajay
student={"rol":1001,"name":"ajay"}
#keys->rol,name,age duplicate keys are not allowed

#if we want to featch a value we have to use corresponding key
#print(student["name"])
#dictonary iteration
for key in student:
    print(key,",",student[key])
#updating value in dictonary
#student["cpp"]+=25
print(student)
student["name"]="TINU"
print(student)
#check a key
print("total" in student)


