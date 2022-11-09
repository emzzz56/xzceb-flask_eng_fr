import unittest

from translator import english_to_french, french_to_english

class TestEToF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFToE(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        
unittest.main()