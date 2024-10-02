import numpy as np

class ColaSecuencial:
    __max: int
    __pri: int
    __ult: int
    __cant: int
    __items: np.ndarray

    def __init__(self):
        self.__pri = 0
        self.__ult = 0
        self.__cant = 0
        self.__max = 7
        self.__items = np.empty(self.__max, dtype=object)

    def vacia(self):
        return self.__cant == 0
    
    def llena(self):
        return self.__max == self.__cant
    
    def insertar(self, dato):
        if self.llena() is False:
            self.__items[self.__ult] = dato
            self.__ult = (self.__ult + 1) % self.__max
            self.__cant += 1
        else:
            print('!Error¡ Cola llena, no se pudo insertar el elemento')
    
    def suprimir(self):
        aux = None
        if self.vacia():
            print('!Error¡ Cola vacia, no se pudo eliminar ningun elemento')
        else:
            aux = self.__items[self.__pri]
            self.__pri = (self.__pri + 1) % self.__max
            self.__cant -= 1
        return aux
    
    def recorrer(self):
        if self.vacia() is False:
            i = self.__pri
            for j in range(self.__cant):
                print(f'{self.__items[i]}')
                i = (i + 1) % self.__max


if __name__ == '__main__':
    c = ColaSecuencial()

    c.insertar(1)
    c.insertar(2)
    c.insertar(3)
    c.insertar(4)
    c.insertar(5)
    c.insertar(6)
    c.insertar(7)
    print(f'El elemento eliminado es: {c.suprimir()}')
    c.recorrer()

    