import unittest
from my_program import make_upper_case, get_first_word, return_list

class UnitTesting(unittest.TestCase):
    def test_hello_world(self):
        result = make_upper_case("hello world")
        self.assertEqual(result, "HELLO WORLD")    

    def test_first_word(self):
        result = get_first_word("Lorem ipsum is derived from the Latin")
        self.assertEqual(result, "Lorem")

    def test_list_return(self):
        result = return_list()
        self.assertListEqual(result, ["Cat", "Dog", "Horse"])

if __name__ == "__main__":
    unittest.main()

