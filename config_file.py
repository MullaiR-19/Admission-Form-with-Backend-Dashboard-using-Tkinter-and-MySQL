from time import sleep
import os
import mysql.connector as sql

user_name = 'root'
passwd = 'password'

def config():
    print('Creting Data Base')
    try:
        server = sql.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        port=3306,
        auth_plugin='mysql_native_password',
        )
        print('Connected to Server')
    except:
        print('Missing MySQL Server\nConfiguration processes cancled!')
    my_cursor = server.cursor()
    try:
        my_cursor.execute('drop database admission_record;')
    except:
        my_cursor.execute('Create database admission_record;')
    table()


def table():
    try:
        server = sql.connect(
        host='localhost',
        user=user_name,
        password=passwd,
        port=3306,
        auth_plugin='mysql_native_password',
        database = 'admission_record'
        )
        print('Connected to Server')
    except:
        print('Missing MySQL Server\nConfiguration processes cancled!')
    print('Creating Table')
    my_cursor = server.cursor()
    my_cursor.execute('use admission_record')
    my_cursor.execute("CREATE TABLE admission_record(student_name varchar(50), parent_name varchar(50), age int, address_r varchar(150), address_p varchar(150), relegion varchar(20),sex varchar(10), dob varchar(25),nationality varchar(30),sslc int,math int, sci int, group_selcted varchar(30),mail varchar(80),number varchar(12), altnumber varchar(12));")
    server.commit()

if __name__ == "__main__":
    config()
