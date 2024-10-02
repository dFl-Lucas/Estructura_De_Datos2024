from colaEncadenada import ColaEncadenada
import random

def varios_cajeros_disp(c1, c2, c3, cola1, cola2, cola3):
    cajeros_disponibles = []
    lista_cajeros = [c1, c2, c3]
    lista_colas = [cola1, cola2, cola3]
    i = 1

    for cajero, cola in zip(lista_cajeros, lista_colas):
        if cajero_disp(cajero) is True and sin_cola(cola) is True:
            cajeros_disponibles.append(i)
        i += 1
    
    return cajeros_disponibles

def cajero_disp(cajero):
    return cajero == 0

def sin_cola(cola):
    return cola.tamañoCola() == 0

def cajeros_ocupados(c1, c2, c3):
    ocupado = True
    lista_cajeros = [c1, c2, c3]
    for cajero in lista_cajeros:
        if cajero_disp(cajero):
            ocupado = False
    return ocupado

def cola_mas_corta(cola1, cola2, cola3):
    mas_corta = 99999
    cola_mas_corta = []
    lista_colas = [cola1, cola2, cola3]
    for cola in lista_colas:
        if len(cola) < mas_corta:
            mas_corta = len(cola)
    for cola in lista_colas:
        if len(cola) == mas_corta:
            cola_mas_corta.append(cola)
    return cola_mas_corta

if __name__ == '__main__':
    frecuencia_clientes = 2
    tiempo_de_simulacion = 120
    reloj = 0
    lista_cajeros = ['cajero1', 'cajero2', 'cajero3'] #lista para elegir aleatoriamente un cajero

    #Disponibilidad de los cajeros
    cajero_1  = 0 #Si es 0 esta descupada y si es numero "x" esta ocupado
    cajero_2  = 0
    cajero_3  = 0 

    #Tiempo de atencion de los cajeros
    tiempo_de_atencion_c1 = 5
    tiempo_de_atencion_c2 = 3
    tiempo_de_atencion_c4 = 4

    #cantidad de clientes atendidos y sin atender
    clientes_atendidos = 0 
    clientes_no_atendidos = 0

    #tiempo de espera acumulado
    total_de_espera = 0 
    tiempo_maximo_espera = 

    #promedio de espera de clientes
    promedio_de_espera_atendidos = 0 #total de espera / en cantidad de tabajos    
    promedio_de_espera_sin_atender = 0

    #cola de los 3 cajeros
    Cola_cajero1= ColaEncadenada()
    Cola_cajero2= ColaEncadenada()
    Cola_cajero3= ColaEncadenada()
    
    while reloj < tiempo_de_simulacion:
        posible_cliente = random.random()

        if posible_cliente <= (1 / frecuencia_clientes):
            cajeros_disp = varios_cajeros_disp(cajero_1, cajero_2, cajero_3, Cola_cajero1, Cola_cajero2, Cola_cajero3)
            if len(cajero_disp) >= 1:
                cajero_aleatorio = random.choice(cajero_disp)
                if cajero_aleatorio == 1:
                    cajero_1 = 5

                elif cajero_aleatorio == 2:
                    cajero_2 = 3

                elif cajero_aleatorio == 3:
                    cajero_3 = 4

            if cajeros_ocupados(cajero_1, cajero_2, cajero_3):
                cola_corta = cola_mas_corta(Cola_cajero1, Cola_cajero2, Cola_cajero3)
                if len(cola_corta) == 1:
                    cola_corta.insertar(reloj)
                elif len(cola_corta) > 1: 
                    cola_elegida = random.choice(cola_corta)
                    cola_elegida.insertar(reloj)
            
            

