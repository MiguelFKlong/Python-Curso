#keys() -> devuelve las claves (tambien nos sirve para iterar)
#get() -> devuelve el valor de una clave
#clear() -> elimina todos los elementos
#pop() -> elimina un elemento
#items() -> para iterar el dict

#////////////////////////////////////////////////////////////////
diccionario = {
    "nombre" : 'miguel',
    "apellido" : 'marin',
    "años" : 20
}

#nos devuelve un objeti dict_item
clave = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_ghj = diccionario.get("ghj")
print("continueeeeeeeeee")

#eliminando todo del diccionario
#diccionario.clear()

#eliminado un elemento del diccionario
#diccionario.pop("nombre")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)