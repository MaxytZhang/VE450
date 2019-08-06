#!flask/bin/python
from Models.Meeting import Meeting
import datetime
import mysql.connector

from mysql.connector import Error

try:
    connection = mysql.connector.connect(host = 'localhost', database = '...', user = '...', password = '...')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", db_Info)
        Foxconn_cursor = connection.cursor()
        Foxconn_cursor.execute("select database();")
        record = Foxconn_cursor.fetchone()
        print("Your connected to - ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # closing database connection.
    if (connection.is_connected()):
        Foxconn_cursor.close()
        Foxconn_connection.close()
        print("MySQL connection is closed")
