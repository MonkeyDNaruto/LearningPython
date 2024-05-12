pets = ["Cat", "Dog", "Goat", "Lion"]
print(pets)
for animal in pets:
    print(animal)

for animal in pets:
    animal = animal.replace("a", "@").replace("o", "0").replace("i", "!")
    print(f"Funky letter of animal are {animal}")

fruits = {"Apple", "Banana", "Mango", "Orange"}
for setFruit in fruits:
    print(setFruit)

info = (
    (19, "Nischal"),
    (21, "Zoro"),
    (88, "Old Man")
)

for age,name in info:
    print(f"Name is {name} and age is {age}")