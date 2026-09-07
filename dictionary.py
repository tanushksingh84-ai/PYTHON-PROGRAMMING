student={"name":"Tanushk","age":18,"course":"Python"}
print(student)
#Empty Dictionary
empty_dict={}
print(empty_dict)

print(len(student))
print(len(empty_dict))

#Accessing values
print(student["name"])
print(student["age"])

#using get()
print(student.get("name"))
print(student.get("city"))

#Default Value
print(student.get("city","City Not Found"))

student["city"]="Noida"
print(student)

student["age"]=26
print(student)

student["city"]="NCR"

del student["course"]
print(student)

age=student.pop("age")
print(age)  
print(student)

#popitem()  remove the last inserted item
student["course"]="Python" 
student["city"]="Noida"
remove_item=student.popitem()
print(remove_item)
print(student)

temp={"a":1,"b":2}
temp.clear()
print(temp)


print("***********************************************")

print(student.keys())
print(student.values())
print(student.items())


for key in student:
    print(key)

for key in student.keys():
    print(key)
    