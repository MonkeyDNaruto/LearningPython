class Main():
    def num(self):
        num = input("Enter a number: ")
        print("Entered number is ", num)
        return num

class Square(Main):
    def square(self):
        previousNum = super().num()
        square = int(previousNum) ** 2
        print("Square of entered number is ", square)
        return square
    
class Cube(Square):
    def cube(self):
        previousNum = super().num()
        cub = int(previousNum) ** 3
        print("Cube of entered number is ", cub)
        return cube    

square = Square()
square.square()

print("\n")

cube = Cube()
cube.cube()