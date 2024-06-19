#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Obtener los argumentos de linea de comandos
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Conectarse al servidor MYSQL
    db = MySQLdb.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
        port=3306)

    # Crear un cursor para ejecutar consultas
    cur = db.cursor()

    # Ejecutar consulta SQL
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Obtener todos los resultados de la consulta
    rows = cur.fetchall()

    # Imprimir cada fila
    for row in rows:
        print(row)

    # Cerrar el cursor y la conexion a la base de datos
    cur.close()
    db.close()
