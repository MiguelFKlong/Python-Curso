#creando un conjunto con set
from builtins import frozenset

conjunto = set(["dato 1", "dato 2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1= frozenset({"dato1", "dato2"})
conjunto2= {conjunto1,"dato3"}
#print(conjunto2)

#Teoria de conjunto
conjunto1 ={1,3,5,7}
conjunto2 ={1,3,7}

#verificando si es un subconjunto o no(devuelve true o false)
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto o no(devuelve true o false)
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero en comun(da true si ningun numero es igual, y false cuando hay uno o mas iguales)
resultado= conjunto2.isdisjoint(conjunto1)

print(resultado)
