from pilaSecuencial import PilaSecuencial

def mostrar_estados(pila1, pila2, pila3):
    print('*** Estados de las pilas ***')
    print('Pila N° 1: ')
    pila1.recorrer()
    print('Pila N° 2: ')
    pila2.recorrer()
    print('Pila N° 3: ')
    pila3.recorrer()

def verificar_movimiento(origen, destino):
    se_puede = False
    dato_origen = origen.suprimir()

    if destino.vacia() is True:
        destino.insertar(dato_origen)
        se_puede = True
    else:
        dato_destino = destino.suprimir()
        destino.insertar(dato_destino)
        
        if dato_origen < dato_destino:
            destino.insertar(dato_origen)
            se_puede = True
        else:
            origen.insertar(dato_origen)
            #destino.insertar(dato_destino)
     
    return se_puede


def pedir_movimiento(pila1, pila2, pila3):
    mov_valido = False
    opciones_pilas = [1,2,3]

    pila_origen = int(input('Ingrese la pila origen [1,2,3]: '))
    opciones_pilas.remove(pila_origen)
    pila_destino = int(input(f'Ingrese la pila destino {opciones_pilas}: '))

    if (pila_origen in [1,2,3]) & (pila_destino in opciones_pilas):
        if pila_origen == 1:
            if pila_destino == 2:
                mov_valido = verificar_movimiento(pila1, pila2)
            elif pila_destino == 3:
                mov_valido = verificar_movimiento(pila1, pila3)

        elif pila_origen == 2:
            if pila_destino == 1:
                mov_valido = verificar_movimiento(pila2, pila1)
            elif pila_destino == 3:
                mov_valido = verificar_movimiento(pila2, pila3)

        elif pila_origen == 3:
            if pila_destino == 1:
                mov_valido = verificar_movimiento(pila3, pila1)
            elif pila_destino == 2:
                mov_valido = verificar_movimiento(pila3, pila2)
    else:
        print('¡Error! Pila origen o pila destino incorrecta')
    
    if mov_valido is False:
        print('¡Error! Movimiento invalido')

    return mov_valido



if __name__ == '__main__':
    pila_1 = PilaSecuencial()
    pila_2 = PilaSecuencial()
    pila_3 = PilaSecuencial()

    num_discos = int(input('Ingrese el numero de discos [max 7]: '))
    n = num_discos
    while n> 0:
        pila_1.insertar(n)
        n -= 1

    mostrar_estados(pila_1, pila_2, pila_3)
    contador_movimiento = 0
    while (pila_1.vacia() is False) or (pila_2.vacia() is False):
        if pedir_movimiento(pila_1, pila_2, pila_3) is True:
            print('Movimiento realizado')
            contador_movimiento += 1
        mostrar_estados(pila_1, pila_2, pila_3)
    
    print(f'Juego completado con {contador_movimiento} movimientos realizados')
    print(f'El juego se podia completar realizando un minimo de {(2**num_discos) - 1} movimientos')