#loops#

#while
#mientras
my_condition=0
while my_condition <10:
    print(my_condition)
    my_condition +=2
else:
    print("Mi condicion es mayor o igual que 10")

print("la ejecucion continua")


while my_condition<20:
    my_condition +=1
    if my_condition ==15:
        print("se detiene la ejecucion")
        break
    print(my_condition)

print("la ejecucion continua")

#FOR#

my_list= [33,48,24,56]

for element in my_list:
    print (element)

my_set={"domy","cirer",32,54,12,76}

for element in my_set:
    print (element)
    
my_tuple = (34,21,23,16)

for element in my_tuple:
    print (element)
    

my_dict = { "Nombre":"Dominique",
                 "Edad":33,
                 "Direccion":"villegas 983",
                 1:"otros datos"}

for element in my_dict:
    print (element)
    

my_dict = { "Nombre":"Dominique",
                 "Edad":33,
                 "Direccion":"villegas 983",
                 1:"otros datos"}

for element in my_dict:
    print (element)
    if element=="Edad":
        break
    print ("Se Ejecuta")
else:
    print("El bucle se frena")