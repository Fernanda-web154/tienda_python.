import tkinter as tk
from services.my_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="purple",
        width=500,
        height=540
    )
    login_panel.pack(side="left", fill="both")

    # Formulario de login
    tk.Label(login_panel, text="Login", bg="purple", fg="white").pack(pady=5)
    tk.Label(login_panel, text="Correo", bg="purple", fg="white").pack()
    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

    tk.Label(login_panel, text="Contraseña", bg="purple", fg="white").pack()
    entrada_contrasenna = tk.Entry(login_panel, show="*")
    entrada_contrasenna.pack()

    # Panel para mostrar categorías (a la derecha)
    resultado_panel = tk.Frame(ventana, bg="white", width=500, height=540)
    resultado_panel.pack(side="right", fill="both", expand=True)

    def funcion_boton():
        correo = entrada_correo.get()
        contrasenna = entrada_contrasenna.get()

        # Ejecuta consulta para mostrar las categorías
        resultados = conectar("SELECT * FROM categorias")

        # Limpia el panel anterior
        for widget in resultado_panel.winfo_children():
            widget.destroy()

        # Muestra los resultados en el panel derecho
        for categoria in resultados:
            tk.Label(resultado_panel, text=f"{categoria[0]} - {categoria[1]}", bg="white", anchor="w").pack(padx=10, pady=2)

    tk.Button(login_panel, text="Continuar", command=funcion_boton).pack(pady=10)

