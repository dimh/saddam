import unittest
from models.words import Word

class SaddamTest(unittest.TestCase):
    def test_get_word(self):
        word_class = Word()
        word = word_class.generar_palabra()
        self.assertEqual('MORIN', word)