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
    def seleccionar_archivo():
        arch = filedialog.askopenfilename(filetypes=[("TXT/CSV", "*.txt *.csv")])
        if arch:
            archivo_path_var.set(arch)

    btn_buscar_archivo = tk.Button(entrada_archivo_frame, text="📂 Seleccionar archivo", font=("Montserrat", 14), bg="#fffbe7", fg="#a76d60",
                                   activebackground="#f4b393", activeforeground="#fffbe7", relief="raised", bd=2, command=seleccionar_archivo)
    btn_buscar_archivo.pack(pady=8, padx=10)

    btn_importar = tk.Button(panel_controles, text="Cargar archivo", font=("Montserrat", 16), bg="#fffbe7", fg="#a76d60",
                             activebackground="#f4b393", activeforeground="#fffbe7", relief="raised", bd=2, command=lambda: importar())
    btn_importar.pack(pady=8, padx=70, fill="x")

    btn_exportar = tk.Button(panel_controles, text="💾 Exportar", font=("Montserrat", 16), bg="#fffbe7", fg="#a76d60",
                             activebackground="#f4b393", activeforeground="#fffbe7", relief="raised", bd=2, command=lambda: exportar())
    btn_exportar.pack(pady=8, padx=70, fill="x")

    sep2 = tk.Frame(panel_controles, height=3, bg="#a76d60")
    sep2.pack(fill="x", padx=44, pady=16)

    tk.Label(panel_controles, text="Vértices del área (X, Y)", font=("Montserrat", 17, "bold"), bg="#f8e9a1", fg="#272e36").pack(pady=10)
    verts_entries = []
    verts_frame = tk.Frame(panel_controles, bg="#f8e9a1")
    verts_frame.pack(pady=3)
    for i in range(4):
        fila = tk.Frame(verts_frame, bg="#f8e9a1")
        fila.pack(pady=5)
        tk.Label(fila, text=f"X{i+1}:", font=("Montserrat", 14), bg="#f8e9a1", fg="#a76d60").pack(side="left")
        entry_x = ttk.Entry(fila, width=9, font=("Consolas", 13))
        entry_x.pack(side="left", padx=3)
        tk.Label(fila, text="Y:", font=("Montserrat", 14), bg="#f8e9a1", fg="#a76d60").pack(side="left")
        entry_y = ttk.Entry(fila, width=9, font=("Consolas", 13))
        entry_y.pack(side="left")
        verts_entries.append((entry_x, entry_y))

    btn_filtrar = tk.Button(panel_controles, text="🎯 Filtrar", font=("Montserrat", 16, "bold"), bg="#a76d60", fg="#fffbe7",
                            activebackground="#f4b393", activeforeground="#272e36", relief="raised", bd=3, command=lambda: filtrar_area())
    btn_filtrar.pack(pady=30, padx=80, fill="x")
