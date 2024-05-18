#Custom Model
def greeting():
    print("Hello from custom modul.")

def even_or_odd():
    num = int(input("Enter a positive number: "))
    if (num) == 0:
        print("Entered number is zero")
    elif (num%2) != 0:
        print(f"{num} is an odd number")
    else:
        print(f"{num} is an even number")