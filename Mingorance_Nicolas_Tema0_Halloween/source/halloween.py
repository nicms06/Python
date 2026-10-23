from collections import namedtuple
import csv
from datetime import datetime

Visita = namedtuple('Visita', 'codigo fecha grupo recorrido personas minutos sustos precio')

#Ejercicio 01
def leer_visitas(ruta):
    registros = []
    
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) 
            
        for linea in lector:
            codigo = linea[0]
            fecha = datetime.strptime(linea[1], '%d/%m/%Y').date()
            grupo = linea[2]
            recorrido = linea[3]
            personas = int(linea[4])
            minutos = int(linea[5])
            sustos = int(linea[6])
            precio = float(linea[7])
              
            tupla= Visita(codigo, fecha, grupo, recorrido, personas, minutos, sustos, precio)
            registros.append(tupla)         
        
    return registros

#Ejercicio 02
def recaudacion(visitas, recorrido):
    resultado = 0
    
    for visita in visitas:
        if visita.recorrido == recorrido:
            resultado += (visita.personas * visita.precio)
    
    return resultado

#Ejercicio 03
def visitas_rapidas(visitas, sustos_minimos, duracion_maxima):
    lista = []
    
    for visita in visitas:
        if visita.sustos >= sustos_minimos and visita.minutos <= duracion_maxima:
            lista.append(visita.codigo)
    
    lista.sort()
        
    return lista

#Ejercicio 04
def asistencia_por_recorrido(visitas):
    resultado = {}
    
    for visita in visitas:
        clave = visita.recorrido
        if clave in resultado:
            resultado[clave] += visita.personas
        else:
            resultado[clave] = visita.personas
    
    return resultado
