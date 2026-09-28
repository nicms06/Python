from olimpiadas import *

def test_lee_fichero(registros):
    print()
    print("Test de la función lee_fichero")
    print("\tLeidos: ", len(registros), " registros")
    print('\tMostrando los tres primeros')
    for atleta in registros[:3]:
        print('\t',atleta,sep='')

if __name__ == "__main__":
    print("Proyecto Olimpiadas")
    registros = leer_fichero('./data/atletas.txt')
    
    test_lee_fichero(registros)
    