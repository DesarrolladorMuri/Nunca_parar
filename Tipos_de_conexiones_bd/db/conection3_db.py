from sqlalchemy import create_engine

# configuración de la conexión
engine = create_engine('mysql+pymysql://usario:contraseña@localhost/store')

# Establecer la conexión
try:
    conn = engine.connect()
    print("Conexión exitosa a la base de datos MySQL")
    
    # Aquí se pueden realizar consultas, inserciones, etc...
    
except Exception as e:
    print(f"Error al conectar a la base de datos MySQL: {e}")
    
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Conexión cerrada")