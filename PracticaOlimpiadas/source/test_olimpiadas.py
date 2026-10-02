from olimpiadas import *

def test_lee_fichero(registros):
    print()
    print("Test de la función lee_fichero")
    print("\tLeidos: ", len(registros), " registros")
    print('\tMostrando los tres primeros')
    for atleta in registros[:3]:
        print('\t',atleta,sep='')
    print('\tEdad media:', edad_media(registros))
    print('\tAtletas por país:', num_atletas_por_pais(registros))
    print('\tNombre de atletas por país:', nombre_atletas_por_pais(registros))
    print('\tAtleta con mayor peso:', atleta_mayor_peso(registros))
    print('\t Pais con mayor peso medio:', pais_mayor_peso_medio(registros))

if __name__ == "__main__":
    print("Proyecto Olimpiadas")
    registros = leer_fichero('./data/atletas.txt')
    
    test_lee_fichero(registros)    