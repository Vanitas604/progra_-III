import tkinter as tk
from tkinter import ttk, messagebox as mb, scrolledtext as st
import mysql.connector


class AlumnosBD:
    # CONEXIÓN A LA BASE DE DATOS
    def abrir(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hola_mundo1"  # Nombre de tu base de datos
        )

    # INSERTAR REGISTRO
    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """INSERT INTO alumnos (StudentID, LastName, FirstName, Address, Phone)
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # CONSULTAR REGISTRO POR ID
    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT * FROM alumnos WHERE StudentID = %s"
        cursor.execute(sql, datos)
        registros = cursor.fetchall()
        cone.close()
        return registros

    # MODIFICAR REGISTRO
    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE alumnos
                 SET LastName = %s,
                     FirstName = %s,
                     Address = %s,
                     Phone = %s
                 WHERE StudentID = %s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # ELIMINAR REGISTRO
    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM alumnos WHERE StudentID = %s"
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # MOSTRAR TODOS LOS REGISTROS
    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM alumnos")
        registros = cursor.fetchall()
        cone.close()
        return registros


class FormularioAlumnos:
    def __init__(self):
        self.emp = AlumnosBD()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Alumnos")
        self.ventana.geometry("800x600")
        self.ventana.configure(bg="#F0F4F8")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.pack(fill="both", expand=True)

        # Pestañas
        self.frame_alta = ttk.Frame(self.cuaderno)
        self.frame_consulta = ttk.Frame(self.cuaderno)
        self.frame_modificacion = ttk.Frame(self.cuaderno)
        self.frame_baja = ttk.Frame(self.cuaderno)
        self.frame_listado = ttk.Frame(self.cuaderno)

        self.cuaderno.add(self.frame_alta, text="Registrar Alumno")
        self.cuaderno.add(self.frame_consulta, text="Consultar Alumno")
        self.cuaderno.add(self.frame_modificacion, text="Modificar Alumno")
        self.cuaderno.add(self.frame_baja, text="Eliminar Alumno")
        self.cuaderno.add(self.frame_listado, text="Listado General de Alumnos")

        self.form_alta()
        self.form_consulta()
        self.form_modificacion()
        self.form_baja()
        self.form_listado()

        self.ventana.mainloop()

    # FORMULARIO DE ALTA
    def form_alta(self):
        self.studentid = tk.StringVar()
        self.lastname = tk.StringVar()
        self.firstname = tk.StringVar()
        self.address = tk.StringVar()
        self.phone = tk.StringVar()

        ttk.Label(self.frame_alta, text="StudentID:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.studentid).grid(column=1, row=0)

        ttk.Label(self.frame_alta, text="LastName:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.lastname).grid(column=1, row=1)

        ttk.Label(self.frame_alta, text="FirstName:").grid(column=0, row=2, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.firstname).grid(column=1, row=2)

        ttk.Label(self.frame_alta, text="Address:").grid(column=0, row=3, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.address).grid(column=1, row=3)

        ttk.Label(self.frame_alta, text="Phone:").grid(column=0, row=4, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.phone).grid(column=1, row=4)

        ttk.Button(self.frame_alta, text="Registrar", command=self.agregar_alumno).grid(column=1, row=5, pady=15)

    def agregar_alumno(self):
        datos = (
            self.studentid.get().strip(),
            self.lastname.get().strip(),
            self.firstname.get().strip(),
            self.address.get().strip(),
            self.phone.get().strip()
        )

        if any(campo == "" for campo in datos):
            mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return

        try:
            self.emp.alta(datos)
            mb.showinfo("Éxito", "Alumno registrado correctamente.")
            self.limpiar_formulario_alta()
        except Exception as e:
            mb.showerror("Error", f"No se pudo registrar el Alumno.\n{e}")

    def limpiar_formulario_alta(self):
        self.studentid.set("")
        self.lastname.set("")
        self.firstname.set("")
        self.address.set("")
        self.phone.set("")

    # FORMULARIO DE CONSULTA
    def form_consulta(self):
        self.id_consulta = tk.StringVar()

        ttk.Label(self.frame_consulta, text="StudentID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_consulta, textvariable=self.id_consulta).grid(column=1, row=0)
        ttk.Button(self.frame_consulta, text="Consultar", command=self.consultar_alumno).grid(column=1, row=1, pady=10)

        self.txt_resultado = st.ScrolledText(self.frame_consulta, width=60, height=15)
        self.txt_resultado.grid(column=0, row=2, columnspan=2, pady=10)

    def consultar_alumno(self):
        datos = (self.id_consulta.get(),)
        registros = self.emp.consulta(datos)
        self.txt_resultado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_resultado.insert(
                    tk.END,
                    f"ID: {fila[0]}\nApellido: {fila[1]}\nNombre: {fila[2]}\nDirección: {fila[3]}\nTeléfono: {fila[4]}\n\n"
                )
        else:
            mb.showinfo("Sin resultados", "No se encontró ningún alumno con ese ID.")
        self.id_consulta.set("")

    # FORMULARIO DE MODIFICACIÓN
    def form_modificacion(self):
        self.studentid_mod = tk.StringVar()
        self.lastname_mod = tk.StringVar()
        self.firstname_mod = tk.StringVar()
        self.address_mod = tk.StringVar()
        self.phone_mod = tk.StringVar()

        etiquetas = ["StudentID:", "LastName:", "FirstName:", "Address:", "Phone:"]
        for i, texto in enumerate(etiquetas):
            ttk.Label(self.frame_modificacion, text=texto).grid(column=0, row=i, padx=10, pady=10, sticky="w")

        ttk.Entry(self.frame_modificacion, textvariable=self.studentid_mod).grid(column=1, row=0)
        ttk.Entry(self.frame_modificacion, textvariable=self.lastname_mod).grid(column=1, row=1)
        ttk.Entry(self.frame_modificacion, textvariable=self.firstname_mod).grid(column=1, row=2)
        ttk.Entry(self.frame_modificacion, textvariable=self.address_mod).grid(column=1, row=3)
        ttk.Entry(self.frame_modificacion, textvariable=self.phone_mod).grid(column=1, row=4)

        ttk.Button(self.frame_modificacion, text="Modificar", command=self.modificar_alumno).grid(column=1, row=5, pady=15)

    def modificar_alumno(self):
        datos = (
            self.lastname_mod.get(),
            self.firstname_mod.get(),
            self.address_mod.get(),
            self.phone_mod.get(),
            self.studentid_mod.get()
        )
        try:
            filas = self.emp.modificacion(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Alumno modificado correctamente.")
                self.limpiar_formulario_mod()
            else:
                mb.showwarning("Aviso", "No se encontró el Alumno con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo modificar el Alumno.\n{e}")

    def limpiar_formulario_mod(self):
        self.studentid_mod.set("")
        self.lastname_mod.set("")
        self.firstname_mod.set("")
        self.address_mod.set("")
        self.phone_mod.set("")

    # FORMULARIO DE BAJA
    def form_baja(self):
        self.id_baja = tk.StringVar()
        ttk.Label(self.frame_baja, text="StudentID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_baja, textvariable=self.id_baja).grid(column=1, row=0)
        ttk.Button(self.frame_baja, text="Eliminar", command=self.eliminar_alumno).grid(column=1, row=1, pady=10)

    def eliminar_alumno(self):
        datos = (self.id_baja.get(),)
        try:
            filas = self.emp.baja(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Alumno eliminado correctamente.")
                self.id_baja.set("")
            else:
                mb.showwarning("Aviso", "No se encontró ningún Alumno con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo eliminar el Alumno.\n{e}")

    # LISTADO GENERAL
    def form_listado(self):
        ttk.Button(self.frame_listado, text="Actualizar Listado", command=self.mostrar_todos).pack(pady=10)
        self.txt_listado = st.ScrolledText(self.frame_listado, width=80, height=25)
        self.txt_listado.pack(pady=10)

    def mostrar_todos(self):
        registros = self.emp.recuperar_todos()
        self.txt_listado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_listado.insert(
                    tk.END,
                    f"ID: {fila[0]} | Apellido: {fila[1]} | Nombre: {fila[2]} | Dirección: {fila[3]} | Teléfono: {fila[4]}\n{'-'*80}\n"
                )
        else:
            self.txt_listado.insert(tk.END, "No hay Alumnos registrados.\n")


if __name__ == "__main__":
    FormularioAlumnos()