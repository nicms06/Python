import csv
from collections import namedtuple, defaultdict, Counter
from datetime import datetime, date

# ==========================================
# MODELO DE DATOS
# ==========================================
Venta = namedtuple('Venta', 'id fecha cliente producto cantidad precio beneficio')


# ==========================================
# LECTURA DEL FICHERO
# ==========================================
def leer(nombre: str) -> list[Venta]:
    """
    Abre el fichero CSV en codificación UTF-8, ignora la cabecera,
    convierte cada línea en un objeto Venta y devuelve una lista con todos los registros.
    - fecha: 'dd/mm/aaaa' -> datetime.date
    - cantidad: int
    - precio: float
    - beneficio: float
    """
    ventas = []
    with open(nombre, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector, None)  # Saltar la cabecera

        for linea in lector:
            if not linea or len(linea) < 7:
                continue

            id_venta = linea[0].strip()
            fecha = datetime.strptime(linea[1].strip(), '%d/%m/%Y').date()
            cliente = linea[2].strip()
            producto = linea[3].strip()
            cantidad = int(linea[4])
            precio = float(linea[5])
            beneficio = float(linea[6])

            registro = Venta(id_venta, fecha, cliente, producto, cantidad, precio, beneficio)
            ventas.append(registro)

    return ventas


# ==========================================
# EJERCICIO 1
# ==========================================
def clientes_producto1_y_producto2(ventas: list[Venta], producto1: str, producto2: str) -> set[str]:
    """
    Devuelve un conjunto con los nombres de los clientes que han comprado ambos productos.
    No utiliza bucles explícitos (se emplean comprensiones de conjuntos e intersección).
    """
    clientes_p1 = {v.cliente for v in ventas if v.producto == producto1}
    clientes_p2 = {v.cliente for v in ventas if v.producto == producto2}
    
    # Intersección de ambos conjuntos de clientes
    return clientes_p1 & clientes_p2


# ==========================================
# EJERCICIO 2
# ==========================================
def total_unidades_vendidas(ventas: list[Venta]) -> int:
    """Función auxiliar que calcula el total global de unidades vendidas."""
    return sum(v.cantidad for v in ventas)


def diccionario_porcentaje_cantidad_producto(ventas: list[Venta]) -> dict[str, float]:
    """
    Devuelve un diccionario que relaciona cada producto con el porcentaje de unidades
    vendidas de ese producto respecto al total de unidades vendidas.
    Utiliza la función auxiliar 'total_unidades_vendidas'.
    """
    total = total_unidades_vendidas(ventas)
    if total == 0:
        return {}

    unidades_por_producto = defaultdict(int)
    for v in ventas:
        unidades_por_producto[v.producto] += v.cantidad

    return {
        prod: (cant / total) * 100.0
        for prod, cant in unidades_por_producto.items()
    }


# ==========================================
# EJERCICIO 3
# ==========================================
def producto_mas_vendido(ventas: list[Venta], clientes: set[str], n: int = 3) -> str | None:
    """
    Devuelve el nombre del producto más frecuente entre las n compras
    con mayor número de unidades realizadas por cualquiera de los clientes indicados.
    """
    # 1. Filtrar las ventas pertenecientes a cualquiera de los clientes del conjunto
    ventas_clientes = [v for v in ventas if v.cliente in clientes]
    if not ventas_clientes:
        return None

    # 2. Ordenar las compras de mayor a menor según la cantidad de unidades
    ventas_ordenadas = sorted(ventas_clientes, key=lambda v: v.cantidad, reverse=True)

    # 3. Tomar las n compras con mayor número de unidades
    top_n_ventas = ventas_ordenadas[:n]

    # 4. Contar la frecuencia de aparición de cada producto en esas n compras
    frecuencias = Counter(v.producto for v in top_n_ventas)

    # 5. Obtener y devolver el producto más común
    return frecuencias.most_common(1)[0][0]


# ==========================================
# CÓDIGO DE PRUEBA Y DEMOSTRACIÓN
# ==========================================
if __name__ == '__main__':
    # Creación del fichero de datos de prueba ventas.txt
    contenido_ventas = """id,fecha,cliente,producto,cantidad,precio,beneficio
2051,04/06/2019,ClienteB,ProductoC,11,7.60,2.67
2052,05/06/2019,ClienteA,ProductoA,25,12.00,5.10
2053,06/06/2019,ClienteA,ProductoC,18,7.60,2.67
2054,07/06/2019,ClienteB,ProductoA,30,12.00,5.10
2055,08/06/2019,ClienteC,ProductoB,15,10.00,4.00
2056,09/06/2019,ClienteA,ProductoC,40,7.60,2.67
2057,10/06/2019,ClienteB,ProductoC,5,7.60,2.67
"""
    fichero_prueba = "ventas.txt"
    with open(fichero_prueba, "w", encoding="utf-8") as f:
        f.write(contenido_ventas)

    print("=== 1. Prueba de función 'leer' ===")
    lista_ventas = leer(fichero_prueba)
    for v in lista_ventas:
        print(" ", v)

    print("\n=== 2. Ejercicio 1: Clientes que compraron 'ProductoA' y 'ProductoC' ===")
    ambos_clientes = clientes_producto1_y_producto2(lista_ventas, 'ProductoA', 'ProductoC')
    print(" ", ambos_clientes)

    print("\n=== 3. Ejercicio 2: Porcentaje de unidades vendidas por producto ===")
    porcentajes = diccionario_porcentaje_cantidad_producto(lista_ventas)
    for prod, pct in porcentajes.items():
        print(f"  {prod}: {pct:.2f}%")

    print("\n=== 4. Ejercicio 3: Producto más vendido entre las 3 mayores compras de ClienteA y ClienteB ===")
    top_prod = producto_mas_vendido(lista_ventas, {'ClienteA', 'ClienteB'}, n=3)
    print("  Producto más frecuente:", top_prod)