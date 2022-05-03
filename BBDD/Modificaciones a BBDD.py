import mysql.connector
from mysql.connector import Error


# Objeto para crear conexion a BBDD
connect = mysql.connector.connect(
    host="localhost",
    username="root",
    password="sasasa",
    db="gimnasio")

try:
    if connect.is_connected():
        print("Conexion Establecida correctamente")

except Error as error:
    connect = None
    print("Error durante la conexion: ", error)

finally:
    pass

# Creacion de puntero/cursor para realizar querys
cursor = connect.cursor(buffered=True)

# Ejecucion de query.
nombre = "Jorge"
id = 2
query = "UPDATE clientes SET cli_nombre=%s WHERE cli_id=%s"
cursor.execute(query, (nombre, id))

# Metodo commit (confirmar) se debe llamar cada vez que se quieran realizar cambios.
connect.commit()

# Insert unico

#query = "INSERT INTO clientes (cli_nombre, cli_empresa) VALUES ('Jacinto','Microsoft')"
# cursor.execute(query)
# connect.commit()

# Insert Lote de registros

# varios_registros = [
#    ("Pedro", "Apple"),
#    ("Camila", "Samsung"),
#    ("Joaquina", "Microsoft")
# ]
#query = "INSERT INTO clientes (cli_nombre, cli_empresa) VALUES (%s,%s)"
#cursor.executemany(query, varios_registros)
# connect.commit()


cursor.close()
connect.close()
if not connect.is_connected():
    print("Conexion finalizada correctamente")
