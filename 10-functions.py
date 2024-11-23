#funciones#

def my_function():
    print("Esto es una funcion")

my_function()

def sum_two_values (a,b):
    return a+b

my_result= sum_two_values(5,8)
print(my_result)

def print_name(name,surname):
    print(f"{name} {surname}")

print_name(surname="Cirer",name="Domy",)#podemos ordenar de la forma que queremos.


def print_name_with_default(name,surname,alias="Sin alias"):#si no recibe ningun parametro de alias, si coloca por default "Sin alias"
    print(f"{name} {surname} {alias}")

print_name_with_default("Cirer","Domy")#podemos ordenar de la forma que queremos.

def print_texts(*text):#con el asterisco, le puedo pasar infinitos parametros.
    print(text)
    
print_texts("hola", "como estas?","prueba de muchos parametros", "es para pasar muchos textos")