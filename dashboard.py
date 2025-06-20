import tkinter as tk 
from .productos_view import crear_panel_productos

def ventana_usuario(ventana_principal, datos_usuario):
    # Limpiar la ventana principal
    for widget in ventana_principal.winfo_children():
        widget.destroy()
    
    # Configurar la ventana principal
    ventana_principal.title("Dashboard - Mi Tienda")
    ventana_principal.geometry("1200x700")
    ventana_principal.configure(bg="#F5F5F5")
    
    # Crear contenedor principal
    panel_principal = tk.Frame(ventana_principal, bg="#F5F5F5")
    panel_principal.pack(fill="both", expand=True, padx=20, pady=20)
    
    # Cargar el panel de productos
    crear_panel_productos(panel_principal)