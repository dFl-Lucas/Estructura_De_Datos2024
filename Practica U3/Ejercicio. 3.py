from pilaEncadenada import PilaEncadenada

if __name__ == '__main__':
    p = PilaEncadenada()

    try:
        numero = int(input('Ingrese un numero entero: '))
        if numero == 0:
            p.insertar(1)
        else: 
            while numero > 0:
                p.insertar(numero)
                numero -= 1
        band = True
    except:
        print('¡Error!, debe ingresar un numero entero')

    print('El factorial del numero ingresado es: ', end='')

    res = 1
    while p.vacia() is False:
        res *= p.suprimir()
    
    print(res)