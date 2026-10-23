from halloween import *

def test_lee_fichero(registros):
    print()
    print("+ Leidos: ", len(registros), " registros")
    print('\n+ Mostrando los tres primeros')
    for atleta in registros[:3]:
        print('\t',atleta,sep='')
        
    print('\n+ Comprobaciones Ejercicio 1:')
    print('\t', len(registros))
    print('\t', registros[0].codigo)
    print('\t', registros[0].fecha)
    
    print('\n+ Comprobaciones Ejercicio 2:')
    print('\t', recaudacion(registros, 'Cripta'))
    print('\t', recaudacion(registros, 'Mansión'))
    
    print('\n+ Comprobaciones Ejercicio 3:')
    print('\t', visitas_rapidas(registros,   30, 29))
    
    print('\n+ Comprobaciones Ejercicio 4:')
    print('\t', asistencia_por_recorrido(registros))

if __name__ == "__main__":
    print("Proyecto Halloween")
    registros = leer_visitas('./data/visitas_halloween.txt')
    
    test_lee_fichero(registros)