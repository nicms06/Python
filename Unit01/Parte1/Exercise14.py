#Escribe un programa en el que declares una constante IVA de valor igual a 21. 
# A continuación, pídele un precio al usuario (recuerda que los precios contienen decimales) 
# y calcula cuál será el precio final con el IVA aplicado.

#Declaramos la constante IVA
IVA = 21

#Pedimos un precio al usuario
precio = float (input ("Introduce el precio: "))

#Calculamos el precio final
precioFinal = precio * (1+(IVA/100))

#Mostramos el resultado
print (f"El precio con IVA es de: {precioFinal:.2f}")