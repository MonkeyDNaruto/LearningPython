person = {
    "Name": "Zoro",
    "Age": 21,
    "Gender": "Male"
}

print(person)
print(person.items())
print(type(person))

print("\nchanging person type into list")
personList = list(person)
print(personList,"\n", type(personList))
personList = list(person.items())
print(personList,"\n", type(personList))

print("\nChanging person type into set")
setPerson = set(person)
print(setPerson,"\n", type(setPerson))
setPerson = set(person.items())
print(setPerson,"\n", type(setPerson))

print("\nChanging person type into tuple")
tulPerson = tuple(person)
print(tulPerson,"\n", type(tulPerson))
tulPerson = tuple(person.items())
print(tulPerson,"\n", type(tulPerson))

print("\nChanging person type into string")
strPerson = str(person)
print(strPerson,"\n", type(strPerson)) 
strPerson = str(person.items())
print(strPerson,"\n", type(strPerson))