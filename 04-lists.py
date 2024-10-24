#listas
#para estructurar datos


#sintaxis
my_list= list()
my_other_list = []

print(len(my_list))

my_list= [33,48,24,56]
print(my_list)
print(len(my_list))

my_other_list = [33,"cirer","dominique",34,"sacudir"]
print(my_other_list)
print(type(my_other_list))

#acceso a los datos por su indice
print(my_other_list[0])
print(my_other_list[-1])

#funciones
print(my_other_list.count(33))

#desempaquetado

edad, apellido, ciudad,otro,tenes = my_other_list
print(edad)

#concatenar listas
print(my_list + my_other_list)

#agregar elementos a la lista
my_other_list.append("Otro")
print(my_other_list)

my_other_list.insert(1, "azul")
print(my_other_list)

#eliminar elementos de la lista
my_other_list.remove("azul")
print(my_other_list)

my_other_list.pop()
print(my_other_list) #elimina el ultimo elemento de la lista y te guarda lo que borraste.

#eliminar por indice

del my_list[2]
print(my_list)

my_list.clear()
print(my_list)

my_new_list= my_other_list.copy()
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

#my_new_list.sort()#sort no soporta mezcla de numeros y strings
#print(my_new_list)

#tomar rango de listas
print(my_new_list[1:3])