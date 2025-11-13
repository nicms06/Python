#Escribir una aplicación que pida el año actual y el año de nacimiento del usuario. Debe calcular su edad.

#Ask the user for the current year
year = int (input ("Input this year: "))

#Ask the user for his year of birth
bornYear = int (input ("Input your year of birth: "))

#Calculate the age

age = year - bornYear

print ("You are " + str(age))