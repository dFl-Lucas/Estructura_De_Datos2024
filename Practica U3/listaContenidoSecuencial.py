import numpy as np

class ListaSecuencial:
    __lista: np.ndarray
    __ultimo: int

    def __init__(self, tam):
        self.__lista = np.empty(tam, dtype=int)
        self.__ultimo = 0

    def insertar(self, elemento):
        if (self.__ultimo < self.__lista.size) and (self.__ultimo >= 0):
            if self.__ultimo == 0:
                self.__lista[0] = elemento
                self.__ultimo += 1
            
            elif self.__ultimo > 0:
                if elemento > self.__lista[self.__ultimo - 1]:
                    self.__lista[self.__ultimo] = elemento
                    self.__ultimo += 1
                else:
                    indice = 0
                    insertado = False
                    while indice < self.__ultimo:
                        if elemento < self.__lista[indice]:
                            j = 1
                            n = self.__ultimo - indice
                            for i in range(0, n):
                                self.__lista[self.__ultimo - i] = self.__lista[self.__ultimo - j]
                                j += 1
                            self.__lista[indice] = elemento
                            insertado = True
                            indice = self.__ultimo
                        else:
                            indice += 1
                    if insertado is True:
                        self.__ultimo += 1
        else:
            print('Erorr, lista llena')

    def vacia(self):
        return self.__ultimo == 0

    def suprimir(self, elemento):
        if self.vacia() is False:
            indice = 0
            posicion = None
            while elemento != self.__lista[indice] and indice < self.__ultimo-1:
                indice += 1
            if elemento == self.__lista[indice]:
                for i in range(indice, self.__ultimo-1):
                   self.__lista[i] = self.__lista[i+1]
                self.__ultimo -= 1
                posicion = indice
        else:
            print('¡Error! Lista vacia')
        return posicion
        
    def buscar(self, elemento):
        if self.vacia() is False:
            i = 0
            posicion = None
            while elemento != self.__lista[i] and i < self.__ultimo-1:
                i += 1
            if elemento == self.__lista[i]:
                posicion = i
        else:
            print('¡Error! Lista vacia')
        return posicion
    	
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

    def siguiente(self, elemento):
        if self.vacia() is False:
            dato = None
            if elemento == self.__ultimo - 1:
                print('¡Error! Esa posicion no tiene siguiente')
            else:
                i = 0
                while elemento != self.__lista[i] and i < self.__ultimo-1:
                    i += 1
                if elemento == self.__lista[i]:
                    dato = self.__lista[i+1]
        else:
            print('¡Error! Lista vacia')
        return dato

    def anterior(self, elemento):
        if self.vacia() is False:
            dato = None
            if elemento == self.__lista[0]:
                print('¡Error! Esa posicion no tiene anterior')
            else:
                i = 0
                while elemento != self.__lista[i] and i < self.__ultimo-1:
                    i += 1
                if elemento == self.__lista[i]:
                    dato = self.__lista[i-1]
        else:
            print('¡Error! Lista vacia')
        return dato
    
    def recorrer(self):
        for i in range(0, self.__ultimo):
            print(f'Elemento de la posicion {i} --> {self.__lista[i]} <-- ')
        print('\n')

    def vacia(self):
        return self.__ultimo == 0

if __name__  == '__main__':
    lista = ListaSecuencial(8)
    lista.insertar(9)
    lista.insertar(1)
    lista.insertar(52)
    lista.insertar(5)
    lista.insertar(13)
    lista.insertar(4)
    lista.insertar(17)
    lista.insertar(26)
    lista.recorrer()
    print(f'El elemento 9 que fue suprimido estaba en la posicion: {lista.suprimir(9)}')
    print(f'El elemento anterior a 13 es: {lista.anterior(13)}')
    print(f'El elemento siguiente a 13 es: {lista.siguiente(13)}')
    lista.recorrer()
    '''print(lista.ultimo_elemento())
    print(lista.primer_elemento())
    print(lista.buscar(7))
    print(lista.recuperar(2))
    lista.suprimir(4)
    lista.recorrer()'''