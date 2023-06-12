import os


def clear():
    if os.name == "ce" or os.name=="nt" or os.name == "dos":
        os.system ("cls") 

def saludo():
    print("Hola, buenos días")