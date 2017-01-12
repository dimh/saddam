class Saddam:

	def __init__(self, palabra):
		self.palabra = palabra
		self._ofuscada = '_'*len(palabra)

	def posicion(self, letra):
		posiciones = []
		i = 0
		for l in self.palabra:
			if l == letra:
				posiciones.append(i)
			i += 1
		return posiciones
		
	def ofuscada(self):
		return self._ofuscada
	
	def buscar(self, letra):
		posiciones = self.posicion(letra)
		arrOfuscada = list(self._ofuscada)	
		for p in posiciones:
			arrOfuscada[p]= letra
		self._ofuscada = ''.join(arrOfuscada)
		return self._ofuscada 
