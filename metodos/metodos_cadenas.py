#DIR - devuelve la lista de atributos validos del objeto pasado., es una funcion

#UPPER - convierte a mayuscula
#LOWER - convierte a minuscula
#CAPITALIZE - primera en mayuscula

#FIND - metodo que encuentra la primera aparicion del valor especificado, sino devuelve -1
#INDEX - metodo que encuentra la primera aparicion del valor especificado, sino devuelve una excepcion

#ISNUMERIC - si es numerico devuelve True
#ISALPHA - si es alfa numerico devuelve True

#COUNT - devuelve el numero de ocurriencias de una subcadena en la cadena dada.
#LEN - cuenta los caracteres de una cadena

#ENDSWITH - verifica si una cadena comienza con
#STARTSWITH - verifica si una cadena termina con

#REPLACE - reemplaza un valor por otro
#SPLIT - separa por el parametro dado

#PRUEBAS
cadena1= "Hola,soy,Miguel,mmhvo,pvta,zorra"
cadena2= "Wenaaaas mmhuevo"

#Convierte a mayuscula
mayus = cadena1.upper() #esta es la manera de tarbajar con un metodo
#mayus = "hola".upper()

#Convierte a mayuscula
minus = cadena1.lower()

#Convierte la primera letra a Mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
busqueda_find= cadena1.find("e")

#buscamos una cadena en otra cadena, si no hay coincidencia lanza un error
busqueda_index= cadena1.index("M")

#si es numero nos devuelve true, sino false
es_numerico= cadena1.isnumeric()

#si es alfa numerico se devuelve true, si no false
#es_alfanumerico= cadena1.isalpha()

#contamos las coincidencias de una cadena y devuelve la cantidad de veces que coincida
contar_coincidencia= cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres= len(cadena1)#es una funcion, no metdo

#verificamos si un una cadena empieza con otra cadena dada, si es asi devuelve true
empienza_con= cadena1.startswith("a")

#verificamos si un una cadena termina con otra cadena dada, si es asi devuelve true
termina_con= cadena1.endswith("Miguel")

#si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada= cadena1.split(",")

print(cadena_separada[4])

