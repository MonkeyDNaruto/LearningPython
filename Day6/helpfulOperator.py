print("Helpful Operator: -> in")
fruits = ["Apple", "Mango", "Orange", "Strawberry", "Watermelon"]
if "Apple" in fruits:
    print(fruits)

print("\nEnumerate")
for index, fruit in enumerate(fruits):
    print(index+1, "->", fruit)

lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3]

print("\nlst1 =", lst1, "\nlst2 =", lst2)
print("\nZipping")

for letter,number in zip(lst1, lst2):
    print(letter, "->", number)

print("\nMin and Max")
print("Min of lst1 ->", min(lst1), "\tMin of lst2 ->", min(lst2))
print("Max of lst1 ->", max(lst1), "\tMax of lst2 ->", max(lst2))

print("\nJoin")
str(lst1)
print(("->".join(lst1)))

print("\nSplit and Sort")
sentence = "I love coding"
word = sentence.split( )
print(word)
word.sort()
print(word)

print(("_".join(word)))

print("\nShuffle")
from random import shuffle
shuffle(word)
print(word)