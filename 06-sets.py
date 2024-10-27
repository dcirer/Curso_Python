#sets#

#no es una estructura ordenada, no se puede recorrer cada elemento.
#no acepta duplicados

my_set=set()
my_other_set={}#tiene la misma sintaxis que los diccionarios, pero depende como llenas.

print(type(my_set))
print(type(my_other_set))
my_set={"tata",12312,"asdasd"}
my_other_set={"domy","cirer",32,54,12,76}#cuando lo paso enformato tipo lista, un dato al lado del otro
print(type(my_other_set))#se transforma en sets

print(len(my_other_set))

my_other_set.add("otro") #agrega desordenado
print(my_other_set)

#si agregas dos veces el mismo dato no lo agrega. no agrega duplicados.
my_other_set.add("otro") 
print(my_other_set)

#busqueda
print("domy" in my_other_set) #para verificar si hay un elemento en el sets
print("domi" in my_other_set)


#eliminar
my_other_set.remove(32)
print(my_other_set)

#my_other_set.clear()
#print(my_other_set)
#print(len(my_other_set))

my_new_set=my_other_set.union(my_set)
print(my_new_set)