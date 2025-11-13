#Escribir un programa que pida un número al usuario e indique mediante un 
#literal booleano (true o false) si el número es par.

#Ask the user for a number
num = int (input ("Input a number: "))

print ("Is " + str (num) + " an even number?")

print (num % 2 == 0)