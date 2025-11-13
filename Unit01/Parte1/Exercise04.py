# Crear una aplicación que calcule la media aritmética de dos notas enteras. 
# Hay que tener en cuenta que la nota media puede tener decimales.

#Ask the user for the marks
mark1 = int (input ("Input the first mark: "))
mark2 = int (input ("Input the second mark: "))

#Calculate the mean
mean = float ((mark1 + mark2) / 2)

#Show the mean
print ("The mean is: " + str (mean))