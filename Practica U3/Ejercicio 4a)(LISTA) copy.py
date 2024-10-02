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
    
    def __eq__(self, otro):
        return self.__fila == otro.getFila() and self.__columna == otro.getColumna()

    def __str__(self):
        return f'Fila: {self.__fila}\nColumna: {self.__columna}\nValor: {self.__valor}\n'
    
    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna

    def getValor(self):
        return self.__valor
    

def comparar(elemento, otro_elemento):
        return elemento.getFila() == otro_elemento.getFila() and elemento.getColumna() == otro_elemento.getColumna()

def matriz_random(tamaño):
    matriz = ListaEncadenada()
    numeros = [0, 0, 0, 0, 0, 0, 1]
    pos = 0
    for i in range(tamaño):
        for j in range(tamaño):
            if random.choice(numeros) != 0:
                aleatorio = random.randint(1,9)
                elemento = Elemento_Matriz(i+1, j+1, aleatorio)
                matriz.insertar(pos, elemento)
                pos += 1
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

def suma(matrizA, matrizB, tamaño):
    matriz_C = crear_matriz(tamaño)
    listaA = matriz_A.getCabeza()
    listaB = matriz_B.getCabeza()
    while listaA != None:
        while listaB.getSiguiente() != None and listaB.getDato() != listaA.getDato():
            listaB = listaB.getSiguiente()

        if comparar(listaA.getDato(), listaB.getDato()):
            matriz_C[(listaA.getDato().getFila()) - 1][(listaA.getDato().getColumna()) - 1] = listaA.getDato().getValor() + listaB.getDato().getValor()
        else:
            matriz_C[(listaA.getDato().getFila()) - 1][(listaA.getDato().getColumna()) - 1] = listaA.getDato().getValor()

        listaA = listaA.getSiguiente()
    return matriz_C

def suma2(matrizA, matrizB, tamaño):
    matriz_C = crear_matriz(tamaño)
    listaA = matriz_A.getCabeza()
    listaB = matriz_B.getCabeza()
    while listaA != None:
        fila = listaA.getDato().getFila()
        columna = listaA.getDato().getColumna()
        valor = listaA.getDato().getValor()
        matriz_C[fila-1][columna-1] += valor

        listaA = listaA.getSiguiente()

    while listaB != None:
        fila = listaB.getDato().getFila()
        columna = listaB.getDato().getColumna()
        valor = listaB.getDato().getValor()
        matriz_C[fila-1][columna-1] += valor

        listaB = listaB.getSiguiente()

    return matriz_C

'''def suma_matrices(lista):
    matriz_C = crear_matriz(tamaño)
    aux = lista.cabeza()
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
    return matriz_C'''

if __name__ == '__main__':
    tamaño = int(input('Ingrese el tamaño de la matriz: '))
    matriz_A = matriz_random(tamaño)
    matriz_B = matriz_random(tamaño)

    print('*** Matriz A ***\n')
    matriz_A.recorrer()
    print('*** Matriz B ***\n')
    matriz_B.recorrer()
    
    matriz_C = suma2(matriz_A, matriz_B, tamaño)
    print('MATRIZ RESULTANTE DE LA SUMA DE LA MATRICES A Y B')
    mostrar_matriz(matriz_C)