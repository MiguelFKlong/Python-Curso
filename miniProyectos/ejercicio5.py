#mini ejercicio de login

listaBD= ["admin", "1234"]
listaIngreso= ["admin", "1234"]

if listaIngreso[0] == listaBD[0]:
    if listaIngreso[1] == listaBD[1]:
        print("INICIANDO SESION...")
else:
    print("ERROR, COLOCO UN DATO ERRONEO")

