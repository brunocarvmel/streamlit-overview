import mysql.connector 

connection = mysql.connector.connect(
  host= 'localhost',
  user= 'root',
  password= 'bruno2501',
  database= 'dbcrudweb',
)
cursor = connection.cursor()

