class MyClass:
    course = "I'm learning python"
    def __init__(self, param):
        self.param = param
        print(param)
my_class = MyClass(param = "Anything")
print(my_class.course)
    