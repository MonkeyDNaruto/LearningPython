num = 1
colors = ("Red", "Green", "Blue", "Orange", "Purple", "Pink")

# Break
print("Loop has started...")
while num<=20:
    print(num)
    num = num + 1
    if num == 10:
        break
print("Loop has ended")
print("\nLoop has started...")
for color in colors:
    if color == "Orange":
        continue
    print(color)
print("Loop has ended\n")

# continue
print("Loop has started...")
while num<=20:
    print(num)
    num = num+1
    if num == 10:
        continue
print("Loop has ended")
print("Loop has started...")
for color in colors:
    if color == "Orange":
        break
    print(color)
print("Loop has ended")
