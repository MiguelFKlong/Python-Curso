#mini ejercicio matematico

print("Bienvenido a este ejercicio matematico, que se actualizara cuando, se aprendan nuevos conocimientos")
print("Seleccione un numero para el ejercicio: 1-Suma; 2-Resta; 3-Multi; 4-Division")
num_eleccion= int(input("Digite su respuesta: "))

#Debido a que aun no se sabe varios conceptos de python se opto por esta forma de realizar el ejercicio usando if y elif

if num_eleccion == 1:
    print("Ha seleccionado la modalidad de suma elija dos numeros para probar funcionalidad")
    #Se digita dos numeros y luego se transforma en int para hacer la operacion
    num1= input("Digite el primer numero: ")
    num2 = input("Digite el segundo numero: ")
    resultado= int(num1) + int(num2)

    #por ultimo se imprime el resultado
    print(resultado)

elif num_eleccion == 2:
    print("Ha seleccionado la modalidad de resta elija dos numeros para probar funcionalidad")

    num1 = input("Digite el primer numero: ")
    num2 = input("Digite el segundo numero: ")
    resultado = int(num1) - int(num2)

    print(resultado)

elif num_eleccion == 3:
    print("Ha seleccionado la modalidad de multiplicacion elija dos numeros para probar funcionalidad")

    num1 = input("Digite el primer numero: ")
    num2 = input("Digite el segundo numero: ")
    resultado = int(num1) * int(num2)

    print(resultado)

elif num_eleccion == 4:
    print("Ha seleccionado la modalidad de division elija dos numeros para probar funcionalidad")

    num1 = input("Digite el primer numero: ")
    num2 = input("Digite el segundo numero: ")
    resultado = int(num1) / int(num2)

    print(resultado)

else:
    #si no se selecciona ningun numero de las opciones se muestra este error
    print("Elija uno de los numeros mmhvo")