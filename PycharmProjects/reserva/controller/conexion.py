import MySQLdb
from datetime import datetime
def conectar():
    conexion= MySQLdb.connect(host='localhost',user='root',passwd='',db='reservas')
    conectado= conexion.cursor()
    return conectado,conexion
def insertar (conect,conexion,objeto):
    fecha =objeto.fecha.strftime('%Y-%d-%m')
    hora=objeto.hora.strftime('%H:%M')
    conexion.execute('INSERT INTO lista_reservas(fecha,hora,comensales,name,telfono,mesa)VALUES(%s,%s,%s,%s,%s,%s)',(fecha,hora,objeto.comensales,objeto.name,objeto.telf,objeto.table))
    conect.commit()
    print('reserva realizada exitosamente')
def select(conexion , buscar ,condicion):
    conexion.execute('SELECT' + buscar +'FROM lista_reservas WHERE ' +condicion)
    return conexion
def actualizar_fecha (conect,conexion,objeto,id):
    try:
        fecha =objeto.strftime('%Y-%d-%m')
        correct = str(id)
        conexion.execute('UPDATE lista_reservas SET fecha=%s WHERE id=%s',(fecha,correct))
        conect.commit()
        print('reserva actualizada exitosamente')
    except ValueError as err:
        print(err)
def actualizar_hora (conect,conexion,objeto,id):
    try:
        hora =objeto.strftime('%H:%M')
        correct = str(id)
        conexion.execute('UPDATE lista_reservas SET hora=%s WHERE id=%s',(hora,correct))
        conect.commit()
        print('reserva actualizada exitosamente')
    except ValueError as err:
        print(err)
def actualizar_comensales (conect,conexion,comensales,mesa,id):
    try:
        correct = str(id)
        conexion.execute('UPDATE lista_reservas SET comensales=%s , mesa=%s WHERE id=%s',(comensales,mesa,correct))
        conect.commit()
        print('reserva actualizada exitosamente')
    except ValueError as err:
        print(err)

def eliminar(connect,conexion,id):
    correct=str(id)
    conexion.execute('DELETE FROM lista_reservas WHERE id=%s',correct)
    connect.commit()
    print('reserva eliminada con exito')