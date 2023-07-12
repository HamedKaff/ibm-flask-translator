import unittest

from translator import english_to_french_translate, french_to_english_translate


class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french_translate("hello"), "bonjour")
        self.assertEqual(english_to_french_translate("no"), "Non")
        self.assertEqual(english_to_french_translate("dangerous"), "dangereux")

    
    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french_translate("hello"), "au revoir")
        self.assertNotEqual(english_to_french_translate("no"), "Oui")
        self.assertNotEqual(english_to_french_translate("dangerous"), "sûr")

    def test_french_to_english(self):
        self.assertEqual(french_to_english_translate("bonjour"), "hello")
        self.assertEqual(french_to_english_translate("morte"), "death")
        self.assertEqual(french_to_english_translate("dangereux"), "dangerous")


    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english_translate("scared"), "bonjour")
        self.assertNotEqual(french_to_english_translate("dead"), "dangereux")
        self.assertNotEqual(french_to_english_translate("break"), "morte")


        
        



if __name__  == '__main__':
    unittest.main()


