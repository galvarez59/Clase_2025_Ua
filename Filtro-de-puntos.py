import tkinter as tk
from tkinter import ttk

# ============================
# ===   VENTANA GRUPO 1    ===
# ============================
def ventana_grupo_1():
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    # Algoritmo: winding number
    def punto_en_area(x, y, area):
        wn = 0
        for i in range(len(area)):
            x0, y0 = area[i]
            x1, y1 = area[(i + 1) % len(area)]
            if y0 <= y:
                if y1 > y and _is_left(x0, y0, x1, y1, x, y) > 0:
                    wn += 1
            else:
                if y1 <= y and _is_left(x0, y0, x1, y1, x, y) < 0:
                    wn -= 1
        return wn != 0 
    
    def _is_left(x0, y0, x1, y1, px, py):
        return (x1 - x0)*(py - y0) - (px - x0)*(y1 - y0)

    class AreaUI:
        def __init__(self, master):
            self.master = master
            master.title("Filtrado por Región - Grupo 1")
            master.geometry("1100x820")
            master.configure(bg="#f7f9fa")

            self.df = None
            self.df_filtrada = None
            self.limites = None

            self._crear_panel_lateral()
            self._crear_panel_grafico()

        def _crear_panel_lateral(self):
            self.panel = tk.Frame(self.master, bg="#d6eaf8", width=320)
            self.panel.pack(side="left", fill="y")
            self.panel.pack_propagate(False)

            tk.Label(self.panel, text="Región de Puntos", font=("Segoe UI", 21, "bold"), bg="#d6eaf8", fg="#1b4f72").pack(pady=28)

            self.btn_cargar = ttk.Button(self.panel, text="Importar archivo", command=self._importar)
            self.btn_cargar.pack(pady=10, padx=35, fill="x")

            self.btn_exportar = ttk.Button(self.panel, text="Exportar TXT", command=self._exportar)
            self.btn_exportar.pack(pady=6, padx=35, fill="x")

            ttk.Separator(self.panel).pack(fill="x", pady=18)

            tk.Label(self.panel, text="Vértices área (Y, X):", font=("Segoe UI", 14), bg="#d6eaf8", fg="#1b4f72").pack(pady=11)
            self.verts_frame = tk.Frame(self.panel, bg="#d6eaf8")
            self.verts_frame.pack(pady=6)

            self.entrada_vertices = []
            for i in range(4):
                fila = tk.Frame(self.verts_frame, bg="#d6eaf8")
                fila.pack(pady=2)
                tk.Label(fila, text=f"Y{i+1}:", font=("Segoe UI", 11), bg="#d6eaf8").pack(side="left")
                e_y = ttk.Entry(fila, width=7)
                e_y.pack(side="left", padx=2)
                tk.Label(fila, text="X:", font=("Segoe UI", 11), bg="#d6eaf8").pack(side="left")
                e_x = ttk.Entry(fila, width=7)
                e_x.pack(side="left")
                self.entrada_vertices.append((e_y, e_x))

            self.btn_filtrar = ttk.Button(self.panel, text="Filtrar área", command=self._filtrar)
            self.btn_filtrar.pack(pady=18, padx=35, fill="x")

        def _crear_panel_grafico(self):
            self.frame_grafico = tk.Frame(self.master, bg="#f7f9fa")
            self.frame_grafico.pack(side="right", expand=True, fill="both")
            self.figura, self.ax = plt.subplots(figsize=(8, 8))
            self.ax.set_facecolor("#f7f9fa")
            self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_grafico)
            self.canvas.get_tk_widget().pack(expand=True, fill="both", pady=20)
            
        def _importar(self):
            archivo = filedialog.askopenfilename(filetypes=[("Archivos TXT/CSV", "*.txt *.csv")])
            if not archivo:
                return

            formato = tk.StringVar()
            def aceptar():
                ventana.destroy()
            ventana = tk.Toplevel(self.master)
            ventana.title("Formato de archivo")
            ventana.geometry("380x210")
            ventana.grab_set()
            tk.Label(ventana, text="¿Formato de archivo?", font=("Segoe UI", 12)).pack(pady=14)
            formatos = [
                ("PNEZD", "PNEZD"),
                ("PENZD", "PENZD"),
                ("ENZD", "ENZD"),
                ("NEZD", "NEZD"),
            ]
            for txt, val in formatos:
                ttk.Radiobutton(ventana, text=txt, variable=formato, value=val).pack(anchor="w", padx=20)
            ttk.Button(ventana, text="Aceptar", command=aceptar).pack(pady=9)
            ventana.wait_window()
            if not formato.get():
                return

            try:
                with open(archivo, "r", encoding="utf-8") as f:
                    primera = f.readline()
                if "," in primera:
                    sep = ","
                elif ";" in primera:
                    sep = ";"
                elif " " in primera:
                    sep = " "
                else:
                    sep = ","

                # Nombres de columnas
                if formato.get() in ["PNEZD", "PENZD"]:
                    columnas = ["Id", "A", "B", "Z", "Extra"]
                else:
                    columnas = ["A", "B", "Z", "Extra"]
                df = pd.read_csv(archivo, sep=sep, header=None, names=columnas, dtype=str)
    # -------------- INSTRUCCIONES GRUPO 1 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

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
    win = tk.Toplevel(root)
    win.title("Poligono 3")
    win.geometry("400x250")
    label = ttk.Label(win, text="Poly_3\nAgrega aquí tu código de filtrado", font=("Segoe UI", 14))
    label.pack(pady=50)
    # -------------- INSTRUCCIONES GRUPO 3 --------------
    # Aquí pueden importar librerías, crear clases, funciones y widgets
    # Ejemplo: crear una interfaz propia, botones, canvas, etc.
    # Pueden eliminar el label anterior cuando agreguen su interfaz.
    # ---------------------------------------------------

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