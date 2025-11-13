#Un frutero necesita calcular los beneficios anuales que obtiene de la venta de manzanas y peras. 
#Por este motivo, es necesario diseñar una aplicación que solicite las ventas (en kilos, tanto 
#de las peras como de las manzanas). La aplicación mostrará el importe total sabiendo que el 
# precio del kilo de manzanas está fijado en 2,35€ y el kilo de peras en 1,95€.

#Declaramos el precio de las manzanasy peras
PRECIO_MANZANAS = 2.35
PRECIO_PERAS = 1.95

#Pedir los kilos de manzanas y peras
kilosManzanas = float (input ("Introduzca los kilos de manzanas: "))
kilosPeras = float (input ("Introduzca los kilos de peras: "))

#Calcular el importe total
importeTotal = (PRECIO_MANZANAS * kilosManzanas) + (PRECIO_PERAS * kilosPeras)

#Mostrar el importe total
print (f"El importe total es {importeTotal:.2f}")