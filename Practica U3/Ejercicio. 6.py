from colaEncadenada import ColaEncadenada
import random

class Trabajo:
    __tiempo_ascociado: int
    __tiempo_de_espera: int
    def __init__(self, num):
        self.__tiempo_ascociado = random.randint(0,10)
        self.__tiempo_de_espera = num

    def cargar_tiempoE(self, dato):
        self.__tiempo_de_espera = dato

    def cargar_tiempoA(self, dato):
        self.__tiempo_ascociado = dato

    def devolver_tiempoE(self):
        return self.__tiempo_de_espera
    
    def devolver_tiempoA(self):
        return self.__tiempo_ascociado

if __name__ == '__main__':
    frecuencia_trabajos = 5
    tiempo_de_simulacion = 60
    tiempo_de_trabajo = 5
    reloj = 0
    impresora  = 0 #Si es 0 esta descupada y si es 5 esta ocupada

    trabajos_impresos = 0 #cuento los trabajos impresos
    total_de_espera = 0 #acumulo los tiempos de espera

    promedio_de_espera = 0 #total de espera / en cantidad de tabajos    

    Cola_impresora = ColaEncadenada()

    while reloj < tiempo_de_simulacion:
        trabajo = random.random()

        if trabajo <= (1 / frecuencia_trabajos):
            nuevo_trabajo = Trabajo(reloj)
            Cola_impresora.insertar(nuevo_trabajo)

        if impresora == 0:
            if Cola_impresora.vacia() is False:
                trabajo_terminado = Cola_impresora.suprimir()
                tiempo_espera = reloj - trabajo_terminado.devolver_tiempoE()
                total_de_espera += tiempo_espera
                tiempo_as = trabajo_terminado.devolver_tiempoA()

                if tiempo_as < tiempo_de_trabajo:
                    print('*** TIEMPO -5 ***')
                    print(f'Tiempo de espera: {tiempo_espera}')
                    print(f'Tiempo asociado: {tiempo_as}\n')
                    trabajos_impresos += 1
                    impresora = tiempo_as

                elif tiempo_as == tiempo_de_trabajo:
                    impresora = tiempo_de_trabajo
                    trabajos_impresos += 1

                else:
                    impresora = tiempo_de_trabajo
                    print('*** TIEMPO +5 ***')
                    print(f'Tiempo de espera: {tiempo_espera}')
                    print(f'Tiempo asociado: {tiempo_as}\n')
                    trabajo_terminado.cargar_tiempoA(tiempo_as - tiempo_de_trabajo)
                    trabajo_terminado.cargar_tiempoE(tiempo_espera)
                    Cola_impresora.insertar(trabajo_terminado)
        reloj += 1

        if impresora > 0:
            impresora -= 1
    
    trabajos_sin_atender = Cola_impresora.tamañoCola()  #trabajos que quedaron en la cola cuando finalizo el tiempo de simulacion
    promedio_de_espera = (total_de_espera / trabajos_impresos)
    print(f'Cantidad de trabajos impresos: {trabajos_impresos}')
    print(f'Cantidad de trabajos sin atender: {trabajos_sin_atender}')
    print(f'El promedio de espera de los trabajos es: {promedio_de_espera}')
        



