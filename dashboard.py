import tkinter as tk 
from views.productos_view import cargar_productos

def ventana_usuario(ventana_principal, datos_usuario):
    # Limpiar la ventana principal
    for widget in ventana_principal.winfo_children():
        widget.destroy()
    
    # Configurar la ventana principal
    ventana_principal.title("Dashboard - Mi Tienda")
    ventana_principal.geometry("1000x600")
    
    # Cargar los productos en la ventana principal
    cargar_productos(ventana_principal)