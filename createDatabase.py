import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE vehicles")


