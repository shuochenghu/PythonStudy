person=dict(Name="Chuck Hu", Age=48, Salary=100000)
print(person)
print(person["Name"])
print("update name")
person["Name"]="Andrew Hu"
print(person["Name"])
print("add Insurance")
person["Insurance"]="Yes"
print(person)
print("delete age")
del person["Age"]
print(person)