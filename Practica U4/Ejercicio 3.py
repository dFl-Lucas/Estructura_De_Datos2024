from listaContenidoEncadenada import ListaEncadenada
from Arbol_ABB_EJ3 import Arbol_BB
from collections import Counter

def contar(cadena):
    letras = []
    for char in cadena:
        if char.isalpha(): # Verificamos si el carácter es una letra
            letras.append(char.upper()) 
        
    contador = Counter(letras)
    return contador

if __name__ == '__main__':
    lista_arboles = ListaEncadenada()

    cadena = 'hola pa todo bien?'
    letras_contadas = contar(cadena)
    for letra, cantidad in letras_contadas.items():
        print(f"'{letra}' aparece {cantidad} veces")
        arbol = Arbol_BB(letra, cantidad)
        lista_arboles.insertarGPT(arbol)
    
    '''arbol1 = Arbol_BB('I', 15)
    lista_arboles.insertarGPT(arbol1)

    arbol2 = Arbol_BB('G', 6)
    lista_arboles.insertarGPT(arbol2)

    arbol3 = Arbol_BB('C', 7)
    lista_arboles.insertarGPT(arbol3)

    arbol4 = Arbol_BB('D', 12)
    lista_arboles.insertarGPT(arbol4)

    arbol5 = Arbol_BB('E', 25)
    lista_arboles.insertarGPT(arbol5)

    arbol6 = Arbol_BB('F', 4)
    lista_arboles.insertarGPT(arbol6)

    arbol7 = Arbol_BB('B', 6)
    lista_arboles.insertarGPT(arbol7)

    arbol8 = Arbol_BB('H', 1)
    lista_arboles.insertarGPT(arbol8)

    arbol9 = Arbol_BB('A', 15)
    lista_arboles.insertarGPT(arbol9)'''

    
    tamaño_lista = lista_arboles.getCant()
    i = 1
    while tamaño_lista >= 2:
        izq = lista_arboles.Suprimir_cabeza().getRaiz()
        letraIzq = izq.getDato()
        frec_izq = izq.getFrec()

        der = lista_arboles.Suprimir_cabeza().getRaiz()
        letraDer = der.getDato()
        frec_der = der.getFrec()

        arbol_doble1 = Arbol_BB(letraIzq+letraDer, frec_izq+frec_der)
        raiz_arb_dob = arbol_doble1.getRaiz()

        letra = izq.getDato()
        frec = izq.getFrec()

        letra2 = der.getDato()
        frec2 = der.getFrec()

        arbol_doble1.cargar(raiz_arb_dob, izq)
        arbol_doble1.cargar(raiz_arb_dob, der)

        lista_arboles.insertarGPT(arbol_doble1)

        tamaño_lista = lista_arboles.getCant()
        i+=1
    
    lista_arboles.recorrer()
    arbol_doble1.In_orden(raiz_arb_dob)

    

    