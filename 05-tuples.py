#tuplas#

my_tuple = tuple()

my_other_tuple = (34,21,23,16)

my_tuple=(33,1.80,"Dominique","cirer")
print (my_tuple)
print (type(my_tuple))

print(my_tuple[2])

print(my_tuple.count("Dominique"))
print(my_tuple.index("Dominique"))

#tuplas son inmutables

#concatenar
print(my_tuple + my_other_tuple)

#seleccionar una parte de la tupla
print(my_other_tuple[1:3])