num = int(input("Enter a number: "))
if num%3 == 0 and num%5 == 0 :
    print("Entered number is perfectly divided by 3 and 5.")

if num%4 == 0 or num%10 == 0 :
    print("Entered number is perfectly divided by 4 or 10.")

if (num%3 == 0 and num%5 == 0) or num%10 == 0:
    print("Entered number is perfectly divided by 3 and 5 or 10")