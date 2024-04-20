personal_information = {
    "name": "Nischal",
    "age": 19,
    "class": "BSC.CSIT",
    "current_courses": ["DL", "C", "IIT", "Math", "Physics"],
}
print(personal_information)
print("Adding one key and value to dictionary")
personal_information["temporary_address"] = "Bhadrapur"
print(personal_information)
print("Removing key and value from dictonary")
del personal_information["temporary_address"]
print(personal_information)
print("listing all keys")
keys = personal_information.keys()
print(keys)
print("Listing all values")
values = personal_information.values()
print(values)
print("gettin what we want using get method")
what_we_want = input("Enter name age class or current_courses: ")
print(personal_information.get(what_we_want))
