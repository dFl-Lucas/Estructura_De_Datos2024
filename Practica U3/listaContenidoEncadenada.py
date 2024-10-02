from nodo import Nodo

class ListaEncadenada:
    __cabeza: Nodo
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0

    def insertar(self, elemento):
        if self.__cant >= 0:
            nuevo_nodo = Nodo(elemento)
            if self.__cant == 0:
                nuevo_nodo.setSiguiente(self.__cabeza)
                self.__cabeza = nuevo_nodo
                self.__cant += 1
            else:
                aux = self.__cabeza
                anterior = aux

                while elemento > aux.getDato() and aux.getSiguiente() != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                
                if elemento < aux.getDato():
                    anterior.setSiguiente(nuevo_nodo)
                    nuevo_nodo.setSiguiente(aux)
                elif elemento >= aux.getDato():
                    aux.setSiguiente(nuevo_nodo)

                self.__cant += 1

    def vacia(self):
        return self.__cant == 0
    
    def suprimir(self, elemento):
        if self.vacia() is False:
                aux = self.__cabeza
                anterior = aux

                while elemento != aux.getDato() and aux.getSiguiente() != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                
                anterior.setSiguiente(aux.getSiguiente())
                self.__cant -= 1
        else:
            print('¡Error! Lista vacia, no se puede eliminar ningun elemento')

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

    def anterior(self, elemento):
        if self.vacia() is False:
            elemento_anterior = None
            if elemento == self.__cabeza.getDato():
                print('¡Error! El elemento ingresado no tiene anterior')
            else:
                aux = self.__cabeza
                anterior = aux
                while aux.getDato() != elemento:
                    anterior = aux
                    aux = aux.getSiguiente()
                elemento_anterior = anterior.getDato()
        else:
            print('¡Error! Lista vacia')
        return elemento_anterior

    def siguiente(self, elemento):
        if self.vacia() is False:
            elemento_siguiente = None
            aux = self.__cabeza
            anterior = aux
            while aux.getDato() != elemento:
                anterior = aux
                aux = aux.getSiguiente()

            if aux.getSiguiente() == None:
                print('¡Error! El elemento ingresado no tiene siguiente')
            else:
                elemento_siguiente = aux.getSiguiente().getDato()
        else:
            print('¡Error! Lista vacia')
        return elemento_siguiente

    def recorrer(self):
        dato = self.__cabeza
        i=0
        while dato is not None:
            print(f'Elemento de la posicion [{i}] --> {dato.getDato()} <--')
            dato = dato.getSiguiente()
            i+=1

if __name__ == '__main__':
    l = ListaEncadenada()
    l.insertar(1)
    l.insertar(3)
    l.insertar(7)
    l.insertar(13)
    l.insertar(5)
    l.insertar(9)
    l.insertar(11)
    l.recorrer()
    #l.suprimir(13)
    #l.recorrer()
    dato = l.anterior(3)
    if dato != None:
        print(f'El elemento anterior a 3 es: {dato}')
    dato2 = l.siguiente(11)
    if dato2 != None:
        print(f'El elemento siguiente a 11 es: {dato2}')

    print(f'El primer elemento de la lista es: {l.primer_elemento()}')
    print(f'El ultimo elemento de la lista es: {l.ultimo_elemento()}')

    print(f'La posicion del elemento buscado es: {l.buscar(7)}')

