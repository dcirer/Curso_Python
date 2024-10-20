##Strings

my_string = "Mi String"
my_other_string = "Mi Otro String"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)


#formateo 

name, surname, age = "Domy","cirer",33
print('Soy {} {} y tengo {}'.format(name, surname, age))
print('Soy %s %s y tengo %d'%(name, surname, age))

print(f'Soy {name} {surname} y tengo {age}')

#desempaquetado de string
language="python"
a,b,c,d,e,f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#division

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-3]
print(language_slice)

#reverse

reversed_language= language[::-1]
print(reversed_language)

#funciones

print(language.capitalize())  #pone la primera mayuscula
print(language.upper()) #pone todo en mayuscula
print(language.count("o"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("pygit"))

