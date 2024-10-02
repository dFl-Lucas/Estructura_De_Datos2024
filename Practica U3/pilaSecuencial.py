import numpy as np

class PilaSecuencial:
    __items: np.ndarray
    __tope: int
    __tamaño: int
    
    def __init__(self):
        self.__tope = -1
        self.__tamaño = 3
        self.__items = np.empty(self.__tamaño, dtype=object)
        
    def lleno(self):
        return self.__tamaño == (self.__tope + 1)
        
    def vacia(self):
        return self.__tope == -1
        
    def insertar(self, dato):
        if self.lleno() is False:
            self.__tope += 1
            self.__items[self.__tope] = dato
        else:
            print('¡Error! Espacio Insuficiente \nPila completamente cargada')
            
    def suprimir(self):
        elemento = None
        if self.vacia() is False:
            elemento = self.__items[self.__tope]
            self.__items[self.__tope] = None
            self.__tope -= 1
        else:
            print('¡Error! Pila vacia, no se pudo eliminar ningun elemento')
        return elemento 

    def mostrar(self):
        for item in self.__items[::-1]:
            print(item) 

if __name__ == '__main__':
    p = PilaSecuencial()
    p.insertar(3)  
    p.insertar(2)
    p.insertar(1)
    p.insertar(0)
    print('Pila sin borrar')
    p.mostrar() 
    print(f'El elemento borrado es {p.suprimir()}')
    p.mostrar()
