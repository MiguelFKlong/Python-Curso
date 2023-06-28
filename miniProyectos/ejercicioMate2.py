dado1=[1,2,3,4,5,6]
dado2=[1,2,3,4,5,6]
dado3=[1,2,3,4,5,6]
total = 216
numero_de_seis = 0
numero_mayores_a_ocho = 0
numero_de_siete = 0
numero_mayores_a_doce = 0

#a
for i in range(0,6):
   for j in range(0,6):
        for k in range(0,6):
            if dado1[i]+dado2[j]+dado3[k] == 6:
                #print(f"{dado1[i]},{dado2[j]},{dado3[k]} = {dado1[i] + dado2[j] + dado3[k]}")
                numero_de_seis +=1

#b
for i in range(0,6):
   for j in range(0,6):
        for k in range(0,6):
            if dado1[i]+dado2[j]+dado3[k] > 8:
                #print(f"{dado1[i]},{dado2[j]},{dado3[k]} = {dado1[i] + dado2[j] + dado3[k]}")
                numero_mayores_a_ocho +=1

#c
for i in range(0,6):
   for j in range(0,6):
        for k in range(0,6):
            if dado1[i]+dado2[j]+dado3[k] == 7:
                #print(f"{dado1[i]},{dado2[j]},{dado3[k]} = {dado1[i] + dado2[j] + dado3[k]}")
                numero_de_siete +=1

#d
for i in range(0,6):
   for j in range(0,6):
        for k in range(0,6):
            if dado1[i]+dado2[j]+dado3[k] > 12:
                #print(f"{dado1[i]},{dado2[j]},{dado3[k]} = {dado1[i] + dado2[j] + dado3[k]}")
                numero_mayores_a_doce +=1




prob_que_de_seis = (numero_de_seis/total) * 100
prob_que_de_mayor_a_ocho = (numero_mayores_a_ocho/total) * 100
prob_que_de_siete = (numero_de_siete/total) * 100
prob_que_de_mayor_a_doce = (numero_mayores_a_doce/total) * 100

print(prob_que_de_seis)
print(prob_que_de_mayor_a_ocho)
print(prob_que_de_siete)
print(prob_que_de_mayor_a_doce)

