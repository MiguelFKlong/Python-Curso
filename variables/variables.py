a = 2
b = 3
c = a + b
nombre="Miguel" #Las variables se pueden declarar y definir

numero=10
numero +=1 #podemos usar esto para sumar o restar un numero de variable

#Concatenacion: existen dos formas de hacer
#1er forma: simple

name="Pedrito"
bienvenido="Hola "+name+" ¿Como estas?"


#2da forma: si utilizamos otros tipos de datos podemos usar f-string, siempre se añade la f al principio

#name="juan"
bienvenido=f"Hola {name} ¿Como estas?"


#Se utiliza el operador del para que una variable deje de estar declarada,
# si una variable ya utilizo el valor que se queria borrar se guarda igualmente
#del name
print(bienvenido)

#operadores de pertinencia (in / not in)

print("ola" in bienvenido) #true
print("Pedrito" not in bienvenido) #false


#print(c, nombre, numero)
