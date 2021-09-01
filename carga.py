# Solución al “Challenge DEV #Caso Keyword en Gmail”

# El presente Código importa la función del archivo inicial,
# crea una base de datos de SQL con ciertos datos requeridos
# la cual estará alojada en un servidor SQL online.

import inicial

inicial.leer_Gmail()
resultado = inicial.resultado

import mysql.connector
mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="JXdnd6btlM",
  password="G11pJ8nwLn",
  database="JXdnd6btlM",
  port="3306"
)

for i in range(len(resultado)):

	mycursor = mydb.cursor()

	sql = "INSERT IGNORE INTO `mails` (`id_del_mensaje`, `fecha`, `de`, `para`, `subject`) VALUES (%s,%s,%s,%s,%s)"
	val = (resultado[i][0],resultado[i][1],resultado[i][2],resultado[i][3],resultado[i][4])
	mycursor.execute(sql, val)

	mydb.commit()
