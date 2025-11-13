#Realiza un conversor de pesetas a euros. Para ello, pídele al usuario que te introduzca el valor 
#en pesetas y, a posteriori, debes mostrarle el resultado de la conversión.(1€ = 166 ptas).

#Preguntar por las pesetas
pesetas = int (input ("Introduzca las pesetas: "))

#calcular los euros
euros = float (pesetas/166)

#Mostrar los euros
print (f"{pesetas} pesetas = {euros:.2f} EUR")