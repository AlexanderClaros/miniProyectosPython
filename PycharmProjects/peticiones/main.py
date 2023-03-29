import MySQLdb

conexion = MySQLdb.connect(host='localhost',user='root',passwd='',db='lista_tareas')
cur = conexion.cursor()
cur.execute('SELECT titulo, descripcion FROM listado')
for titulo, descripcion  in cur.fetchall():
    print(titulo,': ',descripcion)
conexion.close()