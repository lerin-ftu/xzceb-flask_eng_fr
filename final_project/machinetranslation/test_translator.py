import unittest
from translator import english_to_french
from translator import french_to_english

class Testfrench_to_english(unittest.TestCase):
    def Test_frenchtranslation(self):
        self.assertEqual(language_translator.translate("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()