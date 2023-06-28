#Segundo ejercicio:

#le pedimos al usuario que nos diga una frase (o varias)
frase= input("Dime una frase, y vamos a calcular cuanto tardarias en decirlo: ")

#creamos una lista con todas las palabras (se separan cada vez que haya un espacio en blanco)
palabras_separada= frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras= len(palabras_separada)

#en caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Calmate mrko, no te pedi una biblia")

#Calculamos cuanto tardaria en decir las palabras y se lo decimos
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print(f"Dalto lo diria en {cantidad_de_palabras *100 // 2 *1.3 /100} segundos")