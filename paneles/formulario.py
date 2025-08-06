import tkinter as tk
import mysql.connector
from tkinter import messagebox

def crear_formulario_registro(panel, actualizar_lista_callback):
    # Configurar grid para formulario
    panel.columnconfigure(0, weight=1)
    panel.columnconfigure(1, weight=1)
    
    # Campos del formulario
    campos = [
        ("Nombre del Producto", "nombre"),
        ("Precio ($)", "precio"),
        ("Cantidad", "cantidad")
    ]
    
    entries = {}
    for i, (label, key) in enumerate(campos):
        # Etiqueta
        tk.Label(
            panel, 
            text=label + ":",
            bg="#F5F5F5",
            font=("Arial", 10),
            anchor="e"
        ).grid(row=i, column=0, padx=5, pady=8, sticky="ew")
        
        # Campo de entrada
        entry = tk.Entry(
            panel, 
            width=20, 
            font=("Arial", 10),
            relief="solid",
            borderwidth=1
        )
        entry.grid(row=i, column=1, padx=5, pady=8, sticky="ew")
        entries[key] = entry
    
    # Botón de registro
    btn_registrar = tk.Button(
        panel,
        text="REGISTRAR PRODUCTO",
        bg="#4A235A",
        fg="white",
        font=("Arial", 10, "bold"),
        height=2,
        command=lambda: registrar_producto(entries, actualizar_lista_callback)
    )
    btn_registrar.grid(row=len(campos), column=0, columnspan=2, pady=15, sticky="nsew")

def registrar_producto(entries, actualizar_lista_callback):
    try:
        # Obtener valores
        nombre_val = entries['nombre'].get()
        precio_val = entries['precio'].get()
        cantidad_val = entries['cantidad'].get()
        
        # Validar campos
        if not all([nombre_val, precio_val, cantidad_val]):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Convertir valores numéricos
        try:
            precio_val = float(precio_val)
            cantidad_val = int(cantidad_val)
        except ValueError:
            messagebox.showerror("Error", "Precio debe ser un número y Cantidad un entero")
            return
        
        # Conexión a la base de datos (TUS DATOS)
        conexion = mysql.connector.connect(
            user='utmxn2kyt9kerrpc',
            password='FqsJs3ZfRTfJCeEFPyWM',
            host='bwdqevrj2jtcobnufxh3-mysql.services.clever-cloud.com',
            database='bwdqevrj2jtcobnufxh3'
        )
        
        cursor = conexion.cursor()
        
        # Verificar si el producto existe (CORRECCIÓN: EJECUTAR CONSULTA PRIMERO)
        cursor.execute("SELECT * FROM productos WHERE nombre = %s", (nombre_val,))
        existe = cursor.fetchone()
        
        if existe:
            # Actualizar producto existente (CORRECCIÓN: QUITAR ID)
            cursor.execute(
                "UPDATE productos SET precio = %s, cantidad = %s WHERE nombre = %s",
                (precio_val, cantidad_val, nombre_val)
            )
            mensaje = "Producto actualizado correctamente"
        else:
            # Insertar nuevo producto (CORRECCIÓN: QUITAR ID)
            cursor.execute(
                "INSERT INTO productos (nombre, precio, cantidad) VALUES (%s, %s, %s)",
                (nombre_val, precio_val, cantidad_val)
            )
            mensaje = "Producto registrado correctamente"
        
        conexion.commit()
        cursor.close()
        conexion.close()
        
        # Actualizar lista usando callback
        actualizar_lista_callback()
        
        # Limpiar formulario
        for entry in entries.values():
            entry.delete(0, tk.END)
        
        messagebox.showinfo("Éxito", mensaje)

        
    except mysql.connector.Error as err:
        messagebox.showerror("Error de base de datos", f"Error: {err}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")