import mysql.connector

# Configuracion de la conexion
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'store',
    'raise_on_warnings': True
}

# Establecer la conexion
try:
    conn = mysql.connector.connect(**config)
    print("conexión exitosa a la base de datos MySQL")
    
    # Aquí se pueden realizar consultas, inserciones, etc...
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")
    
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexión cerrada")