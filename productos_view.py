import tkinter as tk
import mysql.connector

def cargar_productos(ventana):
    # Panel principal que ocupa toda la ventana
    productos_panel = tk.Frame(ventana, bg="#F5F5F5")
    productos_panel.pack(fill="both", expand=True)
    
    # Título
    tk.Label(
        productos_panel, 
        text="Lista de Productos", 
        font=("Arial", 16, "bold"),
        bg="#F5F5F5",
        pady=10
    ).pack()
    
    # Contenedor para la tabla
    tabla_frame = tk.Frame(productos_panel, bg="white", padx=10, pady=10)
    tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Crear encabezados
    encabezados = ["ID", "Nombre", "Precio", "Cantidad"]
    for col, encabezado in enumerate(encabezados):
        tk.Label(
            tabla_frame, 
            text=encabezado, 
            bg="#4A235A", 
            fg="white",
            font=("Arial", 10, "bold"),
            width=15,
            padx=5,
            pady=5
        ).grid(row=0, column=col, sticky="ew", padx=1, pady=1)
    
    # Obtener datos
    try:
        conexion = mysql.connector.connect(
            user='utmxn2kyt9kerrpc',
            password='FqsJs3ZfRTfJCeEFPyWM',
            host='bwdqevrj2jtcobnufxh3-mysql.services.clever-cloud.com',
            database='bwdqevrj2jtcobnufxh3',
            raise_on_warnings=True
        )
        
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, cantidad FROM productos")
        productos = cursor.fetchall()
        
        # Mostrar datos
        for fila, producto in enumerate(productos, start=1):
            for col, valor in enumerate(producto):
                bg_color = "#E8EAF6" if fila % 2 == 0 else "#FFFFFF"
                tk.Label(
                    tabla_frame, 
                    text=valor, 
                    bg=bg_color,
                    font=("Arial", 9),
                    width=15,
                    padx=5,
                    pady=5,
                    anchor="w"
                ).grid(row=fila, column=col, sticky="ew", padx=1, pady=1)
        
        cursor.close()
        conexion.close()
        
    except mysql.connector.Error as err:
        tk.Label(
            productos_panel, 
            text=f"Error de conexión: {err}", 
            fg="red",
            bg="#F5F5F5",
            font=("Arial", 12)
        ).pack(pady=20)
    
    print("Panel y productos cargados correctamente")