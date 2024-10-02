from nodo import Nodo

class ListaEncadenada:
    __cabeza: Nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def insertar(self, pos, elemento):
            if (0 <= pos <= self.__cant):
                nuevo_nodo = Nodo(elemento)
                if pos == 0:
                    nuevo_nodo.setSiguiente(self.__cabeza)
                    self.__cabeza = nuevo_nodo
                    self.__cant += 1
                else:
                    aux = self.__cabeza
                    for i in range(0, (pos - 1)):
                        aux= aux.getSiguiente()

                    dir_sig = aux.getSiguiente()
                    nuevo_nodo.setSiguiente(dir_sig)
                    aux.setSiguiente(nuevo_nodo)
                    self.__cant += 1
            else:
                print('¡Error! Posicion incorrecta')

    def vacia(self):
        return self.__cant == 0
    
    def suprimir(self, pos):
        if self.vacia() is False:
            if (0 <= pos < self.__cant):
                indice = 0
                aux = self.__cabeza
                anterior = aux
                while indice < pos:
                    anterior = aux
                    aux = aux.getSiguiente()
                    indice += 1
                anterior.setSiguiente(aux.getSiguiente())
                self.__cant -= 1
            else:
                print('¡Error! Posicion incorrecta')
        else:
            print('¡Error! Lista vacia, no se puede recuperar ningun elemento')
    
    def recuperar(self, pos):
        if self.vacia() is False:
            if (0 <= pos < self.__cant):
                indice = 0
                cab = self.__cabeza
                while indice < pos:
                    cab = cab.getSiguiente()
                    indice += 1
                elemento = cab.getDato()
                return elemento
            else:
                print('¡Error! Posicion incorrecta')

        else:
            print('¡Error! Lista vacia, no se puede recuperar ningun elemento')

    def buscar(self, elemento):
        if self.vacia() is False:
            encontrado = None
            dato = self.__cabeza
            otro_elemento = dato.getDato()
            posicion = 0
            while dato is not None and otro_elemento != elemento:
                posicion += 1
                dato = dato.getSiguiente()
                otro_elemento = dato.getDato()

            if elemento == otro_elemento:
                encontrado = posicion
        else:
            print('¡Error! Lista vacia, no se puede buscar ningun elemento')
        return encontrado

    def primer_elemento(self):
        return self.__cabeza.getDato()

    def ultimo_elemento(self):
        dato = self.__cabeza
        aux = dato
        while dato is not None:
            aux = dato
            dato = dato.getSiguiente()
        return aux.getDato()

    def anterior(self, pos):
        anterior = None
        if (0 <= pos <= self.__cant - 1):
            if pos == 0:
                print('¡Error! La posicion ingresada no tiene anterior')
            else:
                i = 0
                aux = self.__cabeza
                while i < pos - 1:
                    aux = aux.getSiguiente()
                    i += 1
                anterior = aux.getDato()
        else:
            print('¡Error! Posicion incorrecta')
        return anterior

    def siguiente(self, pos):
            siguiente = None
            if (0 <= pos < self.__cant):
                if pos == self.__cant - 1:
                    print('¡Error! La posicion ingresada no tiene siguiente')
                else:
                    i = 0
                    aux = self.__cabeza
                    while i < pos + 1:
                        aux = aux.getSiguiente()
                        i += 1
                    siguiente = aux.getDato()
            else:
                print('¡Error! Posicion incorrecta')
            return siguiente

    def recorrer(self):
        dato = self.__cabeza
        while dato is not None:
            print(dato.getDato())
            dato = dato.getSiguiente()

    def getCabeza(self):
        return self.__cabeza

    def getCantidad(self):
        return self.__cant

if __name__ == '__main__':
    l = ListaEncadenada()
    l.insertar(0, 1)
    l.insertar(1, 3)
    l.insertar(2, 5)
    l.insertar(3, 7)
    l.insertar(4, 9)
    l.insertar(5, 11)
    #l.insertar(2, 33)
    l.recorrer()
    print('anterior:')
    print(l.anterior(2))
    print('siguiente')
    print(l.siguiente(2))
    print('ultimo')
    print(l.ultimo_elemento())
    print('primero')
    print(l.primer_elemento())
    print('posicion del elemento buscado')
    print(l.buscar(5))
    print('elemento recuperado de la posicion')
    print(l.recuperar(1))
    l.suprimir(4)
    print('despues de suprimir')
    l.recorrer()
