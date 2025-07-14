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
    from tkinter import filedialog, messagebox, ttk
    import tkinter as tk
    import numpy as np

    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tipwindow = None
            widget.bind('<Enter>', self.show_tip)
            widget.bind('<Leave>', self.hide_tip)
        def show_tip(self, event=None):
            if self.tipwindow or not self.text:
                return
            x, y, _, _ = self.widget.bbox("insert") if self.widget.winfo_class() == 'Entry' else (0, 0, 0, 0)
            x = x + self.widget.winfo_rootx() + 25
            y = y + self.widget.winfo_rooty() + 20
            self.tipwindow = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry(f"+{x}+{y}")
            label = tk.Label(tw, text=self.text, background="#333", foreground="white",
                             relief="solid", borderwidth=1, font=("Segoe UI", 10, "bold"),
                             padx=8, pady=4)
            label.pack()
        def hide_tip(self, event=None):
            tw = self.tipwindow
            if tw:
                tw.destroy()
            self.tipwindow = None

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
            self.root.geometry("1200x780")
            self.root.configure(bg="#f7fafc")
            self.df = None
            self.filtered_df = None
            self.df_before_dupes = None
            self.vertex_entries = []
            self.axis_limits = None
            self.vertices_mouse = []
            self.cid = None
            self.create_widgets()

        def create_widgets(self):
            header = tk.Frame(self.root, bg="#0a3d62", height=70)
            header.pack(fill="x")
            title = tk.Label(header, text="Filtrado Inteligente de Nube de Puntos",
                             font=("Segoe UI", 26, "bold"), bg="#0a3d62", fg="#ffffff")
            title.pack(pady=14)
            main_frame = tk.Frame(self.root, bg="#f7fafc")
            main_frame.pack(fill="both", expand=True, padx=20, pady=10)
            panel = tk.LabelFrame(main_frame, text="Opciones de Filtrado", font=("Segoe UI", 14, "bold"),
                                  bg="#f7fafc", fg="#0a3d62", padx=16, pady=12, bd=2)
            panel.pack(side="left", fill="y", padx=10, pady=10)
            btn_import = ttk.Button(panel, text="Importar TXT", command=self.import_txt)
            btn_import.pack(fill="x", pady=8)
            ToolTip(btn_import, "Importa un archivo de puntos")
            vert_label = tk.Label(panel, text="Vértices del polígono (Norte, Este):", font=("Segoe UI", 12, "bold"),
                                  bg="#f7fafc", fg="#0a3d62")
            vert_label.pack(pady=8)
            verts_frame = tk.Frame(panel, bg="#f7fafc")
            verts_frame.pack()
            for i in range(4):
                box = tk.Frame(verts_frame, bg="#f7fafc")
                box.pack(side="left", padx=5)
                tk.Label(box, text=f"V{i+1} N:", font=("Segoe UI", 11), bg="#f7fafc").pack()
                entry_n = ttk.Entry(box, width=7)
                entry_n.pack()
                tk.Label(box, text="E:", font=("Segoe UI", 11), bg="#f7fafc").pack()
                entry_e = ttk.Entry(box, width=7)
                entry_e.pack()
                self.vertex_entries.append((entry_n, entry_e))
            btn_vertices_mouse = ttk.Button(panel, text="Elegir vértices con mouse", command=self.elegir_vertices_mouse)
            btn_vertices_mouse.pack(fill="x", pady=5)
            ToolTip(btn_vertices_mouse, "Haz clic izquierdo para agregar vértices, derecho para borrar el último")
            btn_reset_poly = ttk.Button(panel, text="Reset Polígono", command=self.reset_poligono)
            btn_reset_poly.pack(fill="x", pady=5)
            ToolTip(btn_reset_poly, "Borra todos los vértices puestos con el mouse y limpia el polígono")
            btn_filter = ttk.Button(panel, text="Filtrar por Polígono", command=self.filtrar_puntos)
            btn_filter.pack(fill="x", pady=12)
            ToolTip(btn_filter, "Filtra los puntos dentro del polígono")
            btn_export = ttk.Button(panel, text="Exportar TXT", command=self.export_txt)
            btn_export.pack(fill="x", pady=5)
            ToolTip(btn_export, "Exporta los puntos filtrados")
            btn_reset = ttk.Button(panel, text="Reset", command=self.reset_all)
            btn_reset.pack(fill="x", pady=5)
            ToolTip(btn_reset, "Limpiar todos los datos y vértices")
            self.btn_undo = ttk.Button(panel, text="Deshacer duplicados", command=self.undo_duplicates)
            self.btn_undo.pack(fill="x", pady=2)
            self.btn_undo.pack_forget()
            ToolTip(self.btn_undo, "Restaurar datos antes de eliminar duplicados")
            info_frame = tk.Frame(panel, bg="#f7fafc")
            info_frame.pack(fill="x", pady=8)
            self.label_total = tk.Label(info_frame, text="Total points: 0", font=("Segoe UI", 12), bg="#f7fafc", fg="#2c3e50")
            self.label_total.pack()
            self.label_filtered = tk.Label(info_frame, text="Filtered points: 0", font=("Segoe UI", 12), bg="#f7fafc", fg="#2c3e50")
            self.label_filtered.pack()
            graph_frame = tk.LabelFrame(main_frame, text="Vista gráfica", font=("Segoe UI", 14, "bold"),
                                       bg="#f7fafc", fg="#0a3d62", padx=12, pady=12, bd=2)
            graph_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
            self.figure, self.ax = plt.subplots(figsize=(9, 7))
            self.figure.patch.set_facecolor("#f7fafc")
            self.ax.set_facecolor("#f7fafc")
            self.canvas = FigureCanvasTkAgg(self.figure, master=graph_frame)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)

        def detectar_duplicados(self):
            if self.df is None:
                return
            duplicados = self.df.duplicated()
            cantidad = duplicados.sum()
            if cantidad > 0:
                respuesta = messagebox.askyesno("Puntos duplicados", f"Se detectaron {cantidad} puntos duplicados.\n¿Deseas eliminarlos?")
                if respuesta:
                    self.df = self.df.drop_duplicates().reset_index(drop=True)
                    messagebox.showinfo("Limpieza completada", f"Se eliminaron {cantidad} duplicados.")
                else:
                    messagebox.showinfo("Aviso", "Los duplicados se han conservado")
