class Animal:
    def __init__(self, species, name, weight, color):
        self.species = species
        self.name =  name
        self.weight = weight
        self.color = color

    def info(self):
        print(f"Type -> {self.species} \t\t Name -> {self.name} \nWeight -> {self.weight} \t\t Color -> {self.weight}")

    def speak(self):
        print("What does your animal speak?")

class Cat(Animal):
    def speak(self):
        print("Meoooowwwww")

class Dog(Animal):
    def speak(self):
        print("Wolf Wolf")


animal = Animal("Goat","Gotti", "23 kg", "Black")
animal.info()
animal.speak()

print("\n")

honey = Cat("Cat", "Honey", "8kg", "White")
honey.info()
honey.speak()

print("\n")

tommy = Dog("Dog", "Tommy", "15kg", "Brown")
tommy.info()
tommy.speak()