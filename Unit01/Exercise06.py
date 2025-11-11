# Escribir un programa que le pida dos números al usuario. 
# A continuación, debe mostrar la suma, la resta, la multiplicación y la división de ambos números. 
# Debe mostrarse el resultado de cada operación en una línea distinta.

#Ask the user for 2 numbers
num1 = int (input ("Input the first number: "))
num2 = int (input ("Input the second number: "))

#Calculate the add, sub, mult, div
add = num1 + num2
sub = num1 - num2
mult = num1 * num2

#Print the solutions
print (str(num1) + " + " + str(num2) + " = " + str(add))
print (str(num1) + " - " + str(num2) + " = " + str(sub))
print (str(num1) + " * " + str(num2) + " = " + str(mult))

#Conditional because you can't divide by 0
if num2 == 0:
    print ("You can't divide by 0")
else:
    div = float (num1 / num2)
    print (str(num1) + " / " + str(num2) + " = " + str(div))