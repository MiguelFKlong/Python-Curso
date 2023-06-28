a=20
b=29
c=30

if a & b >= c:
    print("ambos son mayores")

elif a | b >= c:
    if a >= c: #para que no haya errores identifica bien las condiciones
        print("a es mayor o igual")
    elif b >= c:
        print("b es mayor o igual")

else:
    print("ninguno es mayor")
