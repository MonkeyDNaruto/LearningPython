names = ["Luffy", "Zoro", "Sanji", "Brook"]
def handle_names(name):
    name = name.lower()
    if name == "luffy":
        return "Captain"
    elif name == "zoro":
        return "Swordman"
    elif name == "sanji":
        return "Cook"
    elif name == "brook":
        return "Musician"
    else:
        return "Don't know"
    
for role in map(handle_names, names):
    print(role)
    
role = list(map(handle_names, names))
print(role)