import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "djangouser",
    password = "123456"
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM")

print("LISTO")