#dicts#
my_dict= dict()

my_other_dict = { }

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = { "Nombre":"Dominique",
                 "Edad":33,
                 "Direccion":"villegas 983",
                 1:"otros datos"}
#puede tener una clave tanta númerica como string

my_dict={
    "Nombre":"Dominique",
    "Edad":33,
    "Direccion":"villegas 983",
    "datos":{"concubinato","perro","gato"}
}
#dentro del diccionario podemos guardar otros datos como un set
#Estructura para guardar muchos tipos de datos

print(my_dict)
print(my_other_dict)

#con el len te cuenta la cantidad de claves que tiene el diccionario.
print(len(my_other_dict))

print(my_other_dict["Edad"])

my_other_dict["Edad"]=35 #se pueden actualizar datos del diccionario
print(my_other_dict["Edad"])

#para agregar un nuevo dato
my_other_dict["Profesion"]="programador"
print(my_other_dict)

#para elminar un elemento del diccionario
del my_other_dict["Direccion"]
print(my_other_dict)

print("Dominique" in my_other_dict) #false porque busca indices unicamente.
print("Nombre" in my_other_dict)

print(my_dict.keys())
print(my_dict.items())#arroja una lista de las keys del diccionario

my_new_dict=dict.fromkeys(my_other_dict)
print(my_new_dict)

print(my_dict.values())