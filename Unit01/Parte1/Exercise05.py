# Diseñar una aplicación que calcule la longitud y el área de una circunferencia. 
# Para ello, el usuario debe introducir el radio, que puede contener decimales. 
# Usa Math.PI para tomar el valor de PI. (longitud = 2πr, área=πr2)

#import the library math
import math

#Ask the user for the radius
radius = float (input ("Please, input the radius: "))

#Calculate the length and area
length = float (2*(math.pi)*radius)
area = float((math.pi)*radius**2)

#Show the results
print ("The area is " + str (area) + "\n The length is: " + str (length))