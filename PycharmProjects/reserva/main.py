from controller import reservas_controller
from datetime import datetime
from models.Restaurante import *
control = reservas_controller
restaurante = Restaurante(datetime.strptime('12:00','%H:%M').time(),datetime.strptime('23:00','%H:%M').time(),1,10,4)

while True:
    try:
        print('==========Bienvenido=========')
        print('seleccione la accion que desea realizar'
              '\n 1.Hacer reservacion'
              '\n 2.Modificar reserva'
              '\n 3.Cancelar reserva'
              '\n 4.Salir')
        selector= int(input())
        if selector == 1:
            control.creacion(restaurante)
        elif selector == 2:
            control.modificar(restaurante)
        elif selector == 3:
            control.eliminar()
        elif selector == 4:
            print('========Adios=========')
            break
        else:
            print('no le he entendido')
    except ValueError:
        print('no le entendi')