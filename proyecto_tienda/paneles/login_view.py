import tkinter as tk
from services.my_sql import conectar # Importación corregida

def cargar_login(ventana, on_success_callback):
    login_panel = tk.Frame(
        ventana,
        bg="purple",
        width=1000,
        height=600,
    )
    login_panel.pack(fill="both", expand=True)
    
    # Titulo
    titulo = tk.Label(login_panel, text="Login", font=("Arial", 16), bg="purple", fg="white")
    titulo.pack(pady=20)
    
    # Contenedor para el formulario
    form_frame = tk.Frame(login_panel, bg="white", padx=20, pady=20)
    form_frame.pack(pady=20, padx=100, fill="x")
    
    # Entrada correo
    tk.Label(form_frame, text="Correo", anchor="w", bg="white").pack(fill="x", pady=(10,0))
    entrada_correo = tk.Entry(form_frame)
    entrada_correo.pack(fill="x", pady=5)
    
    # Entrada contraseña
    tk.Label(form_frame, text="Contraseña", anchor="w", bg="white").pack(fill="x", pady=(10,0))
    entrada_contrasenna = tk.Entry(form_frame, show="*")
    entrada_contrasenna.pack(fill="x", pady=5)
    
    # Mensaje de error
    error_label = tk.Label(form_frame, text="", fg="red", bg="white")
    error_label.pack(pady=5)
    
    def funcion_boton():
        correo = entrada_correo.get()
        contrasenna = entrada_contrasenna.get()
        
        if not correo or not contrasenna:
            error_label.config(text="Por favor complete todos los campos")
            return
            
        try:
            # Consulta segura con parámetros
            consultar_usuario = conectar(
                "SELECT * FROM usuarios WHERE correo = %s AND contrasenna = %s",
                (correo, contrasenna)
            )
            
            if consultar_usuario:
                print("¡Éxito! Inicio de sesión exitoso:", consultar_usuario[0][1])
                on_success_callback(consultar_usuario[0])
            else:
                error_label.config(text="Credenciales incorrectas")
        except Exception as e:
            error_label.config(text=f"Error: {str(e)}")
    
    # Botón
    tk.Button(
        form_frame, 
        text="Continuar", 
        command=funcion_boton,
        bg="#4A235A",
        fg="white",
        padx=10,
        pady=5
    ).pack(pady=20)
    
    return login_panel