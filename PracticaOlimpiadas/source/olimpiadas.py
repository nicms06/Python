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

def num_atletas_por_pais(registros):
    resultado = {}
    for atleta in registros:
        clave = atleta.pais
        if clave in resultado:
            resultado[clave] += 1
        else:
            resultado[clave] = 1
            
    return resultado

def nombre_atletas_por_pais(registros):
    resultado = {}
    for atleta in registros:
        clave = atleta.pais
        if clave in resultado:
            resultado[clave].append(atleta.nombre)
        else:
            resultado[clave] = [atleta.nombre]
            
    return resultado

def  atleta_mayor_peso(registros):
    mayor_peso = registros[0].peso
    nombre_mayor_peso = registros[0].nombre
    for atleta in registros:
        if (atleta.peso > mayor_peso):
            mayor_peso = atleta.peso
            nombre_mayor_peso = atleta.nombre
            
    return nombre_mayor_peso

def pais_mayor_peso_medio(registros):
    pesos_por_pais = {}
    for atleta in registros:
        clave = atleta.pais
        if clave in pesos_por_pais:
            pesos_por_pais[clave].append(atleta.peso)
        else:
            pesos_por_pais[clave] = [atleta.peso]
    
    pais_max = None
    max_media = 0
    
    for pais, pesos in pesos_por_pais.items():
        media = sum(pesos) / len(pesos)
        if media > max_media:
            max_media = media
            pais_max = pais
            
    return pais_max

