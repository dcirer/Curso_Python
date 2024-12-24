#Moudulos#

#importar modulo entero
#import module
#module.printValue("como estas?")
#module.sumValues(5,8,45)

#importar funciones especificas de un modulo, para no llamar a todo el modulo
from module import printValue

printValue("como estas?")

#modulos del sistema phyton
import math

print(math.pi)
print(math.pow(2,8))

#se puede llamar directamente 

from math import pi as PI_VALUE
