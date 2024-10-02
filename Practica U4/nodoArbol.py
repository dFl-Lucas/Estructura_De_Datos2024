class Nodo_Arbol:
    __elemento: object
    __izquierda: object 
    __derecha: object

    def __init__(self, dato):
        self.__elemento = dato
        self.__izquierda = None
        self.__derecha = None

    def getDato(self):
        return self.__elemento
    
    def getIzq(self):
        return self.__izquierda
    
    def setIzq(self,dato):
        self.__izquierda = dato

    def getDer(self):
        return self.__derecha
    
    def setDer(self,dato):
        self.__derecha = dato