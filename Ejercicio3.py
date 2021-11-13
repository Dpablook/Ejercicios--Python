	# Ejercicio 4.
	# Usando la función ARRAY, declarar un arreglo que contenga los números
	# del 30 al 45.
	# Crear una función que reciba este arreglo por parámetro.
	# Ya dentro de la función, se deberá recorrer el arreglo recibido y generar
	# dos valores a mostrar por pantalla, la cantidad de números impares
	# recibidos en el array y la sumatoria de múltiplos de 3 contenidos también
	# en dicho array

arreglo=[30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]

def verificar(parametro):
	numImpar=0
	numMultiTres=0

	for valor in parametro:
		if valor%2==1:
			numImpar=numImpar+1

		if valor%3==0:
			numMultiTres=numMultiTres+1

	print(numImpar)
	print(numMultiTres)


verificar(arreglo)