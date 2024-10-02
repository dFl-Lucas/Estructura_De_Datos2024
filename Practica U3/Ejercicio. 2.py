from pilaEncadenada import PilaEncadenada

if __name__ == '__main__':
    p = PilaEncadenada()
    band = False
    try:
        numero = int(input('Ingrese un numero decimal: '))
        while numero >= 1:
            modulo = numero % 2
            numero = numero // 2
            p.insertar(modulo)
        band = True
    except:
        print('¡Error!, debe ingresar un numero entero')
    
    if band is True:
        print(f'El numero en binario es: ', end='')
        while p.vacia() is False:
            print(f'{p.suprimir()}', end='')
    


