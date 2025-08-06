import tkinter as tk
import mysql.connector
from tkinter import font as tkfont
from paneles.formulario import crear_formulario_registro
from tkinter import ttk

# Variable global para almacenar el panel de lista
lista_frame = None

def crear_panel_productos(panel_principal):
    global lista_frame
    
    # Configurar grid para el panel principal
    panel_principal.columnconfigure(0, weight=1)
    panel_principal.columnconfigure(1, weight=1)
    panel_principal.columnconfigure(2, weight=3)
    panel_principal.rowconfigure(0, weight=1)
    
    # Contenedor para formulario de registro
    registro_frame = tk.LabelFrame(
        panel_principal, 
        text="Registrar Producto",
        font=("Arial", 12, "bold"),
        bg="#F5F5F5",
        padx=15,
        pady=15,
        relief=tk.GROOVE,
        borderwidth=2
    )
    registro_frame.grid(row=0, column=0, sticky="nsew", padx=(10, 5), pady=10)
    
    # Contenedor para lista de productos (guardar referencia global)
    lista_frame = tk.LabelFrame(
        panel_principal, 
        text="Productos Registrados",
        font=("Arial", 12, "bold"),
        bg="#F5F5F5",
        padx=15,
        pady=15,
        relief=tk.GROOVE,
        borderwidth=2
    )
    lista_frame.grid(row=0, column=2, columnspan=2, sticky="nsew", padx=(5, 10), pady=10)
    
    # Crear formulario con callback
    crear_formulario_registro(
        registro_frame, 
        actualizar_lista_productos
    )
    
    # Cargar y mostrar lista inicial de productos
    actualizar_lista_productos()

def actualizar_lista_productos():
    # Limpiar panel existente
    for widget in lista_frame.winfo_children():
        widget.destroy()
    
    # Configurar grid para lista
    lista_frame.columnconfigure(0, weight=1)
    lista_frame.rowconfigure(0, weight=1)
    
    # Crear contenedor con scroll
    container = tk.Frame(lista_frame, bg="#FFFFFF")
    container.grid(row=0, column=0, sticky="nsew")
    
    # Crear canvas y scrollbar
    canvas = tk.Canvas(container, bg="#FFFFFF", highlightthickness=0)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#FFFFFF")
    
    # Configurar scroll
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Obtener datos de productos
    try:
        conexion = mysql.connector.connect(
            user='utmxn2kyt9kerrpc',
            password='FqsJs3ZfRTfJCeEFPyWM',
            host='bwdqevrj2jtcobnufxh3-mysql.services.clever-cloud.com',
            database='bwdqevrj2jtcobnufxh3',
            raise_on_warnings=True
        )
        
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, precio, cantidad FROM productos ORDER BY nombre")
        productos = cursor.fetchall()
        
        # Fuente para los productos
        font_productos = tkfont.Font(family="Arial", size=11)
        font_precio = tkfont.Font(family="Arial", size=11, weight="bold")
        
        # Mostrar cada producto con todos los detalles
        for i, producto in enumerate(productos):
            nombre = producto[0]
            precio = f"${float(producto[1]):.2f}"
            cantidad = producto[2]
            
            # Determinar color de fondo alternado
            bg_color = "#f8f9fa" if i % 2 == 0 else "#ffffff"
            
            # Crear frame para cada producto con fondo alternado
            producto_frame = tk.Frame(scrollable_frame, bg=bg_color)
            producto_frame.pack(fill="x", padx=0, pady=2)
            
            # Viñeta decorativa
            tk.Label(
                producto_frame,
                text="•",
                font=("Arial", 16),
                bg=bg_color,
                fg="#4A235A"
            ).pack(side="left", padx=(10, 5))
            
            # Contenedor para detalles del producto
            detalles_frame = tk.Frame(producto_frame, bg=bg_color)
            detalles_frame.pack(side="left", fill="x", expand=True, padx=(0, 10))
            
            # Nombre del producto
            tk.Label(
                detalles_frame,
                text=nombre,
                font=font_productos,
                bg=bg_color,
                anchor="w",
                justify="left"
            ).pack(fill="x")
            
            # Precio y cantidad en la misma línea
            info_frame = tk.Frame(detalles_frame, bg=bg_color)
            info_frame.pack(fill="x")
            
            # Precio en verde y negrita
            tk.Label(
                info_frame,
                text=f"Precio: {precio}",
                font=font_precio,
                bg=bg_color,
                fg="#27ae60",
                anchor="w"
            ).pack(side="left", fill="x")
            
            # Espaciador
            tk.Label(
                info_frame,
                text=" • ",
                font=font_productos,
                bg=bg_color,
                fg="#7f8c8d"
            ).pack(side="left")
            
            # Cantidad
            tk.Label(
                info_frame,
                text=f"Cantidad: {cantidad}",
                font=font_productos,
                bg=bg_color,
                anchor="w"
            ).pack(side="left", fill="x")
            
            # Separador entre productos
            if i < len(productos) - 1:
                separator = tk.Frame(scrollable_frame, height=1, bg="#e0e0e0")
                separator.pack(fill="x", padx=10, pady=5)
        
        cursor.close()
        conexion.close()
        
        # Contador de productos
        contador_frame = tk.Frame(lista_frame, bg="#F5F5F5", height=30)
        contador_frame.grid(row=1, column=0, sticky="ew", pady=(5, 0))
        
        tk.Label(
            contador_frame,
            text=f"Total de productos: {len(productos)}",
            font=("Arial", 10, "italic"),
            bg="#F5F5F5",
            fg="#555555"
        ).pack(side="right", padx=10)
        
    except mysql.connector.Error as err:
        tk.Label(
            lista_frame, 
            text=f"Error de conexión: {err}", 
            fg="red",
            bg="#F5F5F5",
            font=("Arial", 12)
        ).grid(row=0, column=0, sticky="nsew")