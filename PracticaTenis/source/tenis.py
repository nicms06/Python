import csv
from collections import namedtuple
from datetime import date, datetime

Jugador = namedtuple('Jugador', 'fecha, rival, superficie, duracion,juegos_ganados, juegos_perdidos, ganado')

def lee_fichero(fichero):
    registros = []
    
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        
        for linea in lector:
            fecha_obj = datetime.strptime(linea[0], '%d/%m/%Y').date()            
            rival = linea[1]
            superficie = linea[2]
            duracion = int(linea[3])
            juegos_ganados = int(linea[4])
            juegos_perdidos = int(linea[5])
            ganado = linea[6].lower() == 'true'
        
            registro = Jugador(
                fecha_obj,
                rival,
                superficie,
                duracion,
                juegos_ganados,
                juegos_perdidos,
                ganado   
            )
            registros.append(registro)
    
    return registros

