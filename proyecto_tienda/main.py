import tkinter as tk
from views.login_view import cargar_login
from views.productos_view import cargar_productos
from views.header_view import cargar_header

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("mi tienda")
ventana.geometry("1000x600")

# Cargar los módulos de la interfaz
cargar_header(ventana)
cargar_login(ventana)

# Iniciar el bucle de la ventana
ventana.mainloop()
