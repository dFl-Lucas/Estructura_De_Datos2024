from nodoArbol import Nodo_Arbol


class Arbol_BB:
    __raiz: Nodo_Arbol

    def __init__(self, dato):
        self.__raiz = Nodo_Arbol(dato)

    def vacio(self):
        return self.__raiz == None
    
    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, raiz):
        self.__raiz = raiz
    
    def mostrarRaiz(self):
        return self.__raiz.getElemento()
    
    def insertar(self, nodo, dato):
        if nodo.getDato() == dato:
            print('Error, elemento ya existente')
        else:
            if dato < nodo.getDato():
                if nodo.getIzq() is None:
                    nodo.setIzq(Nodo_Arbol(dato))
                else:
                    self.insertar(nodo.getIzq(), dato)
            else:
                if nodo.getDer() is None:
                    nodo.setDer(Nodo_Arbol(dato))
                else:
                    self.insertar(nodo.getDer(), dato)

    def Grado(self, nodo):
        if nodo is not None:
            if nodo.getIzq() != None and nodo.getDer() != None:
                grado = 2
            elif nodo.getIzq() != None or nodo.getDer() != None:
                grado = 1
            else:
                grado = 0
            return grado

    def Suprimir(self, nodo, dato):
        if nodo is None:
            print('Erorr, elemento inexistente')
        else:
            if dato == nodo.getDato():
                if self.Grado(nodo) == 0: #Se denomina grado de un nodo al número de hijos de dicho nodo.
                    nodo = None
                elif self.Grado(nodo) == 1:
                    if nodo.getIzq() != None:
                        nodo = nodo.getIzq()
                    else:
                        nodo = nodo.getDer()
                elif self.Grado(nodo) == 2:
                    nodo = max(nodo.getIzq())
                    self.Suprimir(max(nodo.getDer()))

    
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

    def nivel(self, nodo, dato):
        if self.vacio():
            print('Erorr, arbol vacio')
        else:
            if dato == nodo.getDato():
                return 1
            else:
                if dato < nodo.getDato():
                    return 1 + self.nivel(nodo.getIzq(), dato)
                else:
                    if dato > nodo.getDato():
                        return 1 + self.nivel(nodo.getDer(), dato)
            
    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            alt_izq = self.altura(nodo.getIzq())
            alt_der = self.altura(nodo.getDer())
            return 1 + max(alt_izq, alt_der)

    
    def Hijo_o_Padre(self, nodo, supuesto_hijo, supuesto_padre):
        if nodo is not None:
            bandera = False
            nodo_sup_padre = self.Buscar(nodo, supuesto_padre)
            if (nodo_sup_padre.getIzq() != None) and  (nodo_sup_padre.getIzq().getDato() == supuesto_hijo):
                bandera = True
            elif (nodo_sup_padre.getDer() != None) and (nodo_sup_padre.getDer().getDato() == supuesto_hijo):
                bandera = True
            return bandera
        else:
            print('Error arbol vacio')
    
    def Hoja(self, nodo, supuesta_hoja):
        if nodo is not None:
            bandera = False
            nodo_sup_hoja = self.Buscar(nodo, supuesta_hoja)
            if nodo_sup_hoja.getIzq() == None and nodo_sup_hoja.getDer() == None:
                bandera = True
            return bandera
        else:
            print('Error arbol vacio')

    def Camino(self, nodo_partida, nodo_llegada, lista):
        if nodo is not None:
            if nodo_llegada == nodo_partida.getDato():
                lista.append(nodo_partida.getDato())
            else:
                if nodo_llegada < nodo_partida.getDato():
                    lista.append(nodo_partida.getDato())
                    self.Camino(nodo_partida.getIzq(), nodo_llegada, lista)
                else:
                    lista.append(nodo_partida.getDato())
                    self.Camino(nodo_partida.getDer(), nodo_llegada, lista)
        else:
            print('Error arbol vacio')

    def Padre_y_Hermano(self, nodo, dato):
        if nodo is None:
            print('Erorr, elemento inexistente')
            return None  #retornamos estas llamadas recursivas porque si no se pierde el nodo encontrado
        else:
            #anterior = nodo
            if dato == nodo.getDato():
                return nodo
            else:
                if dato < nodo.getDato():
                    if dato == nodo.getIzq().getDato():
                        return nodo
                    else:
                        return self.Padre_y_Hermano(nodo.getIzq(), dato) #retornamos estas llamadas recursivas porque si no se pierde el nodo encontrado
                else:
                    if dato > nodo.getDato():
                        if dato == nodo.getDer().getDato():
                            return nodo
                        else:
                            return self.Padre_y_Hermano(nodo.getDer(), dato)
                       
    def Sucesor(self, raiz, dato):
        nodo = self.Buscar(raiz, dato)
        if nodo is not None: #Si encuentro el nodo hago

            #Si tiene hijo derecho hace esto
            if nodo.getDer() != None:
                nodo2= nodo.getDer()
                while nodo2.getIzq() != None:
                    nodo2 = nodo2.getIzq()
                return nodo2
            
            else:
                #Si no tiene hijo derecho hace esto
                padre = self.Padre_y_Hermano(raiz, nodo.getDato())
                while padre != None and nodo is padre.getDer():
                    nodo = padre
                    padre = self.Padre_y_Hermano(raiz, padre.getDato())
                return padre
        else:
            print('Nodo no encontrado')
       

    


