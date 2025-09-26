import mysql.connector

# Conexión a la base de datos
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="BD1"
)

cursor1 = conexion1.cursor()

# ==== MOSTRAR DATOS ====
cursor1.execute("SELECT id, descripcion, precio FROM artículos")
print("Registros antes de modificar:")
for datos in cursor1:
    print(datos)

# ==== MODIFICAR REGISTRO ====
# Cambiar precio y descripción de un artículo con (id) específico
nuevo_precio = 8
nueva_descripcion = "Telefono"
id_modificar = 14

cursor1.execute(
    "UPDATE artículos SET precio=%s, descripcion=%s WHERE id=%s",
    (nuevo_precio, nueva_descripcion, id_modificar)
)
conexion1.commit()  # Guardar cambios en la BD

# Verificar si realmente se modificó
if cursor1.rowcount > 0:
    print(f"Registro con id={id_modificar} fue modificado.")
else:
    print(f"No se encontró ningún registro con id={id_modificar}.")

# ==== MOSTRAR DATOS DESPUÉS DE MODIFICAR ====
cursor1.execute("SELECT id, descripcion, precio FROM artículos")
print("Registros después de modificar:")
for datos in cursor1:
    print(datos)

# Cerrar conexión
conexion1.close()
print("Modificación Exitosa")