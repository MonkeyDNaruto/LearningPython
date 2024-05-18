# #catching_exception.py

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")

# try:
#     num3 = float(num1)/float(num2)
#     print(num3)
# except TypeError as e:
#     print("Opps there is an error, ", e)
# except ValueError as e:
#     print("Opps you have encounter an error,", e)
# except ZeroDivisionError as e:
#     print("FLoat cannot be divided by zero,", e)
# except Exception as e:
#     print(type(e))
#     print(e)
# else:
#     print("Program sucessfully run")


while True:
    num1 = input("Enter a number: ")
    num2 = input("Enter a number: ")
    try:
        num3 = float(num1)/float(num2)
        print(num3)
        break
    except ZeroDivisionError as e:
        print("Float cannot be divided by zero,", e)
    except TypeError as e:
        print("String cannot be divided,", e)
    except ValueError as e:
        print("Float and string cannot be divided,", e)
    except Exception as e:
        print(type(e))
        print(e)
    finally:
        print("This is going to run no matter what")