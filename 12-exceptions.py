#Manejo de errores#

a = 5

b = 1

b = "1"

try:
    print(a+b)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

#Try except else, si hay except no se ejecuta el else
try:
    print(a+b)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

else:
    print("Sigue la ejecucion")
    

#try except finally, finally siempre se ejecuta aunque aparezca una except 
try:
    print(a+b)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
finally:
    print("siempre se ejecuta")
    
##captura de excepciones por tipo definido.

try:
    print(a+b)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")
    
    ## captura de la informacion del error
try:
    print(a+b)
    print("No se ha producido un error")
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)