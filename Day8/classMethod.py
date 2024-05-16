class MyClass:
    sentence = "Hello, World!"
    def __init__(self, param1="Anything"):
        print(param1)

    def student(self, std):
        self.std = std
        print(f"Number of student is {std}")

    def newStudent(self, newStd):
        self.newStd = newStd
        print(f"Number of of new student is {self.newStd}")

    def totalStudent(self):
        self.total = self.std + self.newStd
        print(f"Total number of student is {self.total}")


my_class = MyClass("Nothing")
my_class.student(100_000)
my_class.newStudent(30_000)
my_class.totalStudent()