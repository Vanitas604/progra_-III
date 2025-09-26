import tkinter as tk
from datetime import date


def calcular_edad():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        anio = int(entry_anio.get())

        nacimiento = date(anio, mes, dia)
        hoy = date.today()

        edad = hoy.year - nacimiento.year

        # Ajustar si no ha cumplido años este año
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

        label_resultado.config(
            text=f" Tienes {edad} años.",
            fg="blue"
        )
    except ValueError:
        label_resultado.config(
            text="Ingresa una fecha válida (números correctos).",
            fg="orange"
        )


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("350x300")
ventana.config(bg="#f0f0f0")

# Etiquetas y entradas
tk.Label(ventana, text="Día de nacimiento:", bg="#f0f0f0").pack(pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Mes de nacimiento:", bg="#f0f0f0").pack(pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.pack()

tk.Label(ventana, text="Año de nacimiento:", bg="#f0f0f0").pack(pady=5)
entry_anio = tk.Entry(ventana)
entry_anio.pack()

# Botón para calcular
tk.Button(
    ventana,
    text="Calcular Edad",
    command=calcular_edad,
    bg="#27ae60",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10, pady=5
).pack(pady=15)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_resultado.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
