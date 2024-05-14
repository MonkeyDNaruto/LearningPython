keys = ["name", "age", "gender"]
values = ["Zoro", 21, "Male"]

print("keys ->", keys, "\nvalues ->", values)

person1 = {}
for key,value in zip(keys, values) :
    person1[key] = value
print("\nperson1 ->",person1)

person2 = {key: value for key, value in zip(keys, values)}
print("\nperson2 ->", person2)

person3 = {key: value for key, value in zip(keys, values) if key != "age"}
print("\nperson3 ->", person3)