a ={1:1,
"Name": "Pooja"}
print(a)

#add
a["Age"] = 28
print(a)

#delete 
del a["Age"]
print(a)


# Exercise 1: Basic Dictionary Operations
# Exercise 2: Dictionary Operations
# Exercise 3: Dictionary from Two Lists
a ={"pooja", "hell"}

b ={23,56}
c= {a: b for a,b in zip(a,b)}
print(c)
# Exercise 4: Clear Dictionary

a = {2:3,"name":"pooja"}
a.clear
print(a)

# Exercise 5: Merge Dictionaries
dict1 = {"age": 2,"name":"pooja"}
dict2 = {"age":52,"name":"goja"}
# dict3 = (**dict1 
# Exercise 6: Access Nested Dictionary
person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person["address"]["zip"])
person["address"]["zip"]=3553
print(person)
# Exercise 7: Access ‘history’ Key From a Nested Dictionary
# student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
# a = student[]

# Exercise 8: Initialize Dictionary with Default Values
keys = ["math", "science", "english", "history"]
default = 30
var = dict.fromkeys(keys,30)
print(var)

# Exercise 9: Rename a Key of Dictionary
keys = {"name": "pooja", "age": 34}
keys["First name"]=keys.pop("name")
print(keys)

# Exercise 10: Delete a List of Keys
keys = {"name": "pooja", "age": 34,"salary" : 47565, "designation": "QA"}
list1= {"name","salary"}
for i in list1:
    keys.pop(i,None)
print(keys)