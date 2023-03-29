from models.reserva import Reserva
from datetime import datetime
from controller import conexion
import math


def creacion(restaurante):

    con, conect = conexion.conectar()
    fecha_resv = ''
    hora_resv = ''
    comensales=''
    ocupado = 0
    while True:
        try:
            while True:
                try:
                    print('indique la fecha en la que quiera realizar la reserva ')
                    print('con el siguiente formato \'dia-mes-año\', \' 00-00-0000\' ')
                    fecha = input()
                    fecha_resv = datetime.strptime(fecha,'%d-%m-%Y')
                    hoy = datetime.now().date()
                    comprobar = fecha_resv.date()-hoy
                    if comprobar.days < 0:
                        print('introduzca una fecha valida')
                    else:
                        break
                except ValueError:
                    print('Formato de fecha incorrecto')
            while True:
                try:
                    print(' indique la hora que quiere reservar el ', fecha_resv.date())
                    print('con el siguiente formato \' HH:mm\' \'00:00\'')
                    hora=input()
                    hora_resv = datetime.strptime(hora,'%H:%M')
                    if hora< restaurante.hour_open.strftime('%H:%M') or hora >restaurante.hour_close.strftime('%H:%M'):
                        print('no se pueden realizar reservas fuera de horario laboral')
                    elif hora == restaurante.hour_close.strftime('%H:%M'):
                        print('esa es hora de cierre')
                    else:
                        break
                except ValueError:
                    print('Formato de hora incorrecto')
            while True:
                try:
                    print('indique el numero de comensales')
                    comensales =int(input())
                    if comensales> restaurante.num_table * restaurante.num_people:
                        print('exede la cantidad de mesas disponibles ')
                    else:
                        break
                except ValueError:
                    print('error al introducir comensales')
            condicion='fecha= CONVERT(\''+fecha_resv.date().strftime('%Y-%d-%m')+'\',DATE) AND hora= CONVERT(\''+hora_resv.time().strftime('%H:%M')+'\',TIME)'
            result= conexion.select(con,' mesa ', condicion)

            for mesa in result.fetchall():
                mesa_o = int(''.join(map(str,mesa)))
                ocupado =ocupado+ mesa_o
            if ocupado >= restaurante.num_table:
                print('no quedan reservaciones disponibles a esa hora  para esa cantidad de comensales')
            else:
                break
        except ValueError:
            print('error en la reservacion')

    print('introduzca el nombre al que quiere hacer la reserva')
    name = input()
    while True:
        try:
            print('introduzca numero de tlf:')
            tlf = int(input())
            break
        except ValueError:
            print('error al introducir el numero de telefono')
    reservacion = Reserva(fecha_resv.date(), hora_resv.time(), comensales, name, tlf,math.ceil(comensales / restaurante.num_people))
    conexion.insertar(conect,con,reservacion)
    print(reservacion.fecha, ' ', reservacion.hora, ' \n Comensales:', reservacion.comensales, ' mesas reservadas: ', reservacion.table,'\n nombre:', reservacion.name, ' tlf:',reservacion.telf)

    conect.close()

def busqueda():
    while True:
        try:
            print('introduce la la fecha de la reserva')
            print('con el siguiente formato \'dia-mes-año\', \' 00-00-0000\' ')
            fecha = input()
            fecha_resv = datetime.strptime(fecha,'%d-%m-%Y')

            print(' indique la hora de la reserva ', fecha_resv.date())
            print('con el siguiente formato \' HH:mm\' \'00:00\'')
            hora=input()
            hora_resv = datetime.strptime(hora,'%H:%M')

            print('introduzca el nombre del propietario de la reserva')
            name = input()

            print('introduzca numero de tlf:')
            tlf = int(input())


            break
        except ValueError:
            print('error al introducir los datos incorrecto')
    con, connect = conexion.conectar()
    condicion = 'fecha= CONVERT(\'' + fecha_resv.date().strftime('%Y-%d-%m') + '\',DATE) AND hora= CONVERT(\'' + hora_resv.time().strftime('%H:%M') + '\',TIME)'+' AND name = \'' +name+ '\' AND telfono= \''+str(tlf) +'\''
    result = conexion.select(con,' id ',condicion)
    for id in result.fetchall():
        identificador = int(''.join(map(str, id)))
        if id == 0:
            return 0
        else:
            return identificador


