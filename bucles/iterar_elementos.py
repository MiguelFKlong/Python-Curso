#creando listas o tuplas, etc
lista_animales = ["gato","perro","loro","cocodrilo","cococabra"]
numeros = [10, 16, 18, 6, 9]

#recorriendo la lista animales
for animal in lista_animales:
    print(f"Ahora la variable animal es igual a: {animal}")

print("-------------------------------------------")

#recorriendo la lista numeros y multiplicando cada valor por 10
for num in numeros:
    rst = num * 10
    print(f"El resultado es {rst}")

print("----------------------------------------------")

#usamos la funcion zip para recorrer dos o mas listas
#iterando dos listas del mismo tamaño al mismo tiempo
for num,animal in zip(lista_animales, numeros):
    print(f"recorriendo lista 1: {num}")
    print(f"recorriendo lista 2: {animal}")

print("---------------------------------------")

#usamos range para recorrer desde un numero hasta el rango que le demos
for num in range(5,10):
    print(num)

print("---------------------------------------")

#forma no optima de recorrer una lista con su indice(no funciona con conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

print("-----------------------------------------")

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice}, y el valor es: {valor}")

print("----------------------------------------")

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

#todo lo anterior funciona exactamente igual para tuplas y conjuntos

#print("------------------------------")
#for num,i in enumerate(numeros):
    #print(f"num es: {num} e i es: {i}")
