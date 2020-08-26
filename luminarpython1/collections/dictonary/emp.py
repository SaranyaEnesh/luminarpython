employee={"eid":1001,
          "ename":"anju",
          "desig":"kottayam",
          "salary":15000,
          }
print(employee["ename"])
print("company" in employee)
employee["company"]="Luminar"
print(employee["company"])
employee["salary"]+=5000
for key in  employee:
    print(key,",",employee[key])