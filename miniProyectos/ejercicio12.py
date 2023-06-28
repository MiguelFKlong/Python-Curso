datos1= ["Miguel", "Maron", 23, 180, "paquito", True]

nombre, color, edad, cm, nickname, existe = datos1

datos2 ={nombre, edad, cm}
datos3 ={nombre, color, edad, cm, nickname, existe}

resultado= datos2.issubset(datos3)
resultado2= datos3.issuperset(datos2)
resultado3= datos2.isdisjoint(datos3)

print(f"datos2 es subconjunto de datos3?: {resultado}")
print(f"datos3 es superconjunto de datos2?: {resultado2}")
print(f"No se repite algun datos entre ambos conjuntos?: {resultado3}")

datos2="Angel",

nombre = datos2


#se puede combinar tupla y lista, de una manera sencilla pero rustica
print(nombre, color)