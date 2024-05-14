sentence = "Python for Evenyone"

lst1 = []

for letter in sentence:
    lst1.append(letter)
print("lst1 =", lst1)

lst2 = [letter for letter in sentence]
print("\nlst2 =", lst2)

vowels = [letter for letter in sentence if letter.lower() in "aeiou"]
print("\nVowels letter in sentence ->", vowels)

c = [-50, -30, -15, 0, 15, 33, 50]
print("\nDegree in celcius ->", c)

print("\nChanging celcius into fahrenheit using normal way")
f = []
for temp in c:
    temp = (temp*1.8) + 32
    f.append(temp)
print("Degree in fahrenheit ->", f)

print("\nChanging celcius into fahrenheit using list comprehension")
f = [(temp*1.8) + 32 for temp in c]
print("Degree in fahrenheit ->", f)