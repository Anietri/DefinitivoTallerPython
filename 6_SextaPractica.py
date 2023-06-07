cantidaddeman = int(input("Cuántas manzanas vas a comprar? "))
preciodeman = int(input("Cuál es el precio de las manzanas? "))
total = (cantidaddeman * preciodeman)
descuento:float = 0

if(cantidaddeman > 10): 
    total = total * .9
    descuento = (cantidaddeman * preciodeman)*.1
print(f"Como te estás llevando: {cantidaddeman} y cuestan : {preciodeman} vas a pagar {total} y te ahorraste {descuento}")
