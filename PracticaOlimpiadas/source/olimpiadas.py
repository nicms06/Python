import csv
from collections import namedtuple
Atleta = namedtuple('Atleta', 'nombre,edad,pais,peso')

def leer_fichero(nombre_fichero):
    registros = []
    
    with open(nombre_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) #saltamos la primera línea
        
        for linea in lector:
          nombre = linea[0]
          edad = int(linea[1])
          pais = linea[2]
          peso = float(linea[3])
          
          tupla= Atleta(nombre, edad, pais, peso)
          registros.append(tupla)         
    
    return registros

def edad_media(registros):
    suma_edades = 0
    
    for registro in registros:
        suma_edades += registro.edad
    
    return suma_edades / len(registros)

# def num_atletas_por_pais(registros):
#     numero_atletas = {}
    
#     for registro in registros:
#         if  in 