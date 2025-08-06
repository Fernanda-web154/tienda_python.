import mysql.connector

def conectar(consulta_sql, params=None):
    """Conecta a la base de datos y ejecuta consultas de manera segura"""
    config = {
        'user': 'utmxn2kyt9kerrpc',
        'password': 'FqsJs3ZfRTfJCeEFPyWM',
        'host': 'bwdqevrj2jtcobnufxh3-mysql.services.clever-cloud.com',
        'database': 'bwdqevrj2jtcobnufxh3',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        
        # Ejecutar con parámetros para prevenir inyecciones SQL
        if params:
            cursor.execute(consulta_sql, params)
        else:
            cursor.execute(consulta_sql)
        
        # Manejar diferentes tipos de consultas
        if consulta_sql.strip().lower().startswith('select'):
            resultado = cursor.fetchall()
        else:
            conexion.commit()
            resultado = cursor.rowcount
        
        cursor.close()
        conexion.close()
        return resultado

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        raise  # Relanzar la excepción para manejo en el llamador