if __name__ == '__main__':
    arbol = Arbol_BB(50)
    raiz = arbol.getRaiz()

    arbol.insertar(raiz,59)
    arbol.insertar(raiz,37)
    arbol.insertar(raiz,33)
    arbol.insertar(raiz,62)
    arbol.insertar(raiz,55)
    arbol.insertar(raiz,42)
    arbol.insertar(raiz,60)
    arbol.insertar(raiz,27)
    arbol.insertar(raiz,31)
    arbol.insertar(raiz,40)
    arbol.insertar(raiz,57)
    arbol.insertar(raiz,56)
    arbol.insertar(raiz,65)
    arbol.insertar(raiz,45)
    arbol.insertar(raiz,43)
    

    arbol.In_orden(raiz)
    print('')
    print(f'La altura del arbol es: {arbol.altura(raiz)}')


    nodo = 33
    # nodo = int(input('Ingrese el nodo para buscar su nivel en el arbol: '))
    print(f'El nivel del nodo [{nodo}] es: {arbol.nivel(raiz, nodo)}')
    print('')

    nodo_a_buscar = 33
    #nodo_a_buscar = int(input('Ingrese el nodo a buscar: '))
    elemento_buscado = arbol.Buscar(raiz, nodo_a_buscar)
    if elemento_buscado != None:
        print(f'Dato del nodo: [{elemento_buscado.getDato()}]')
        if elemento_buscado.getIzq() != None:
            print(f'Nodo hijo izquierdo: [{elemento_buscado.getIzq().getDato()}]')
        else:
            print('Nodo hijo izquierdo: [None]')
        if elemento_buscado.getDer() != None:
            print(f'Nodo hijo derecho: [{elemento_buscado.getDer().getDato()}]')
        else:
            print('Nodo hijo derecho: [None]')
    else: 
        print('Elemento no encontrado')

    supuesto_padre = 42
    #supuesto_padre = int(input('Ingrese el nodo del padre a consultar: '))
    supuesto_hijo = 40
    #supuesto_hijo =  int(input('Ingrese el nodo del hijo a consultar: '))
    print(f'Es hijo {supuesto_hijo} de {supuesto_padre} ? -> Respuesta: {arbol.Hijo_o_Padre(raiz, supuesto_hijo, supuesto_padre)}')

    supuesto_padre2 = 59
    #supuesto_padre = int(input('Ingrese el nodo del padre a consultar: '))
    supuesto_hijo2 = 55
    #supuesto_hijo =  int(input('Ingrese el nodo del hijo a consultar: '))
    print(f'Es padre {supuesto_padre2} de {supuesto_hijo2} ? -> Respuesta: {arbol.Hijo_o_Padre(raiz, supuesto_hijo2, supuesto_padre2)}')

    supuesto_hoja = 60
    #supuesto_hoja =  int(input('Ingrese el nodo a consultar si es hoja del arbol: '))
    print(f'Es una hoja {supuesto_hoja} del arbol ? Respuesta: {arbol.Hoja(raiz, supuesto_hoja)}')

    nodo_partida = 50
    #nodo_partida = int(input('Ingrese el nodo de inicio del camino: '))
    nodo_llegada = 43
    #nodo_llegada = int(input('Ingrese el nodo de llegada del camino: '))

    camino = []
    nodo_partida = arbol.Buscar(raiz, nodo_partida)
    arbol.Camino(nodo_partida, nodo_llegada, camino)
    print(camino)

    '''nodo_a_eliminar = arbol.Buscar(raiz, 4)
    arbol.Suprimir(nodo_a_eliminar, 4)
    arbol.In_orden(raiz)'''

    print(f'Cantidad de nodos del arbol: {arbol.Contar_Post_orden(raiz)}')

    num = 31
    #num= int(input('Ingrese el nodo que desea saber su padre y hermanos: '))
    padre = arbol.Padre_y_Hermano(raiz, num)
    if (padre.getIzq() != None) and (padre.getIzq().getDato() == num):
        if padre.getDer() != None:
            hermano = padre.getDer().getDato()
        else:
            hermano = None
    else:
        if padre.getIzq() != None:
            hermano = padre.getIzq().getDato()
        else:
            hermano = None

    print(f'Nodo padre de {num} es: {padre.getDato()}\nNodo hermano de {num} es: {hermano}')

    sucesor = 42
    #sucesor = int(input('Ingrese el nodo del cual desea saber el sucesor: '))
    print(f'El sucesor de {sucesor} es: {arbol.Sucesor(raiz, sucesor).getDato()}')

