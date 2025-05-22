import mysql.connector

def conectar(consulta_sql):
    # Credenciales para la conexión
    config = {
        'user': 'utmxn2kyt9kerrpc',
        'password': 'FqsJs3ZfRTfJCeEFPyWM',
        'host': 'bwdqevrj2jtcobnufxh3-mysql.services.clever-cloud.com',
        'database': 'bwdqevrj2jtcobnufxh3',
        'raise_on_warnings': True
    }

    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(**config)
        consulta = conexion.cursor()

        # Ejecutar la consulta SQL
        consulta.execute(consulta_sql)

        # Obtener resultados
        resultado = consulta.fetchall()

        # Cerrar cursor y conexión
        consulta.close()
        conexion.close()

        return resultado

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

