#!/usr/bin/env/ python
import numpy as ma
a = ma.array([5,2,3,1,4,6])
def sort_array(array):
	for x in range(1,len(array)):
		j = x
		while array[j-1] > array[j] and j>0:
			array[j-1],array[j] = array[j], array[j-1]
			j-=1
	return array
def merge_sort(array):
	if array.size < 2:
		raise ValueError('Array must have at least 2 values')

def cuenta_numero(numero):
	if numero == 0:
		return 0
	return numero + cuenta_numero(numero-1)
def cuenta_digitos(numero):
	cont = 0
	if numero > 0:
		cont = 1 + cuenta_digitos(numero//10)
	return cont
def potencia(n1,n2):
	if n1 == 1 or n1 == 0:
		return True
	if n1 <= n2:
		if n1 == n2:
			return True
		else:
			return potencia(n1, n2/n1)
	else:
		return False
def string_pos(a, b):
	pos = 0 - len(b)
	lista = []
	z = a
	while len(z) !=0:
		try:
			pos = a.index(b, pos+ len(b))
			print(pos)
			z = a[pos:]
			lista.append(pos)
		except ValueError as error:
			return lista

def recursion(a, b,lista, posicion):
	if b not in a:
		return 'mama mia'
	else:
		try:
			lista.append(posicion)
			return recursion(a,b,lista, posicion = a.index(b, posicion+len(b)))
		except ValueError as error:
			string = a[:len(b)]
			if string == b:
				return lista
			else:
				lista.pop(0)
				return lista
print(recursion('Un tete a tete con Tete', 'te', lista =[], posicion=0))
def replicar_lista(lista, numero):
	if len(lista) == 0 or numero == 0:
		return []
	else:
		return [lista[0]]*numero + replicar_lista(lista[1:],numero)
def search():
	lista =[1,2,2,2,2,2,5,5,6,6,7,6,8]*1000	
	number = 6
	low = 0
	high = len(lista)-1
	def location_card(lista, number, mid):
		mid_number = lista[mid]
		if mid_number == number:
			if mid-1 >= 0 and lista[mid-1] == number:
				return 'left'
			else:
				return 'found'
		elif number < mid_number:
			return 'left'
		else:
			return 'right'
	def binary_search(lista, number, low, high):
		lista.sort()
		if number not in lista:
			return 'Not found any character'
		if low <= high:
			mid = (low +high)//2
			result = location_card(lista, number, mid)
			if result == 'found':
				return mid
			elif result == 'left':
				return binary_search(lista, number, low= low, high = mid-1)
			elif result == 'right':
				return binary_search(lista, number,low = mid+1, high=high)
	position = binary_search(lista,number, low, high)
	return position

