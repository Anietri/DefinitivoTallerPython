class person:
    name:str
    age:int
    
    def greeting():
        print(f"Hola, mi nombre es {name}")
    
person1=person
person1.name="Andrés"
person1.age=28

print(person1.name)
person1.greeting()
print(person1.age)