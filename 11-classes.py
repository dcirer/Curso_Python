##Clases##

class EmptyPerson:
    pass #palabra reservada para crear un class que no hace nada.
    
class Person:
    def __init__(self, name, surname):
        self.fullname= f"{name} {surname}"
    
    def walk(self):
        print(f"{self.fullname} esta caminando")

my_person= Person("Dominique","Cirer")

print(my_person.fullname)
my_person.walk()