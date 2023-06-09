cantidaddeman = int(input("Cuántas manzanas vas a comprar? "))
preciodeman = int(0)
total = int(0)
descuento = int(0)
while cantidaddeman != 0:
    preciodeman = int(input("Cuál es el precio de las manzanas? "))
    nombre = input("¿Cuál es tu nombre?    ")
    total = (cantidaddeman * preciodeman)
    descuento:float = 0
    if(cantidaddeman == 18 or nombre == "andres"):
        total = total * .8
        descuento = (cantidaddeman * preciodeman)*.2
    elif(cantidaddeman > 10): 
        total = total * .9
        descuento = (cantidaddeman * preciodeman)*.1
    print(f"Como te estás llevando: {cantidaddeman} y cuestan : {preciodeman} vas a pagar {total} y te ahorraste {descuento}")
    break