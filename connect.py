import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='curriculo_vtx')
	print("Conexão de banco de dados feita!")
	cursor = db_connection.cursor()

	query = ("SELECT nome, telefone, email FROM `usuarios` WHERE status != 'Contratado (a)'")
	cursor.execute(query)
	for (nome, telefone, email) in cursor:
		print(f'{nome}:{telefone}:{email}')
		o = open("lista.txt","a")
		o.write(f'{nome}:{telefone}:{email}\n')

except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Banco de dados não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("O nome de usuário ou a senha estão errados")
	else:
		print(error)
else:
	db_connection.close()