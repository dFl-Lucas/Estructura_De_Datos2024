from listaSecuencial import ListaSecuencial
from listaEncadenada import ListaEncadenada
import random

class Elemento_Matriz:
    __fila: int
    __columna: int
    __valor: int

    def __init__(self, fila, columna, valor):
        self.__fila = fila
        self.__columna = columna
        self.__valor = valor

    def __str__(self):
        return f'Fila: {self.__fila}\nColumna: {self.__columna}\nValor: {self.__valor}\n'
    
    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna

    def getValor(self):
        return self.__valor

def matriz_random(tamaño):
    matriz = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            num_aleatorio = random.randint(0,5)
            opcion = [0, 0, 0, 0, num_aleatorio]

            fila.append(random.choice(opcion))
    
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(f'{elemento}', end=' ')
        print('')
    print('')

'''def mostrar(matriz, tam):
    for i in range(tam):
        for j in range(tam):
            print(f'{matriz[i][j]}', end=' ')
        print('')'''

def crear_matriz(tamaño):
    matriz = []  
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            fila.append(0)
        matriz.append(fila)
    return matriz


def cargar_lista(lista, matriz, tamaño, pos=0):
    for i in range(tamaño):
        for j in range(tamaño):
            if matriz[i][j] != 0:
                elemento_matriz = Elemento_Matriz(i+1, j+1, matriz[i][j])
                lista.insertar(pos,elemento_matriz)
                pos += 1
    return pos

def suma_matrices(lista):
    matriz_C = crear_matriz(tamaño)
    aux = lista.getCabeza()
    while aux != None:
        dato = aux.getDato()
        fila = dato.getFila()
        columna = dato.getColumna()
        valor = dato.getValor()
        matriz_C[fila-1][columna-1] += valor
        aux = aux.getSiguiente()
    return matriz_C

def suma_matrices_secuencial(lista):
    matriz_C = crear_matriz(tamaño)
    tope_LISTA = lista.getUltimo()
    lista_verdadera = lista.getLista()

    for i in range(tope_LISTA):
        dato = lista_verdadera[i]
        fila = dato.getFila()
        columna = dato.getColumna()
        valor = dato.getValor()
        matriz_C[fila-1][columna-1] += valor
    
    return matriz_C

if __name__ == '__main__':
    tamaño = int(input('Ingrese el tamaño de la matriz: '))
    matriz_A = matriz_random(tamaño)
    matriz_B = matriz_random(tamaño)

    lista = ListaSecuencial(30)
    pos = cargar_lista(lista, matriz_A, tamaño)
    pos = cargar_lista(lista, matriz_B, tamaño, pos)

    print('MATRIZ A')
    mostrar_matriz(matriz_A)
    print('MATRIZ B')
    mostrar_matriz(matriz_B)
    
    matriz_C = suma_matrices_secuencial(lista)
    print('MATRIZ RESULTANTE DE LA SUMA DE LA MATRICES A Y B')
    mostrar_matriz(matriz_C)

    
    
 
    

