print("Args\n")
def keys(*args) :
    for arg in args:
        print(arg)

keys(1,2,3,4)

print("\nKwargs")
def keyValue(**kwargs):
    for key,value in kwargs.items():
        print("Key:", key, "\t\tvalue: ", value)

keyValue(Name="Nischal", Age=19, Hobby="Coding")

print("\n")
def order(name, *dishes, **kwargs):
    print(f"Hello {name}")
    for dish in dishes:
        print(f"You ordered {dish}")
    if kwargs.get("address"):
        address = kwargs.get("address")
        print(f"We are delivering to {address}")
    else:
        print("YOU DID'T GIVE US YOUR ADDRESS CMON")

order("Nischal", "Pizza", "Burger", "Keema Noodles", address="KTM")
print("\n")
order("Nishuka", "Fried Rice", "Momos")