import tkinter as tk
from tkinter import ttk

# ============================
# ===   VENTANA GRUPO 1    ===
# ============================
def ventana_grupo_1():
    win = tk.Toplevel(root)
    win.title("Poligono 1 prueba")
    win.geometry("400x250")
    label = ttk.Label(win, text="Poly_1\nAgrega aquí tu código de filtrado", font=("Segoe UI", 14))
    label.pack(pady=50)
    # -------------- INSTRUCCIONES GRUPO 1 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

# ===================================
# ===   VENTANA GRUPO 2 Ejemplo   ===
# ===================================
def ventana_grupo_2():
    # --- IMPORTA AQUI LAS LIBRERIAS QUE NECESITES ---
    import tkinter as tk
    from tkinter import messagebox

    # --- AQUI VA TU LOGICA, FUNCIONES Y CLASES ---
    # Por ejemplo:
    def ejemplo_funcion():
        messagebox.showinfo("Ejemplo", "Esto es un ejemplo para el Poly_2.")

    # --- CREA UNA NUEVA VENTANA PARA TU GRUPO ---
    win = tk.Toplevel(root)
    win.title("Poligono 2")
    win.geometry("400x300")


    # -------------- INSTRUCCIONES GRUPO 3 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

# ============================
# ===   VENTANA GRUPO 3    ===
# ============================
def ventana_grupo_3():
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import math
    import os
        # Suma de ángulos
    def punto_en_poligono_angulo(px, py, poligono):
        total = 0.0
        n = len(poligono)
        for i in range(n):
            x1, y1 = poligono[i][0] - px, poligono[i][1] - py
            x2, y2 = poligono[(i+1)%n][0] - px, poligono[(i+1)%n][1] - py
            ang1 = math.atan2(y1, x1)
            ang2 = math.atan2(y2, x2)
            dtheta = ang2 - ang1
            while dtheta > math.pi:
                dtheta -= 2 * math.pi
            while dtheta < -math.pi:
                dtheta += 2 * math.pi
            total += dtheta
        return abs(total) > math.pi

    win = tk.Toplevel()
    win.title("Grupo 3 - Filtrado de Región")
    win.geometry("1200x840")
    win.configure(bg="#272e36")

    df = None
    df_filtrada = None
    limites = None

#Panel grafico
    panel_grafico = tk.Frame(win, bg="#ffffff", width=700, height=800, bd=0, relief="ridge", highlightthickness=0)
    panel_grafico.pack(side="left", fill="both", expand=True)
    panel_grafico.pack_propagate(False)

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#ffffff")
    ax.set_facecolor("#ffffff")
    ax.grid(True, linestyle="--", color="#a3a3a3", alpha=0.7, linewidth=1.0)
    ax.set_axisbelow(True)
    ax.set_aspect('equal', adjustable='box')
    canvas = FigureCanvasTkAgg(fig, master=panel_grafico)
    canvas.get_tk_widget().pack(expand=True, fill="both", padx=36, pady=44)
#Panel de controles
    panel_controles = tk.Frame(win, bg="#f8e9a1", width=500, height=800, bd=0, relief="ridge", highlightthickness=0)
    panel_controles.pack(side="right", fill="y")
    panel_controles.pack_propagate(False)

    tk.Label(panel_controles, text="Filtro\nGrupo 3", font=("Montserrat", 26, "bold"), bg="#f8e9a1", fg="#a76d60").pack(pady=36)
    sep1 = tk.Frame(panel_controles, height=3, bg="#a76d60")
    sep1.pack(fill="x", padx=44, pady=10)
# Entrada de archivos
    entrada_archivo_frame = tk.Frame(panel_controles, bg="#f8e9a1")
    entrada_archivo_frame.pack(pady=12)

    archivo_path_var = tk.StringVar()
    archivo_path_label = tk.Label(entrada_archivo_frame, textvariable=archivo_path_var, font=("Consolas", 11, "italic"), bg="#f8e9a1", fg="#a76d60")
    archivo_path_label.pack(pady=2)


# ============ VENTANA PRINCIPAL =============
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x500")
root.configure(bg="#ecf0f1")

banner = ttk.Label(root, text="Filtrado de Nube de Puntos", anchor="center",font=("Segoe UI", 20, "bold"), background="#0984e3", foreground="white")
banner.pack(fill="x", pady=(0, 20))

# 69 text= "esto es editable"
instruccion = ttk.Label(root, text="Seleccione un Poligono", font=("Segoe UI", 12), background="#ecf0f1")
instruccion.pack(pady=(10,30))

# Botones de cada grupo, Luego del bg= hay un cuadrado con color al apretarlo configuran el color del boton
b1 = tk.Button(root, text="Poligono 1", font=("Segoe UI", 14, "bold"), width=30, height=2,bg="#0550a7", fg="white",command=ventana_grupo_1)
b1.pack(pady=15)
b2 = tk.Button(root, text="Poligono 2", font=("Segoe UI", 14, "bold"), width=30, height=2,bg="#fdcb6e", fg="white",command=ventana_grupo_2)
b2.pack(pady=15)
b3 = tk.Button(root,text="Poligono 3",font=("Segoe UI", 14, "bold"),width=30, height=2, bg="#e17055", fg="white", command=ventana_grupo_3)
b3.pack(pady=15)

root.mainloop()