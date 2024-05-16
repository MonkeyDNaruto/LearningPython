class MyClassList:
    def __init__(self, name="Nischal", hobby="Coding"):
        self.name = name
        self.hobby = hobby
        print(f"Name -> {name} \t\t hobby -> {hobby}")

    def say_hello(self):
        print(f"Hello {self.name}")

    def say_name(self):
        print(f"Your name is {self.name}")

    def say_hobby(self):
        print(f"Your hobby is {self.hobby}")

person = MyClassList(name = "Nishuka", hobby="Sleeping")
person.say_hello()
person.say_name()
person.say_hobby()