class Nodo_Huffman:
    __elemento: str
    __frecuencia: int
    __izquierda: object 
    __derecha: object

    def __init__(self, dato, frecuencia):
        self.__elemento = dato
        self.__frecuencia = frecuencia
        self.__izquierda = None
        self.__derecha = None

    def getDato(self):
        return self.__elemento
    
    def getFrec(self):
        return self.__frecuencia
    
    def getIzq(self):
        return self.__izquierda
    
    def setIzq(self,dato):
        self.__izquierda = dato

    def getDer(self):
        return self.__derecha
    
    def setDer(self,dato):
        self.__derecha = dato

    def __str__(self):
        return f'Letra: {self.__elemento} - Frecuencia: {self.__frecuencia}'

class Arbol_BB:
    __raiz: Nodo_Huffman

    def __init__(self, letra, frecuencia):
        self.__raiz = Nodo_Huffman(letra, frecuencia)

    def vacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, raiz):
        self.__raiz = raiz
    
    def mostrarRaiz(self):
        return self.__raiz.getElemento()
    
    def insertar(self, nodo, dato, frecuencia):
        if nodo.getDato() == dato:
            print('Error, elemento ya existente')
        else:
            if dato < nodo.getDato():
                if nodo.getIzq() is None:
                    nodo.setIzq(Nodo_Huffman(dato, frecuencia))
                else:
                    self.insertar(nodo.getIzq(), dato, frecuencia)
            else:
                if nodo.getDer() is None:
                    nodo.setDer(Nodo_Huffman(dato, frecuencia))
                else:
                    self.insertar(nodo.getDer(), dato, frecuencia)

    def cargar(self, raiz, hijo):
        if raiz.getIzq() is None:
            raiz.setIzq(hijo)
        else:
            raiz.setDer(hijo)

    def Buscar(self, nodo, dato):
        if nodo is None:
            print('Erorr, elemento inexistente')
            return None  #retornamos estas llamadas recursivas porque si no se pierde el nodo encontrado
        else:
            if dato == nodo.getDato():
                return nodo
            else:
                if dato < nodo.getDato():
                    return self.Buscar(nodo.getIzq(), dato) #retornamos estas llamadas recursivas porque si no se pierde el nodo encontrado
                else:
                    if dato > nodo.getDato():
                        return self.Buscar(nodo.getDer(), dato)  #retornamos estas llamadas recursivas porque si no se pierde el nodo encontrado
    
    def Pre_orden(self, nodo):
        if nodo is not None:
            print(nodo.getDato(), end=', ')
            self.Pre_orden(nodo.getIzq())
            self.Pre_orden(nodo.getDer())

    def In_orden(self, nodo):
        if nodo is not None:
            self.In_orden(nodo.getIzq())
            print(nodo.getDato(), end=', ')
            self.In_orden(nodo.getDer())
    
    def Post_orden(self, nodo):
        if nodo is not None:
            self.Post_orden(nodo.getIzq())
            self.Post_orden(nodo.getDer())
            print(nodo.getDato(), end=', ')

    def Contar_Post_orden(self, nodo):
        if nodo is not None:
            izq = self.Contar_Post_orden(nodo.getIzq())
            der = self.Contar_Post_orden(nodo.getDer())
            raiz = 1
            return izq + der + raiz
        return 0
