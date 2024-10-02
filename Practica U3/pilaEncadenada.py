from nodo import Nodo

class PilaEncadenada:
    __tope: Nodo
    __contador: int

    def __init__(self):
        self.__tope = None
        self.__contador = 0

    def vacia(self):
        return self.__contador == 0
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.setSiguiente(self.__tope)
        self.__tope = nuevo_nodo
        self.__contador += 1

    def suprimir(self):
        elemento = None
        if self.vacia() is False:
            elemento = self.__tope.getDato()
            self.__tope = self.__tope.getSiguiente()
            self.__contador -= 1
        else:
            print('¡Error! Pila vacia, no se pudo eliminar ningun elemento')
        return elemento
    
    def recorrer(self):
        dato = self.__tope
        while dato is not None:
            print(dato.getDato())
            dato = dato.getSiguiente()

if __name__ == '__main__':
    p = PilaEncadenada()
    p.insertar(5)
    p.insertar(4)
    p.insertar(3)
    p.insertar(2)
    p.insertar(1)
    p.recorrer()
    print(f'El elemento eliminado es: {p.suprimir()}')
    print(f'El elemento eliminado es: {p.suprimir()}')
    p.recorrer()
