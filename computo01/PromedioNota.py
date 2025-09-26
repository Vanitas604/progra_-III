import tkinter as tk


def calcular_promedio():
    try:
        lab1 = float(entry_lab1.get())
        lab2 = float(entry_lab2.get())
        parcial = float(entry_parcial.get())

        promedio = (lab1 * 0.30) + (lab2 * 0.30) + (parcial * 0.40)

        if promedio >= 6:
            label_resultado.config(
                text=f"Tu promedio es: {promedio:.2f}\n Aprobaste el cómputo",
                fg="green"
            )
        else:
            label_resultado.config(
                text=f"Tu promedio es: {promedio:.2f}\n Reprobaste el cómputo",
                fg="red"
            )
    except ValueError:
        label_resultado.config(text="⚠️ Ingresa solo números válidos", fg="orange")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Promedio Cómputo 1")
ventana.geometry("350x300")
ventana.config(bg="#f0f0f0")

# Etiquetas y entradas
tk.Label(ventana, text="Nota Lab1 (30%):", bg="#f0f0f0").pack(pady=5)
entry_lab1 = tk.Entry(ventana)
entry_lab1.pack()

tk.Label(ventana, text="Nota Lab2 (30%):", bg="#f0f0f0").pack(pady=5)
entry_lab2 = tk.Entry(ventana)
entry_lab2.pack()

tk.Label(ventana, text="Nota Parcial (40%):", bg="#f0f0f0").pack(pady=5)
entry_parcial = tk.Entry(ventana)
entry_parcial.pack()

# Botón
tk.Button(
    ventana,
    text="Calcular Promedio",
    command=calcular_promedio,
    bg="#0077b6",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10, pady=5
).pack(pady=15)

# Resultado
label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_resultado.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
