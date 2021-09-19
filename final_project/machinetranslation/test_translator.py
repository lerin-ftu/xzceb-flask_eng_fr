import unittest
from translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def Test_frenchtranslation(self):
        self.assertEqual(
            french_to_english("Bonjour"), "Hello"
        )
        self.assertNotEqual(
            french_to_english("Bounjour"), "How are you"
        )

class Testenglish_to_french(unittest.TestCase):
    def Test_englishtranslation(self):
        self.assertEqual(
            english_to_french("Hello"), "Bonjour"
        )
        self.assertNotEqual(
            english_to_french("Hello"), "comment allez-vous"
        )

if __name__ == '__main__':
    unittest.main()
