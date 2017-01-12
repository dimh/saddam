class Saddam:

	def __init__(self, palabra):
		self.palabra = palabra
		self.ofuscada = '_'*len(palabra)

	def posicion(self, letra):
		posiciones = []
		i = 0
		for l in self.palabra:
			if l == letra:
				posiciones.append(i)
			i += 1
		return posiciones
		
	def ofuscada():
		return self.ofuscada
