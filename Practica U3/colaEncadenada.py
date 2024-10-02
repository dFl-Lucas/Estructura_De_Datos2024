from nodo import Nodo

class ColaEncadenada:
    __cant: int
    __pri: Nodo
    __ult: Nodo

    def __init__(self):
        self.__cant = 0
        self.__pri = None
        self.__ult = None
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.__ult == None:
            self.__pri = nuevo_nodo
        else:
            self.__ult.setSiguiente(nuevo_nodo)
        self.__ult = nuevo_nodo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print('¡Error! Cola vacia, no se puedo eliminar ningun elemento')
        else:
            dato = self.__pri.getDato()
            self.__pri = self.__pri.getSiguiente()
            self.__cant -= 1

            if self.__pri == None:
                self.__ult = None
        return dato
    
    def recorrer(self):
        dato = self.__pri
        while dato != None:
            print(f'{dato.getDato()}')
            dato = dato.getSiguiente()

    def tamañoCola(self):
        return self.__cant

if __name__ == '__main__':
    p = ColaEncadenada()
    p.insertar(5)
    p.insertar(4)
    p.insertar(3)
    p.insertar(2)
    p.insertar(1)
    p.recorrer()
    print(f'El elemento eliminado es: {p.suprimir()}')
    print(f'El elemento eliminado es: {p.suprimir()}')
    p.recorrer()