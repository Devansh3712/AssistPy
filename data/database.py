'''
Module for maintaining search
history of user using MySQL
database management
'''

#Importing modules
try:
    import datetime
    import mysql.connector as mc

except:
    print("Database module not setup")
    exit()

#Initialize database connection object
connectMySQL = mc.connect(host = "localhost", user = "root", password = "root")

#Initialize database operation cursor
cursor = connectMySQL.cursor(buffered = True)

#create database and user table if it doesn't exist
cursor.execute('create database IF NOT EXISTS assistpy')
cursor.execute('use assistpy')
cursor.execute('create table IF NOT EXISTS users(date varchar(10), history varchar(65535), time varchar(10))')

#Class for creating user history/logs
class Logs:

    def __init__(self):
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.time = datetime.now().strftime("%X")