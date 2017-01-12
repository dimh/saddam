import unittest
from models.saddam import Saddam

class SaddamTest(unittest.TestCase):
	def test_validar_letra_X_en_SEXY(self):
		saddam = Saddam('SEXY')
		posicion = saddam.posicion('X')
		self.assertEqual(2, posicion[0])

	def test_validar_letra_H_en_SEXY(self):
		saddam = Saddam('SEXY')
		posicion = saddam.posicion('H')
		self.assertEqual(0, len(posicion))

	def test_validar_letra_X_en_SELECCIONES(self):
		saddam = Saddam('SELECCIONES')
		posicion = saddam.posicion('S')
		self.assertEqual( [0,10], posicion)
