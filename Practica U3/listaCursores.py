import numpy as np

class CeldaCursor:
    __item: object
    __enlace: int

    def __init__(self, elemento, enlace):
        self.__item = elemento
        self.__enlace = enlace

    def setSiguiente(self, siguiente):
        self.__enlace = siguiente

    def getSiguiente(self):
        return self.__enlace
    
    def getDato(self):
        return self.__item
    
    def setDato(self, dato):
        self.__item = dato

class ListaCursores:
    __cabeza: int
    __cantidad: int
    __disponible: int
    __arreglo: np.ndarray
    __maximo: int

    def __init__(self, tamaño):
        self.__cabeza = None
        self.__cantidad = 0
        self.__disponible = 0
        self.__arreglo = np.empty(tamaño, dtype=CeldaCursor)
        self.__maximo = tamaño  
        for i in range(tamaño):
            self.__arreglo[i] = CeldaCursor()
        for j in range(tamaño-1):
            self.__arreglo[j].setSiguiente(j+1)

    def insetar(self, elemento):
