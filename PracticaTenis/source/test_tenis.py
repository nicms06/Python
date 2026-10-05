from tenis import *

def test_lee_fichero(registros):
    print('Proyecto Tenis')
    print('Imprimiendo los 3 primeros:')
    for jugador in registros[:3]:
        print(jugador)
    
if __name__ == "__main__":
    
    registros = lee_fichero('./data/datos.txt')
    test_lee_fichero(registros)