import pymysql
import pymysql.cursors

# Coonfiguracion de la conexión
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'store',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

# Establecer la conexión
try:
    conn = pymysql.connect(**config)
    print("Conexión exitosa a la base de datos MySQL")
    
    # Aquí se pueden realizar consultas, inserciones, etc...
except pymysql.Error as e:
    print(f"Error de conexión: {e}")

finally:
    if 'conn' in locals() and conn.open:
        conn.close()
        print("Conexión cerrada")