import tkinter as tk
from services.my_sql import conectar

def cargar_productos(ventana):
    productos_panel = tk.Frame(
        ventana, 
        bg="purple", 
        padx=0, 
        pady=0,
        width=1000,
        height=400,
    )
    
    # Obtener productos de la base de datos
    resultados = conectar("SELECT * FROM productos")
    
    # Crear contenedor para productos
    contenedor = tk.Frame(productos_panel, bg="purple")
    contenedor.pack(pady=20)
    
    # Mostrar productos
    if resultados:
        for producto in resultados:
            producto_texto = f"ID: {producto[0]} | Nombre: {producto[1]}"
            label = tk.Label(
                contenedor,
                text=producto_texto,
                bg="white",
                fg="black",
                padx=10,
                pady=5,
                width=80,
                anchor="w"
            )
            label.pack(pady=5)
    else:
        tk.Label(contenedor, text="No hay productos disponibles", bg="purple", fg="white").pack()

    productos_panel.pack()
