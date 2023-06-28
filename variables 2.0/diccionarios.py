#creando diccionario con dict()
diccionario = dict(nombre="lucas", apellido="manolo")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {("dalto", "rancio"):"jajajajajjajaja"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario1 = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "Paquito"
diccionario2 = dict.fromkeys(["nombre", "apellido"], "Paquito")

print(diccionario2["nombre"])

print(diccionario)