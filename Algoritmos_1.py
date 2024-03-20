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
def merge(array:list)->list:
    left = []
    right = []
    if(len(array)==1):
        return array
	#Dividimos el arreglo a la mitad
    middle = int(len(array)/2)
    left = array[:middle]
    right = array[middle:]
    divided_array_l=merge(left)
    dividev_array_r=merge(right)
    return mergesort(divided_array_l,dividev_array_r)

def mergesort(left:list,right:list)->list:
    result = []
	#Pasamos el arreglo dividido, primero cuando estan solos, despues cuando se hacen pareja, y ps poco a poco los juntamos, y vamos decidiendo cual es mayor
    while len(left)>0 and len(right)>0:
        if left[0]>right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    while len(left)>0:
        result.append(left[0])
        left.pop(0)
    while len(right)>0:
        result.append(right[0])
        right.pop(0)
    return result

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
def terneria(lim_inf:int,lim_sup:int,array:list):
	'''ordenamos el arreglo'''
	array.sort()
	'''el numero a buscar en el arreglo'''                       
	num_buscar = 6
	'''estas tres líneas las cheque en un codigo para obtener las particiones'''                      
	size = lim_sup-lim_inf 
	'''este es el primer tercio'''             
	left = int(lim_inf+(size/3)) 
	'''este es el tercer tercio, '''
	right = int(lim_inf+((size*2)/3))   
	'''El tercer tercio es el de enmedio y abarca desde[left:right]'''
	if(lim_inf<=lim_sup):
		'''Si el lim_inf es mayor entonces no encontramos el numero'''
		if(array[left] == num_buscar):  
			''' Checamos si el numero es igual'''
			if (array[left-1]==num_buscar):  
				lim_inf-=1
	#CASO ESPECIAL CHECAMOS SI EL NUMERO ANTERIOR NO ES EL DEL MISMO ARREGLAR, PARA ASI ENCONTRAR LA PRIMERA POSICION
				lim_sup=left-1
				return terneria(lim_inf, lim_sup, array)
			else:
				#RETORNAMOS LA POSICION, EL NUMERO A BUSCAR, Y EL ANTERIOR A ESE NUMERO
			    return left+1,array[left+1],array[left-1]
		elif(num_buscar< array[left]):
			#EL ARREGLO AHORA VA A SER DE LA PRIMERA POSICION HASTA EL SEGUNDO TERCIO
			lim_sup = left-1
			
			return terneria(lim_inf,lim_sup,array)
		else:
			#SI ES MAYOR EL ARREGLO VA A EMPEZAR DEL SEGUDO TERCIO HASTA EL FINAL DEL ARREGLO
			lim_inf=right+1
			return terneria(lim_inf,lim_sup,array)
	else:
		return -1#Si no encontramos el numero
