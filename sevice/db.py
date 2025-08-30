import mysql.connector

db = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password ='',
    database ='Data Keuangan'

)

def insert_barang(nama_barang, harga_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (nama_barang, harga_barang) VALUES (%s, %s)", (nama_barang, harga_barang))
    db.commit()
    if cursor.rowcount > 0:
        print("data masuk")
    else:
        print("data gagal")

def fetch_barang():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()