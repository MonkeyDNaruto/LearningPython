def func_name() :
    print("Hello, World!")

func_name()

def function2(num1, num2):
    sum = num1 + num2
    print("Sum -> ",sum)

function2(3, 4)

def user_age(age):
    userAge = print(f"You are {int(age)} years old")

zoro = user_age(21)

def person_info(name, age, gender, role="Student", requiredBook=5):
    person = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Role": role,
        "Required_Book": requiredBook
    }
    return person

nischal = person_info("Nischal", 19, "Male")
print("Nischal info ->", nischal)

nishuka = person_info("Nishuka", 24, "Female", "Worker", 0)
print("Nishuka info ->", nishuka)