from listaEncadenada import ListaEncadenada
import random

class Polinomio:
    __base: int
    __exponente: int

    def __init__(self, base, exp):
        self.__base = base
        self.__exponente = exp

    def __str__(self):
        return f'Base: {self.__base}  \tExponente: {self.__exponente}'

    def getBase(self):
        return self.__base

    def getExponente(self):
        return self.__exponente 
    
def crear_polinomio():
    poli = ListaEncadenada()
    terminos = random.randint(1,5)
    for i in range(terminos):
        #posibles_bases = list(range(-20, -1) + list(range(1, 20)))
        #otra_base = random.choice(posibles_bases)
        base = random.randint(1,10)
        nuevo_polinomio = Polinomio(base, terminos)
        poli.insertar(i, nuevo_polinomio)
        terminos -= 1
    if random.randint(1,3) == 1:
        base = random.randint(1,10)
        nuevo_polinomio = Polinomio(base, 0)
        poli.insertar(i+1, nuevo_polinomio)
    return poli

def sumaP(A, B):
    poliC = ListaEncadenada()

    if A.getCantidad() >= B.getCantidad():
        poliA = A.getCabeza()
        poliB = B.getCabeza()
    else:
        poliA = B.getCabeza()
        poliB = A.getCabeza()

    i = 0
    while poliA != None and poliB != None:
        if poliA.getDato().getExponente() == poliB.getDato().getExponente():
            base = poliA.getDato().getBase() +  poliB.getDato().getBase()
            nuevo_polinomio = Polinomio(base, poliA.getDato().getExponente())
            poliC.insertar(i, nuevo_polinomio)
            i += 1
            poliB = poliB.getSiguiente()
        else:
            base = poliA.getDato().getBase()
            nuevo_polinomio = Polinomio(base, poliA.getDato().getExponente())
            poliC.insertar(i, nuevo_polinomio)
            i += 1
        poliA = poliA.getSiguiente()
    
    if poliB != None:
        #poliB = poliB.getSiguiente()
        nuevo_polinomio = Polinomio(poliB.getDato().getBase(), poliB.getDato().getExponente())
        poliC.insertar(i, nuevo_polinomio)
    elif poliA != None:
        #poliB = poliB.getSiguiente()
        nuevo_polinomio = Polinomio(poliA.getDato().getBase(), poliA.getDato().getExponente())
        poliC.insertar(i, nuevo_polinomio)
    return poliC

def restaP(A, B):
    poliC = ListaEncadenada()
    poliA = A.getCabeza()
    poliB = B.getCabeza()

    i = 0
    while poliA != None and poliB != None:
        if poliB.getDato().getExponente() > poliA.getDato().getExponente():
            nuevo_polinomio = Polinomio(-poliB.getDato().getBase(), poliB.getDato().getExponente())
            poliC.insertar(i, nuevo_polinomio)
            i += 1
            poliB = poliB.getSiguiente()
        else: 
            if poliA.getDato().getExponente() == poliB.getDato().getExponente():
                base = poliA.getDato().getBase() -  poliB.getDato().getBase()
                nuevo_polinomio = Polinomio(base, poliA.getDato().getExponente())
                poliC.insertar(i, nuevo_polinomio)
                i += 1
                poliB = poliB.getSiguiente()
            else:
                base = poliA.getDato().getBase()
                nuevo_polinomio = Polinomio(base, poliA.getDato().getExponente())
                poliC.insertar(i, nuevo_polinomio)
                i += 1
            poliA = poliA.getSiguiente()
    
    if poliB != None:
        #poliB = poliB.getSiguiente()
        nuevo_polinomio = Polinomio(-poliB.getDato().getBase(), poliB.getDato().getExponente())
        poliC.insertar(i, nuevo_polinomio)
    elif poliA != None:
        #poliB = poliB.getSiguiente()
        nuevo_polinomio = Polinomio(poliA.getDato().getBase(), poliA.getDato().getExponente())
        poliC.insertar(i, nuevo_polinomio)
    return poliC
    
def multiplicacion_escalar(A, escalar):
    poliC = ListaEncadenada()
    poliA = A.getCabeza()
    i = 0
    while poliA != None:
        base = poliA.getDato().getBase() * escalar
        exponente = poliA.getDato().getExponente()
        nuevo_polinomio = Polinomio(base, exponente)
        poliC.insertar(i, nuevo_polinomio)
        poliA = poliA.getSiguiente()
    return poliC


if __name__ == '__main__':
    polinomio_1 = crear_polinomio() 
    polinomio_2 = crear_polinomio()
    print('** Polinomio A **')
    polinomio_1.recorrer()
    print('')
    print('** Polinomio B **')
    polinomio_2.recorrer()
    print('')

    polinomio_sumado = sumaP(polinomio_1, polinomio_2)
    print('Resultado de la suma de A y B')
    polinomio_sumado.recorrer()

    polinomio_restado = restaP(polinomio_1, polinomio_2)
    print('Resultado de la resta de A y B')
    polinomio_restado.recorrer()

    k = 3
    polinomio_multiplicado = multiplicacion_escalar(polinomio_1, k)
    print(f'El resultado de multplicar A por el escalar {k}')
    polinomio_multiplicado.recorrer()