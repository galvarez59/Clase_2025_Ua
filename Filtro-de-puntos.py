import tkinter as tk
from tkinter import ttk

# ============================
# ===   VENTANA GRUPO 1    ===
# ============================
def ventana_grupo_1():
    win = tk.Toplevel(root)
    win.title("Poligono 1")
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
    import pandas as pd
    import matplotlib.pyplot as plt 
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from tkinter import filedialog, messagebox
    import tkinter as tk

    def point_in_polygon(x, y, polygon):
        n = len(polygon)
        inside = False
        px, py = x, y
        for i in range(n):
            xi, yi = polygon[i]
            xj, yj = polygon[(i + 1) % n]
            if ((yi > py) != (yj > py)) and \
               (px < (xj - xi) * (py - yi) / ((yj - yi) + 1e-10) + xi):
                inside = not inside
        return inside

    class PointFilterApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Filtrado de Nube de Puntos (X, Y, Z)")
            self.root.geometry("1150x750")
            self.root.configure(bg="#ecf0f1")

            self.df = None
            self.filtered_df = None
            self.vertex_entries = []
            self.axis_limits = None

            self.create_widgets()

        def create_widgets(self):
            title = tk.Label(self.root, text="Filtrado Inteligente de Nube de Puntos",
                             font=("Segoe UI", 22, "bold"), bg="#ecf0f1", fg="#2c3e50")
            title.pack(pady=10)

            frame_controls = tk.Frame(self.root, bg="#dfe6e9")
            frame_controls.pack(pady=10)

            self.label_total = tk.Label(self.root, text="Total points: 0", font=("Segoe UI", 12), bg="#ecf0f1", fg="#2c3e50")
            self.label_total.pack()

            self.label_filtered = tk.Label(self.root, text="Filtered points: 0", font=("Segoe UI", 12), bg="#ecf0f1", fg="#2c3e50")
            self.label_filtered.pack()

            btn_import = tk.Button(frame_controls, text="Importar TXT", font=("Segoe UI", 12),
                                   command=self.import_txt, bg="#0984e3", fg="white")
            btn_import.grid(row=0, column=0, padx=10, pady=5)

            tk.Label(frame_controls, text="Vértices del polígono (Norte, Este):", font=("Segoe UI", 12, "bold"), bg="#dfe6e9").grid(row=1, column=0, pady=10)
            for i in range(4):
                tk.Label(frame_controls, text=f"V{i+1} Norte:", font=("Segoe UI", 11), bg="#dfe6e9").grid(row=1, column=1 + i*2)
                entry_n = tk.Entry(frame_controls, width=8)
                entry_n.grid(row=1, column=2 + i*2)
                tk.Label(frame_controls, text=f"Este:", font=("Segoe UI", 11), bg="#dfe6e9").grid(row=2, column=1 + i*2)
                entry_e = tk.Entry(frame_controls, width=8)
                entry_e.grid(row=2, column=2 + i*2)
                self.vertex_entries.append((entry_n, entry_e))

            btn_filter = tk.Button(frame_controls, text="Filtrar por Polígono", font=("Segoe UI", 12),
                                   command=self.filtrar_puntos, bg="#00b894", fg="white")
            btn_filter.grid(row=1, column=9, padx=10, pady=5, rowspan=2)

            btn_export = tk.Button(frame_controls, text="Exportar TXT", font=("Segoe UI", 12),
                                   command=self.export_txt, bg="#6c5ce7", fg="white")
            btn_export.grid(row=1, column=10, padx=10, pady=5, rowspan=2)

            self.figure, self.ax = plt.subplots(figsize=(8, 6))
            self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
            self.canvas.get_tk_widget().pack(pady=10)


    win2 = tk.Toplevel()
    app = PointFilterApp(win2)


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