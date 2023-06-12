milista = [4, 5, 6, 7, 22, 79, 3, 3, 2, 7, 1, 7, 1, 4]
print(milista)
print(milista[5])
print(len(milista))
milista.append(13)#apilar(añadir) un valor
print(milista)


for count, element in enumerate(milista):
    print(f"contador {count} element {element}")
    
if 22 in milista:
    print("Sí está el 22")
    print(milista.index(22))