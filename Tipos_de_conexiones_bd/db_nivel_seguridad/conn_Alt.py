import mysql.connector

# Configuracion de la conexion
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'store',
    'auth_plugin': 'caching_sha2_password',
    'ssl_ca': '/ruta/al/archivo/ca.pem', #Opcional: Certificado Ca para SSl
    'ssl_cart': '/ruta/al/archivo/cart.pem', #Opcional: Certificado del cliente para SSL
    'ssl_key': '/ruta/al/archivo/cliente_key.pem', #Opcional: Clave privada del cliente para SSL
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