#Creando una lista (se pueden modificar)
lista:list = ["Miguel Marin", "Fklong", True, 1.85]

#esto es valido
lista[3]=29

#Creando tuplas (no se pueden modificar)
tupla=("Miguel Marin", "Fklong", True, 1.85)

#esto no
#tupla[3]=29

#(lista, tupla[1])

#creando un conjunto (set)(no se accede a elementos por indice, no se almacena datos duplicados, es desordenado, y se accede utilizando bucles)
conjunto = {"Miguel Marin", "Fklong", True, 1.85}

#creando un diccionario(dict)
diccionario= {
    "nombre" : "Miguel Marin",
    "profesion" : "estudiante",
    "esta_emocionado" : True,
    "altura" : 1.84,
    "dato_duplicado" : "Miguel Marin"
}

print(diccionario["profesion"])
print(lista)