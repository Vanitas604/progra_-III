import mysql.connector

conexion1=mysql.connector.connect(host="localhost",
                                  user= "root",
                                  passwd="" ,
                                  database="BD1")

cursor1=conexion1.cursor()
sql="insert artículos(descripcion, precio) values (%s,%s)"

datos=("Raton",3)
cursor1.execute(sql,datos)

datos=("Teclado",20)
cursor1.execute(sql,datos)

datos=("Monitor",150)
cursor1.execute(sql,datos)

datos=("Lentes 3D",50)
cursor1.execute(sql,datos)

datos=("USB 32 GB",15)
cursor1.execute(sql,datos)

datos=("Audifonos",30)
cursor1.execute(sql,datos)

datos=("RAM 8GB",40)
cursor1.execute(sql,datos)

conexion1.commit()
conexion1.close()
print("Se han guardado correctamente")