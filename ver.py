# Solución al “Challenge DEV #Caso Keyword en Gmail”

# El presente Código permite ingresar al servidor SQL online,
# y extraer la información de la base de datos creada en
# el archivo carga.py

import mysql.connector
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="JXdnd6btlM",
  password="G11pJ8nwLn",
  database="JXdnd6btlM",
  port="3306"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mails")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
