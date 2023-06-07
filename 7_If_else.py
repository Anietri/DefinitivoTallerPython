dia = input("Ingresa el día de la semana:  ")

if dia == "lunes" or dia == "miercoles":
    print("Toca curso")
elif dia == "viernes": ##El elif nos ayuda a seguir la secuencia del if anterior
    print("Toca curso")
    print("Toca peda")
elif dia == "jueves":
    print("Ya casi es viernes")
else:
    print("Toca descansar")

print("Felicidades")