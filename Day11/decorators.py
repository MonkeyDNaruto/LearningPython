#decorators.py

def main_func(orginal_func):
    def child_func():
        value = orginal_func()
        print(f"Entered number is {value}")
        value = value ** 2
        print(f"The square of entered number is {value}")
        return value
    return child_func

@main_func
def orginal_func():
    num = int(input("Enter a number: "))
    return num

orginal_func()