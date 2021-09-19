import unittest
from translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"), "hello") # test when bonjour is given as input the output is Hello.
        self.assertNotEqual(french_to_english("animaux"), "dog") # test when animaux is given as input the output is not dog.
        self.assertEqual(french_to_english("repas"), "meals") # test when repas is given as input the output is meals.
        self.assertEqual(french_to_english(), None) # test when null is given as input the output is null.

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "bonjour") # test when hello is given as input the output is bonjour.
        self.assertNotEqual(english_to_french("dog"), "animaux") # test when dog is given as input the output is not animaux.
        self.assertEqual(english_to_french("meals"), "repas") # test when meals is given as input the output is repas.
        self.assertEqual(english_to_french(), None) # test when null is given as input the output is null.

if __name__ == '__main__':
    unittest.main()
