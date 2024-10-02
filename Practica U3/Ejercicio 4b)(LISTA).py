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


def crear_matriz(tamaño):
    matriz = []  
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            fila.append(0)
        matriz.append(fila)
    return matriz

def suma(A, B, tamaño):
    matriz_C = crear_matriz(tamaño)
    for i in range(tamaño):
        for j in range(tamaño):
            if A[i][j] != 0:
                matriz_C[i][j] += A[i][j]
            if B[i][j] != 0:
                matriz_C[i][j] += B[i][j]
    return matriz_C

if __name__ == '__main__':
    tamaño = int(input('Ingrese el tamaño de la matriz: '))
    matriz_A = matriz_random(tamaño)
    matriz_B = matriz_random(tamaño)

    print('MATRIZ A')
    mostrar_matriz(matriz_A)
    print('MATRIZ B')
    mostrar_matriz(matriz_B)

    matriz_C = suma(matriz_A, matriz_B, tamaño)

    print('MATRIZ RESULTANTE DE LA SUMA DE LA MATRICES A Y B')
    mostrar_matriz(matriz_C)