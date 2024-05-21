#my_program.py
def make_upper_case(text):
    """
    i.e. hello world -> HELLO WORLD
    """
    return text.upper()

def get_first_word(sentence):
    word = sentence.split(' ')
    return word[0]

def return_list():
    return ["Cat", "Dog", "Horse"]