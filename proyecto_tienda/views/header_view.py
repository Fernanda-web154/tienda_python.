#el lenguaje es tkinter pero se pondrá como tk
import tkinter as tk 

#frame está conteniendo los elementos de la interfaz
def cargar_header(ventana):
    header_panel = tk.Frame(
        ventana,    
        bg="red", 
        padx=0, 
        pady=0,
        width=1000,
        height=400
        )
    header_panel.pack()
    #el pack sirve para que se pueda mostrar gráficamente