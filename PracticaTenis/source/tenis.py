import csv
from collections import namedtuple, defaultdict, Counter
from datetime import datetime, date

# ==========================================
# MODELO DE DATOS
# ==========================================
Partido = namedtuple('Partido', 'fecha rival superficie duracion juegos_ganados juegos_perdidos ganado')


# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def _parse_bool(cadena: str) -> bool:
    """Convierte una cadena a booleano de forma flexible."""
    return cadena.strip().lower() in ('true', '1', 'verdadero', 'v', 's', 'si', 'sí')


def _parse_fecha(cadena: str) -> date:
    """Parsea una cadena de texto a un objeto date soportando formatos comunes."""
    cadena = cadena.strip()
    for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y'):
        try:
            return datetime.strptime(cadena, fmt).date()
        except ValueError:
            pass
    return datetime.strptime(cadena, '%Y-%m-%d').date()


def diferencia_juegos(partido: Partido) -> int:
    """Función auxiliar que calcula la diferencia entre juegos ganados y perdidos."""
    return partido.juegos_ganados - partido.juegos_perdidos


# ==========================================
# LECTURA DEL FICHERO
# ==========================================
def lee_fichero(fichero: str) -> list[Partido]:
    """
    Abre el fichero en UTF-8, ignora la cabecera, convierte los datos
    a sus tipos correspondientes y devuelve una lista de objetos Partido.
    """
    partidos = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector, None)  # Saltar la cabecera

        for linea in lector:
            if not linea or len(linea) < 7:
                continue

            fecha = _parse_fecha(linea[0])
            rival = linea[1].strip()
            superficie = linea[2].strip()
            duracion = int(linea[3])
            juegos_ganados = int(linea[4])
            juegos_perdidos = int(linea[5])
            ganado = _parse_bool(linea[6])

            registro = Partido(fecha, rival, superficie, duracion, juegos_ganados, juegos_perdidos, ganado)
            partidos.append(registro)

    return partidos


# ==========================================
# EJERCICIO 1
# ==========================================
def desviaciones_media(partidos: list[Partido], n: float) -> list[tuple[float, Partido]]:
    """
    Devuelve una lista de tuplas (desviacion, partido) con los partidos cuya duración
    supere en 'n' o más minutos la duración media de todos los partidos.
    Utiliza una comprensión de lista (sin bucles explícitos).
    """
    if not partidos:
        return []

    media = sum(p.duracion for p in partidos) / len(partidos)
    
    # Comprensión de listas sin bucle explícito for/while tradicional
    return [(p.duracion - media, p) for p in partidos if (p.duracion - media) >= n]


# ==========================================
# EJERCICIO 2
# ==========================================
def diccionario_diferencia_juegos_superficie(partidos: list[Partido], n: int = 3) -> dict[str, list[date]]:
    """
    Devuelve un diccionario que relaciona cada superficie con las fechas de los 'n' partidos
    jugados en esa superficie con mayor diferencia entre juegos ganados y perdidos.
    Utiliza la función auxiliar 'diferencia_juegos'.
    """
    partidos_por_superficie = defaultdict(list)
    for p in partidos:
        partidos_por_superficie[p.superficie].append(p)

    resultado = {}
    for superficie, lista in partidos_por_superficie.items():
        # Ordenamos los partidos de mayor a menor diferencia de juegos usando la función auxiliar
        ordenados = sorted(lista, key=diferencia_juegos, reverse=True)
        # Extraemos las fechas de los primeros n partidos
        fechas = [p.fecha for p in ordenados[:n]]
        resultado[superficie] = fechas

    return resultado


# ==========================================
# EJERCICIO 3
# ==========================================
def rival_mayor_porcentaje_victorias(partidos: list[Partido], superficie: str) -> tuple[str, float]:
    """
    Devuelve una tupla (rival, porcentaje) con el rival frente al que se haya obtenido
    el mayor porcentaje de victorias en la superficie indicada.
    """
    # Filtrar partidos jugados en la superficie dada
    partidos_sup = [p for p in partidos if p.superficie.lower() == superficie.lower()]
    if not partidos_sup:
        return (None, 0.0)

    totales_por_rival = Counter()
    victorias_por_rival = Counter()

    for p in partidos_sup:
        totales_por_rival[p.rival] += 1
        if p.ganado:
            victorias_por_rival[p.rival] += 1

    # Calcular porcentajes
    porcentajes = {
        rival: (victorias_por_rival[rival] / total) * 100.0
        for rival, total in totales_por_rival.items()
    }

    # Obtener el rival con el porcentaje máximo
    rival_max = max(porcentajes, key=porcentajes.get)
    return (rival_max, porcentajes[rival_max])


# ==========================================
# PRUEBAS DE FUNCIONAMIENTO
# ==========================================
if __name__ == '__main__':
    # Creación de un archivo de prueba datos.txt
    contenido_ejemplo = """fecha,rival,superficie,duracion,juegos_ganados,juegos_perdidos,ganado
2020-10-11,Novak Djokovic,Tierra,160,19,7,True
2021-06-05,Rafael Nadal,Tierra,180,18,15,True
2021-07-10,Roger Federer,Hierba,120,18,10,True
2022-01-30,Daniil Medvedev,Dura,300,19,17,True
2022-06-05,Casper Ruud,Tierra,130,18,6,True
2022-09-11,Carlos Alcaraz,Dura,200,12,18,False
2023-06-11,Novak Djokovic,Tierra,190,12,18,False
2023-07-16,Carlos Alcaraz,Hierba,280,15,19,False
2023-07-10,Novak Djokovic,Hierba,110,18,8,True
"""
    with open("datos.txt", "w", encoding="utf-8") as f:
        f.write(contenido_ejemplo)

    print("=== 1. Prueba de lee_fichero ===")
    partidos = lee_fichero("datos.txt")
    print(f"Se han cargado {len(partidos)} partidos.")
    for p in partidos[:3]:
        print(" ", p)

    print("\n=== 2. Ejercicio 1: desviaciones_media (n=20) ===")
    desviaciones = desviaciones_media(partidos, n=20)
    for desv, p in desviaciones:
        print(f"  Desviación: {desv:+.2f} min | Rival: {p.rival} ({p.duracion} min)")

    print("\n=== 3. Ejercicio 2: diccionario_diferencia_juegos_superficie (n=2) ===")
    dic_juegos = diccionario_diferencia_juegos_superficie(partidos, n=2)
    for sup, fechas in dic_juegos.items():
        print(f"  Superficie '{sup}': {fechas}")

    print("\n=== 4. Ejercicio 3: rival_mayor_porcentaje_victorias (Tierra) ===")
    rival, pct = rival_mayor_porcentaje_victorias(partidos, "Tierra")
    print(f"  Rival top en Tierra: {rival} ({pct:.1f}% victorias)")