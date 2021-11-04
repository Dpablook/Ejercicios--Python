# coding=utf-8
# Ejercicio 1.
# Escribir una función que reciba dos valores y verifique cuáles son los
# números primos (divisibles solo por sí mismos y por la unidad) que hay
# entre ambos, incluyendo los dos números ingresados.
# Los valores encontrados deberán ser guardados en un array dentro de la
# función y como último paso, mostrarlos, también desde la función, por
# pantalla.

def verificar(numero1, numero2):
	arreglo=[]
	for valor in range(numero1,numero2):
		if valor%2!=0 and valor%3!=0 and valor%5!=0 and valor%7!=0 or valor==2 or valor==3 or valor==5 or valor==7:
			arreglo.append(valor)
	print(arreglo)

verificar(1,100)
