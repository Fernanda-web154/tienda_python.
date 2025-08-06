import tkinter as tk
from paneles.login_view import cargar_login
from views.dashboard import ventana_usuario

def on_login_success(usuario):
    print(f"Usuario autenticado: {usuario[1]}")
    ventana_usuario(ventana, usuario)

ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("1000x600")

# Cargar el login y pasar la función de callback
login_panel = cargar_login(ventana, on_login_success)  # Pasar el callback
login_panel.pack(fill="both", expand=True)

ventana.mainloop()