#Funciones internas
    def importar():
        nonlocal df, df_filtrada, limites
        archivo = archivo_path_var.get()
        if not archivo or not os.path.isfile(archivo):
            messagebox.showwarning("Aviso", "Selecciona primero un archivo válido (usa el botón).")
            return

        formatos = [
            ("PNEZD (Y, X, Z, Descripción)", "PNEZD"),
            ("PENZD (X, Y, Z, Descripción)", "PENZD"),
            ("ENZD (X, Y, Z, Descripción)", "ENZD"),
            ("NEZD (Y, X, Z, Descripción)", "NEZD"),
        ]
        formato_var = tk.StringVar()
        formato_var.set(formatos[0][1])
        win_form = tk.Toplevel(win)
        win_form.title("Formato de archivo")
        win_form.geometry("440x210")
        win_form.configure(bg="#68b0ab")

        selected_format_holder = {"value": None}

        tk.Label(win_form, text="Tipo de archivo/orden de columnas:", font=("Montserrat", 15), bg="#68b0ab", fg="#fffbe7").pack(pady=14)
        formato_combo = ttk.Combobox(win_form, values=[f[0] for f in formatos], font=("Montserrat", 13), state="readonly")
        formato_combo.current(0)
        formato_combo.pack(pady=8)

        def aceptar():
            selected_format_holder["value"] = formato_combo.get()
            win_form.destroy()

        ttk.Button(win_form, text="Aceptar", command=aceptar).pack(pady=18)
        win_form.wait_window()

        seleccionado = selected_format_holder["value"]
        if not seleccionado:
            return
        formato_real = [f[1] for f in formatos if f[0] == seleccionado][0] if seleccionado else formatos[0][1]

        try:
            with open(archivo, "r", encoding="utf-8") as f:
                linea = f.readline()
            sep = ","
            if ";" in linea: sep = ";"
            elif " " in linea: sep = " "

            if formato_real == "PNEZD":
                columnas = ["Y", "X", "Z", "Descripción"]
            elif formato_real == "PENZD":
                columnas = ["X", "Y", "Z", "Descripción"]
            elif formato_real == "ENZD":
                columnas = ["X", "Y", "Z", "Descripción"]
            elif formato_real == "NEZD":
                columnas = ["Y", "X", "Z", "Descripción"]
            else:
                columnas = ["X", "Y", "Z", "Descripción"]
            df_archivo = pd.read_csv(archivo, sep=sep, header=None, names=columnas, dtype=str)
            for col in ["X", "Y", "Z"]:
                df_archivo[col] = pd.to_numeric(df_archivo[col], errors="coerce")
            if "Descripción" in df_archivo.columns:
                df_archivo["Descripción"] = df_archivo["Descripción"].fillna("").astype(str)
            columnas_finales = ["X", "Y", "Z"]
            if "Descripción" in df_archivo.columns and not df_archivo["Descripción"].isnull().all() and not (df_archivo["Descripción"] == "").all():
                columnas_finales.append("Descripción")
            df = df_archivo[columnas_finales].dropna(subset=["X", "Y", "Z"])
            df_filtrada = None
            dibujar(df)
            limites = calcular_limites(df)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo importar:\n{e}")
            def filtrar_area():
             nonlocal df, df_filtrada
        if df is None:
            messagebox.showwarning("Aviso", "Primero importa datos.")
            return
        area = []
        for i, (entry_x, entry_y) in enumerate(verts_entries):
            try:
                x = float(entry_x.get())
                y = float(entry_y.get())
                area.append((x, y))
            except ValueError:
                messagebox.showerror("Error", f"Vértice {i+1} inválido.")
                return
        if len(area) < 3:
            messagebox.showerror("Error", "Debes ingresar mínimo 3 vértices.")
            return
        mask = [punto_en_poligono_angulo(x, y, area) for x, y in zip(df["X"], df["Y"])]
        df_filtrada = df[mask]
        dibujar(df_filtrada, area, "Área seleccionada", mantener_limites=True)

    def exportar():
        nonlocal df, df_filtrada
        if df is None:
            messagebox.showwarning("Aviso", "No hay datos para exportar.")
            return
        datos = df_filtrada if df_filtrada is not None else df
        datos = datos.dropna(subset=["X", "Y", "Z"])
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("TXT", "*.txt")])
        if not archivo:
            return
        try:
            extra = "Descripción" if "Descripción" in datos.columns and not (datos["Descripción"] == "").all() else None
            cols = ["Id", "X", "Y", "Z"]
            datos_out = {
                "Id": range(1, len(datos) + 1),
                "X": datos["X"].astype(float),
                "Y": datos["Y"].astype(float),
                "Z": datos["Z"].astype(float),
            }
            if extra:
                cols.append("Descripción")
                datos_out["Descripción"] = datos[extra].fillna("")
            df_final = pd.DataFrame(datos_out)[cols]
            df_final.to_csv(archivo, sep=",", index=False, header=False, float_format='%.3f')
            messagebox.showinfo("Exportación", f"Archivo guardado en:\n{archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar:\n{e}")

    def calcular_limites(df_local):
        min_x, max_x = df_local["X"].min(), df_local["X"].max()
        min_y, max_y = df_local["Y"].min(), df_local["Y"].max()
        rango_x = max_x - min_x
        rango_y = max_y - min_y
        centro_x = (max_x + min_x) / 2
        centro_y = (max_y + min_y) / 2
        lado = max(rango_x, rango_y) * 1.13
        xlim = (centro_x - lado / 2, centro_x + lado / 2)
        ylim = (centro_y - lado / 2, centro_y + lado / 2)
        return xlim, ylim

    def dibujar(df_local, area=None, titulo="Puntos", mantener_limites=False):
        ax.clear()
        # GRILLA SIEMPRE VISIBLE Y DESTACADA
        ax.grid(True, linestyle="--", color="#a3a3a3", alpha=0.7, linewidth=1.0)
        ax.set_axisbelow(True)
        ax.set_aspect('equal', adjustable='box')
        if df_local is not None and not df_local.empty:
            ax.scatter(df_local["X"], df_local["Y"], s=38, alpha=0.92, c="#f76c6c", edgecolors="#383838", linewidths=1.7, zorder=3)
        if area is not None and len(area) >= 3:
            xs, ys = zip(*area)
            ax.plot(list(xs) + [xs[0]], list(ys) + [ys[0]], color="#68b0ab", linewidth=4, zorder=7, label="Área")
            ax.legend()
        ax.set_title(titulo, fontsize=18, fontweight="bold", color="#f76c6c")
        ax.set_xlabel("X", fontsize=15, color="#272e36")
        ax.set_ylabel("Y", fontsize=15, color="#272e36")

        if area is not None and len(area) >= 3:
            puntos_x = list(df_local["X"]) if df_local is not None and not df_local.empty else []
            puntos_y = list(df_local["Y"]) if df_local is not None and not df_local.empty else []
            poligono_x = [xy[0] for xy in area]
            poligono_y = [xy[1] for xy in area]
            todos_x = puntos_x + poligono_x
            todos_y = puntos_y + poligono_y
            min_x, max_x = min(todos_x), max(todos_x)
            min_y, max_y = min(todos_y), max(todos_y)
            rango_x = max_x - min_x
            rango_y = max_y - min_y
            padding = max(rango_x, rango_y) * 0.12 if max(rango_x, rango_y) > 0 else 1
            ax.set_xlim(min_x - padding, max_x + padding)
            ax.set_ylim(min_y - padding, max_y + padding)
        elif mantener_limites and limites is not None:
            xlim, ylim = limites
            ax.set_xlim(*xlim)
            ax.set_ylim(*ylim)
        elif df_local is not None and not df_local.empty:
            xlim, ylim = calcular_limites(df_local)
            ax.set_xlim(*xlim)
            ax.set_ylim(*ylim)
        canvas.draw()






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