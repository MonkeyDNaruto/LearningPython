num = int(input("Enter a number: "))

if num > 0:
    if num%2 == 0:
        print("Entered number is positive even number")
    else :
        print("Entered number is positive odd number")
elif num < 0:
    if num%2 == 0:
        print("ENtered number is negative even number")
    else:
        print("Entered number is negative odd number")
else:
    print("Entered number is zero")