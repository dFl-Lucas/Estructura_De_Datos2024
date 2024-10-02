import numpy as np

class ListaSecuencial:
    __lista: np.ndarray
    __ultimo: int

    def __init__(self, tam):
        self.__lista = np.empty(tam, dtype=object)
        self.__ultimo = 0

    def insertar(self, pos, elemento):
        if (self.__ultimo < self.__lista.size) and (self.__ultimo >= 0):

            if (self.__ultimo > 0) and (0 <= pos <= self.__ultimo):
                if pos < self.__ultimo:
                    n = self.__ultimo - pos
                    j = 1
                    for i in range(0, n):
                        self.__lista[self.__ultimo - i] = self.__lista[self.__ultimo - j]
                        j += 1
                    self.__lista[pos] = elemento
                    self.__ultimo += 1
                else:
                    self.__lista[pos] = elemento
                    self.__ultimo += 1

            elif (self.__ultimo > 0) and (pos == self.__ultimo + 1):
                self.__lista[pos] = elemento
                self.__ultimo += 1

            elif (self.__ultimo == 0) and (pos == 0):
                self.__lista[pos] = elemento
                self.__ultimo += 1
        else:
            print('Erorr, lista llena')

    def vacia(self):
        return self.__ultimo == 0

    def suprimir(self, pos):
        if self.__ultimo > 0 and (0 <= pos < self.__ultimo):
            print(f'Elemento suprimido: -> {self.__lista[pos]} <-')
            self.__lista[pos] = None
        else:
            print('¡Error! Posicion incorrecta')

    def recuperar(self, pos):
        if self.__ultimo > 0 and (0 <= pos < self.__ultimo):
            return self.__lista[pos]
        else:
            print('¡Error! Posicion incorrecta')

    def buscar(self, elemento):
        if self.__ultimo > 0:
            i = 0
            while elemento != self.__lista[i]:
                i += 1
            if elemento == self.__lista[i]:
                p = i
        else:
            print('¡Error! Lista vacia')
        return p
    	
    def primer_elemento(self):
        if self.vacia() is False:
            return self.__lista[0]
        else:
            print('¡Error! Lista vacia')

    def ultimo_elemento(self):
        if self.vacia() is False:
            return self.__lista[self.__ultimo - 1]
        else:
            print('¡Error! Lista vacia')

    def siguiente(self, pos):
        if (0 <= pos < self.__ultimo):
            elemento = None
            if pos == self.__ultimo - 1:
                print('¡Error! Esa posicion no tiene siguiente')
            else:
                elemento = self.__lista[pos]
        else:
            print('¡Error! Posicion incorrecta')
        return elemento

    def anterior(self, pos):
        if (0 <= pos <= self.__ultimo):
            elemento = None
            if pos == 0:
                print('¡Error! Esa posicion no tiene anterior')
            else:
                elemento = self.__lista[pos]
        else:
            print('¡Error! Posicion incorrecta')
        return elemento

    def recorrer(self):
        for i in range(self.__ultimo):
            print(f'Elemento de la posicion {i} --> {self.__lista[i]} <-- ')
        print('\n')

    def vacia(self):
        return self.__ultimo == 0
    
    def getUltimo(self):
        return self.__ultimo
    
    def getLista(self):
        return self.__lista

'''if __name__  == '__main__':
    lista = ListaSecuencial(5)
    lista.insertar(0, 1)
    lista.insertar(1, 3)
    lista.insertar(2, 5)
    lista.insertar(3, 7)
    lista.insertar(4, 9)
    lista.recorrer()
    print(lista.anterior(1))
    print(lista.siguiente(2))
    print(lista.ultimo_elemento())
    print(lista.primer_elemento())
    print(lista.buscar(7))
    print(lista.recuperar(2))
    lista.suprimir(4)
    lista.recorrer()'''