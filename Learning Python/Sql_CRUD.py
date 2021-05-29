# belajar membuat app CRUD menggunakan python dan mysql

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'admin'
)

if db.is_connected() :
    print ('Berhasil terhubung ke database')