def modificar(restaurante):
    while True:
        try:
            id = busqueda()

            if id == None:
                print('surgio un error al buscar esa reserva vuelva a intentarlo')
            else:
                con, connect = conexion.conectar()

                print('seleccione que desa modificar'
                      '\n1.Fecha'
                      '\n2.Hora'
                      '\n3.Numero comensales'
                      '\n4.Salir')

                seleccionado = int(input())

                if seleccionado == 1:
                    while True:
                        try:
                            print('indique la fecha en la que quiera realizar la reserva ')
                            print('con el siguiente formato \'dia-mes-año\', \' 00-00-0000\' ')
                            fecha = input()
                            fecha_resv = datetime.strptime(fecha, '%d-%m-%Y')
                            hoy = datetime.now().date()
                            comprobar = fecha_resv.date() - hoy
                            if comprobar.days < 0:
                                print('introduzca una fecha valida')
                            else:
                                break
                        except ValueError:
                            print('Formato de fecha incorrecto')
                    conexion.actualizar_fecha(connect,con,fecha_resv,id)
                    break
                elif seleccionado ==2:
                    while True:
                        try:
                            print(' indique la hora que quiere reservar')
                            print('con el siguiente formato \' HH:mm\' \'00:00\'')
                            hora = input()
                            hora_resv = datetime.strptime(hora, '%H:%M')
                            if hora < restaurante.hour_open.strftime('%H:%M') or hora > restaurante.hour_close.strftime('%H:%M'):
                                print('no se pueden realizar reservas fuera de horario laboral')
                            elif hora == restaurante.hour_close.strftime('%H:%M'):
                                print('esa es hora de cierre')
                            else:
                                break
                        except ValueError:
                            print('Formato de hora incorrecto')
                    conexion.actualizar_hora(connect,con,hora_resv,id)
                    break
                elif seleccionado ==3:
                    ocupado = 0
                    while True:
                        try:
                            print('indique el numero de comensales')
                            comensales = input()
                            comensales_int= int(comensales)
                            if comensales_int > restaurante.num_table * restaurante.num_people:
                                print('exede la cantidad de mesas disponibles ')
                            else:
                                break
                        except ValueError:
                            print('error al introducir comensales')
                    correct= str(id)
                    condicion_tmp = 'id=\''+correct+'\''
                    select_tmp = conexion.select(con,' * ',condicion_tmp )
                    reserva_tmp= None
                    for reserva in select_tmp.fetchall():
                        reserva_tmp = Reserva(reserva[1],reserva[2],reserva[3],reserva[4],reserva[5],reserva[6])
                    fecha_str= str(reserva_tmp.fecha)
                    fecha =datetime.strptime(fecha_str,'%Y-%d-%m')
                    hora_str=str(reserva_tmp.hora)
                    hora =datetime.strptime(hora_str,'%H:%M:%S')
                    condicion = 'fecha= CONVERT(\'' + fecha.strftime('%Y-%d-%m') + '\',DATE) AND hora= CONVERT(\'' + hora.strftime('%H:%M') + '\',TIME)'
                    result = conexion.select(con, ' mesa ', condicion)

                    for mesa in result.fetchall():
                        mesa_o = int(''.join(map(str, mesa)))
                        ocupado = ocupado + mesa_o
                    mesa_tmp=int(reserva_tmp.table)
                    ocupado=ocupado+mesa_tmp
                    if ocupado >= restaurante.num_table:
                        print('no quedan reservaciones disponibles a esa hora  para esa cantidad de comensales')
                    else:
                        mesas_dispo= comensales_int / restaurante.num_people
                        conexion.actualizar_comensales(connect, con, comensales,mesas_dispo,id)
                        break



                elif seleccionado ==4:
                    break
        except ValueError as err:
            print('no le entendi')
            print(err)

def eliminar():
    id = busqueda()
    while True:
        try:
            if id == None:
                print('surgio un error al buscar esa reserva vuelva a intentarlo')
            else:
                con, connect = conexion.conectar()

                print('esta seguro que quieres eliminar la reserva'
                      '\n1.Si'
                      '\n2.No')

                seleccionado = int(input())

                if seleccionado == 1:
                    conexion.eliminar(connect, con,id)
                    break
                elif seleccionado == 2:

                    break
        except ValueError as err:
            print('no le entendi')
            print(err)