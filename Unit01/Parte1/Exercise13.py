#Escribir un programa que solicite las notas del primer, segundo y tercer trimestre 
# (notas enteras que se solicitarán al usuario). El programa debe mostrar la nota media 
# del curso como se utiliza en el boletín de calificaciones (solo la parte entera) y 
# como se usa en el expediente académico (con decimales).

#Pedir notas del primer, segundo y tercer trimestre
primerTrim = int (input ("Introduzca las nostas del primer trimestre: "))
segundoTrim = int (input ("Introduzca las nostas del segundo trimestre: "))
tercerTrim = int (input ("Introduzca las nostas del tercer trimestre: "))

#Calculamos la suma
suma = primerTrim + segundoTrim + tercerTrim

#Calculamos el boletín de calificaciones (parte entera)
boletin = (suma // 3)

#Calculamos el expediente académico (parte con decimales)
expediente = suma /3

#Mostramos
print (str (boletin))
print (f"Expediente : {expediente:.2f}")