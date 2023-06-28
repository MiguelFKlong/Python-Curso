#promedio de duracion
otros_cursos_min= 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso=1.5

#duracion de crudo
crudo_promedio= 5
crudo_dalto= 3.5

#diferencias de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10 #
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

#Calculando el porcentuaje de tiempo vacio
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto= 100 - dalto_curso * 1000 // crudo_dalto / 10

#mostrando las diferencias de duracion(Ejercicio A)
print("------------------------------------------")
print("El curso de Dalto dura:")
print(f" - un {diferencia_con_min}% menos que el mas rapido")
print(f" - un {diferencia_con_max}% menos que el mas lento")
print(f" - un {diferencia_con_promedio}% menos que el promedio")
print("------------------------------------------")

#mostrando la cantidad de espacio vacio que se remueve(Ejercicio b)
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")
print("------------------------------------------")


#mostrando diferencias si los cursos duraran 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas del curso de dalto")

