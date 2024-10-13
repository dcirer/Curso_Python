#Variables

my_string_variable="Esto es un string"
print(my_string_variable)

my_int_variable=34
print(my_int_variable)

my_bool_variable=True
print(my_bool_variable)

#concatenacion
print(my_string_variable,my_bool_variable,my_int_variable)
print("este texto: ",my_string_variable, " tiene: ", len(my_string_variable)," letras")
#funciones del sistema

#cuenta los caracteres, contando los espacios.
print(len(my_string_variable))

#variables en una linea (no es buena practica)

nombre, apellido, edad, mail="dominique","cirer",33, "Domy.741gmail.com"
print("Mi nombre es:",nombre,apellido,". Mi edad es:",edad,". Mi correo es:",mail)

#inputs

name = input("Cual es tu nommbre?")
age = input("Cual es tu edad?")

print(name)
print(age)
