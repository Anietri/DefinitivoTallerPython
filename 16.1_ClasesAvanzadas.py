class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def saludo(self):
        print(f"Hola, mi nombre es {self.name} y mi edad es {self.age} años")

p1 = Person("Andres", 28)
p2 = Person("Paula", 23)

p1.saludo()
p2.saludo()
    