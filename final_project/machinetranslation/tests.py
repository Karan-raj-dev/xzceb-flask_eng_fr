"""System module."""
import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    """ This class is to test the translator """
    def test_french_to_english(self):
        ''' test_1 '''
        self.assertEqual(french_to_english('0'), '0')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english("None"), '')
        self.assertNotEqual(french_to_english(0), 0)

    def test_english_to_french(self):
        ''' test_2 '''
        self.assertEqual(english_to_french('0'), '0')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french("None"), '')
        self.assertNotEqual(english_to_french(0), 0)




unittest.main()