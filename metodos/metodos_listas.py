#LIST - creamos una lista

#LEN - cuenta la cantidad de elementos de una lista

#APPEND - agrega un elemento a la lista
#INSERT - agrega un elemento a la lista en el "indice" especificado
#EXTEND - agrega varios elementos a la lista

#POP - elimina un elemento de una lista, pide indice y devuelve valor
#REMOVE - remueve un elemento de una lista, pide valor
#CLEAR - elimina todos los elementos de una lista

#SORT - ordena una lista de forma ascendente a descendente
#REVERSE - invierte los elementos de una lista

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#creando una lista con list()
lista= list([79, 58, 3, 5, False, True])

#Devuelve la cantidad de elementos que la lista posee
resultado = len(lista)

#agregando un elemento a la lista
lista.append(45)

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"Toma awita")

#agrega varios elementos a la lista
lista.extend([222, 12, 48, 21, 45])

#eliminando un elemento de una lista por su indice
lista.pop(-1)#para eliminar el ultimo un truco usa -1 y podras eliminarlo con mas facilidad, igual el penultimo

#removiendo un elemento de la lista por su valor
lista.remove("Toma awita")

#eliminando todo los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
#lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificamdo si un elemento se encuentra en la lista
elemento_encontrado= lista.index(5)

print(elemento_encontrado)