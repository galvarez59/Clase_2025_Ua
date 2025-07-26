import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ============================
# ===   VENTANA GRUPO 1    ===
# ============================
def ventana_grupo_1():
    win = tk.Toplevel(root)
    win.title("Poligono 1")
    win.geometry("400x250")

    label = ttk.Label(win, text="Poly_1\nAgrega aquí tu código de filtrado", font=("Segoe UI", 14))
    label.pack(pady=50)

    # Botón para volver al menú principal
    btn_volver = tk.Button(
        win, 
        text="Volver al menú principal", 
        command=win.destroy, 
        bg="#dfe6e9", 
        font=("Segoe UI", 10, "bold")
    )
    btn_volver.pack(pady=10)


# ============================
# ===   VENTANA GRUPO 2    ===
# ============================
def ventana_grupo_2():
    win = tk.Toplevel(root)
    win.title("Poligono 2")
    win.geometry("400x300")

    # Ejemplo de función que muestra una alerta
    def ejemplo_funcion():
        messagebox.showinfo("Ejemplo", "Esto es un ejemplo para el Poly_2.")

    # Botón de ejemplo
    btn_ejemplo = tk.Button(
        win, 
        text="Mostrar Ejemplo", 
        command=ejemplo_funcion,
        bg="#ffeaa7", 
        font=("Segoe UI", 10)
    )
    btn_ejemplo.pack(pady=20)

    # Botón para volver al menú principal
    btn_volver = tk.Button(
        win, 
        text="Volver al menú principal", 
        command=win.destroy, 
        bg="#dfe6e9", 
        font=("Segoe UI", 10, "bold")
    )
    btn_volver.pack(pady=10)


# ============================
# ===   VENTANA GRUPO 3    ===
# ============================
def ventana_grupo_3():
    win = tk.Toplevel(root)
    win.title("Poligono 3")
    win.geometry("400x250")

    label = ttk.Label(win, text="Poly_3\nAgrega aquí tu código de filtrado", font=("Segoe UI", 14))
    label.pack(pady=50)

    # Botón para volver al menú principal
    btn_volver = tk.Button(
        win, 
        text="Volver al menú principal", 
        command=win.destroy, 
        bg="#dfe6e9", 
        font=("Segoe UI", 10, "bold")
    )
    btn_volver.pack(pady=10)


# ============ VENTANA PRINCIPAL =============
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x500")
root.configure(bg="#ecf0f1")

# Título principal
banner = ttk.Label(
    root, 
    text="Filtrado de Nube de Puntos", 
    anchor="center",
    font=("Segoe UI", 20, "bold"), 
    background="#0984e3", 
    foreground="white"
)
banner.pack(fill="x", pady=(0, 20))

# Instrucciones
instruccion = ttk.Label(
    root, 
    text="Seleccione un Poligono", 
    font=("Segoe UI", 12), 
    background="#ecf0f1"
)
instruccion.pack(pady=(10, 30))

# Botones para abrir cada polígono
b1 = tk.Button(
    root, 
    text="Poligono 1", 
    font=("Segoe UI", 14, "bold"), 
    width=30, 
    height=2,
    bg="#0550a7", 
    fg="white", 
    command=ventana_grupo_1
)
b1.pack(pady=15)

b2 = tk.Button(
    root, 
    text="Poligono 2", 
    font=("Segoe UI", 14, "bold"), 
    width=30, 
    height=2,
    bg="#fdcb6e", 
    fg="white", 
    command=ventana_grupo_2
)
b2.pack(pady=15)

b3 = tk.Button(
    root,
    text="Poligono 3",
    font=("Segoe UI", 14, "bold"),
    width=30,
    height=2,
    bg="#e17055",
    fg="white",
    command=ventana_grupo_3
)
b3.pack(pady=15)

# Inicia la aplicación
root.mainloop()
