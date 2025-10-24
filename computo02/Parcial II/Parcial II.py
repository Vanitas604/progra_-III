import mysql.connector

class hola_mundo1:

    # CONEXIÓN A LA BASE DE DATOS
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hola_mundo1"
        )
        return conexion

    # INSERTAR REGISTRO
    def alta(self, datos):
        """
        datos = (StudentID, LastName, FirstName, Address, Phone)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """INSERT INTO empleados
                 (StudentID, LastName, FirstName, Address, Phone)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # CONSULTAR UN EMPLEADO POR ID
    def consulta(self, datos):
        """
        datos = (StudentID,)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """SELECT StudentID, LastName, FirstName, Address, Phone
                 FROM hola_mundo1
                 WHERE StudentID = %s"""
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        cone.close()
        return resultado

    # RECUPERAR TODOS LOS EMPLEADOS
    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """SELECT StudentID, LastName, FirstName, Address, Phone
                 FROM hola_mundo1"""
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cone.close()
        return resultados

    # ELIMINAR EMPLEADO
    def baja(self, datos):
        """
        datos = (StudentID,)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM hola_mundo1 WHERE StudentID = %s"
        cursor.execute(sql, datos)
        cone.commit()
        filas_borradas = cursor.rowcount
        cone.close()
        return filas_borradas

    # MODIFICACIÓN DATOS DE UN EMPLEADO
    def modificacion(self, datos):
        """
        datos = (StudentID, LastName, FirstName, Address, Phone)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE hola_mundo1
                 SET StudentID = %s,
                     LastName = %s,
                     FirstName = %s,
                     Address = %s,
                     Phone = %s
                 WHERE StudentID = %s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas_modificadas = cursor.rowcount
        cone.close()
        return filas_modificadas  # cantidad de filas modificadas
