#nested_function.py
def animal():
    print("Which animal sound you need.")

    def dog():
        print("Dog")
        def dog_sound():
            sound = "WOOF WOOF"
            return sound
        print(dog_sound())
        return dog_sound
    
    def cat():
        print("Cat")
        def cat_sound():
            sound = "MEOW MEOW"
            return sound
        print(cat_sound())
        return cat_sound

    return dog,cat


        
dog = animal()[0]
dog()

cat = animal()[1]
cat()
