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
    print("Error durante la conexion: {}".format(error))


# Creacion de puntero/cursor para realizar querys
cursor = connect.cursor(buffered=True)

# Ejecucion de query.
cursor.execute("SELECT * FROM clientes")

# cursor.fetchall (Extraer todo), se extraen todos los registros de la ejecucion, y se almacenan dentro de una variable como lista cuyo contenido serian tuplas de cada registro.
resultado = cursor.fetchall()
print(resultado)
for filas in resultado:
    print(filas)  # filas[0] imprime solo primera columna
print(f"Total de registros: {cursor.rowcount}")

#query = cursor.fetchone()
# while query is not None:
#    print(query)
#    query = cursor.fetchone()

# Cuando se hace una consulta en base a un dato entregado por usuario, se debe usar el "%s" y pasar como parametro el dato en el cursor.execute, ya que asi se evita que se pueda realizar un SQL inject.
dato = input("Ingrese la id de cliente que desea consultar: ")
query = "SELECT * FROM clientes WHERE cli_id= %s"
cursor.execute(query, (dato,))
resultado2 = cursor.fetchall()
for filas in resultado2:
    print(filas)


cursor.close()
connect.close()
if not connect.is_connected():
    print("Conexion finalizada correctamente")