#Importacion de datos: archivos NEZD/ENZD con 3 o 4 columnas
        def import_txt(self):
            file_path = filedialog.askopenfilename(filetypes=[("Archivos de TXT/CSV/Excel", "*.txt *.csv *.xlxs")])
            if not file_path:
                return

            formato = tk.StringVar()
            def seleccionar_formato():
                ventana.destroy()

            ventana = tk.Toplevel(self.root)
            ventana.title("Seleccionar formato de archivo")
            ventana.geometry("400x300")
            ventana.grab_set()
            tk.Label(ventana, text="¿Qué formato tiene el archivo?", font=("Segoe UI", 12)).pack(pady=20)
            formatos = [
                ("PNEZD (Punto, Norte, Este, Cota, Descripción)", "PNEZD"),
                ("PENZD (Punto, Este, Norte, Cota, Descripción)", "PENZD"),
                ("ENZD (Este, Norte, Cota, Descripción)", "ENZD"),
                ("NEZD (Norte, Este, Cota, Descripción)", "NEZD"),
            ]
            for texto, valor in formatos:
                tk.Radiobutton(ventana, text=texto, variable=formato, value=valor, font=("Segoe UI", 11)).pack(anchor="w", padx=20)
            tk.Button(ventana, text="Aceptar", command=seleccionar_formato, bg="#00b894", fg="white").pack(pady=10)
            ventana.wait_window()

            if not formato.get():
                return

            try:
                # Detectar delimitador automáticamente (soporta coma, punto y coma, espacio)
                with open(file_path, "r", encoding="utf-8") as f:
                    first_line = f.readline()
                if "," in first_line:
                    sep = ","
                elif ";" in first_line:
                    sep = ";"
                elif " " in first_line:
                    sep = " "
                else:
                    sep = ","  # fallback

                # Definir nombres de columnas según formato (sin encabezado en archivo)
                if formato.get() in ["PNEZD", "PENZD"]:
                    columnas = ["Punto", "A", "B", "Z", "Descripción"]
                else:
                    columnas = ["A", "B", "Z", "Descripción"]

                df = pd.read_csv(file_path, sep=sep, header=None, names=columnas, dtype=str)
                # Asignar X/Y según formato
                if formato.get() == "PNEZD":
                    df.rename(columns={"A": "Y", "B": "X"}, inplace=True)
                elif formato.get() == "PENZD":
                    df.rename(columns={"A": "X", "B": "Y"}, inplace=True)
                elif formato.get() == "ENZD":
                    df.rename(columns={"A": "X", "B": "Y"}, inplace=True)
                elif formato.get() == "NEZD":
                    df.rename(columns={"A": "Y", "B": "X"}, inplace=True)

                # Convertir X, Y, Z a float, Descripción como texto (puede haber vacíos)
                for col in ["X", "Y", "Z"]:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                if "Descripción" in df.columns:
                    df["Descripción"] = df["Descripción"].fillna("").astype(str)

                columnas_validas = ["X", "Y", "Z"]
                if "Descripción" in df.columns and not df["Descripción"].isnull().all() and not (df["Descripción"] == "").all():
                    columnas_validas.append("Descripción")
                self.df = df[columnas_validas].dropna(subset=["X", "Y", "Z"])
                self.filtered_df = None

                self.detectar_duplicados()
                self.plot_points(self.df)
                self.axis_limits = self.get_axis_limits(self.df)
                self.label_total.config(text=f"Total points: {len(self.df)}")
                self.label_filtered.config(text="Filtered points: 0")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")

        def filtrar_puntos(self):
            # Si se usaron vértices por mouse válidos, usa esos
            if self.vertices_mouse and len(self.vertices_mouse) >= 3:
                poly = self.vertices_mouse
                # Desconecta el evento para evitar seguir agregando vértices al hacer click
                if self.cid:
                    self.canvas.mpl_disconnect(self.cid)
                    self.cid = None
                self.vertices_mouse = []
            else:
                # Usa los entrys manuales
                poly = []
                for i, (entry_n, entry_e) in enumerate(self.vertex_entries):
                    try:
                        n = float(entry_n.get())
                        e = float(entry_e.get())
                        poly.append((e, n))
                    except ValueError:
                        continue
                if len(poly) < 3:
                    messagebox.showerror("Error", "Debes ingresar al menos 3 vértices para definir el polígono.")
                    return
            mask = [point_in_polygon(x, y, poly) for x, y in zip(self.df["X"], self.df["Y"])]
            self.filtered_df = self.df[mask]
            self.plot_points(self.filtered_df, poly, title="Puntos dentro del polígono definido", keep_limits=True)
            self.label_filtered.config(text=f"Filtered points: {len(self.filtered_df)}")
 

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