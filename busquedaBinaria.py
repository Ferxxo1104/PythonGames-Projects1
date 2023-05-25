import random
import time


def busquedaIngenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busquedaBinaria(lista, objetivo, limInf = None, limSup = None):
    if limInf is None:
        limInf = 0 #Inicio de la lista
    if limSup is None:
        limSup = len(lista)-1 #Final de la lista

    if limSup < limInf:
        return -1
    
    puntoMedio = (limInf + limSup) // 2

    if lista[puntoMedio] == objetivo:
        return puntoMedio
    elif objetivo < lista[puntoMedio]:
        return busquedaBinaria(lista,objetivo,limInf,puntoMedio - 1)
    else:
        return busquedaBinaria(lista, objetivo, puntoMedio + 1,limSup)
    

if __name__== '__main__':
    # CREAR UNA LISTA CON 10K Numeros aleatorios
    tamaño = 100000
    conjutoInicial = set()

    while len(conjutoInicial) < tamaño:
        conjutoInicial.add(random.randint(-3*tamaño, 3*tamaño))

    listaOrdenada = sorted(list(conjutoInicial))

    # #medir el tiempo de busqueda ingenua
    # inicio = time.time()
    # for objetivo in listaOrdenada:
    #     busquedaIngenua(listaOrdenada, objetivo)
    # fin = time.time()
    # print(F"Tiempo de busqueda ingenua: {fin - inicio} segundos.") 
    
    #medir el tiempo de busqueda Binaria
    inicio = time.time()
    for objetivo in listaOrdenada:
        busquedaBinaria(listaOrdenada, objetivo)
    fin = time.time()
    print(F"Tiempo de busqueda Binaria: {fin - inicio} segundos.")