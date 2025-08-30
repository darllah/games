import main
from sevice import db

def add():
    nama_barang = input('nama barang:')
    harga_barang = int(input('harga barang:'))

    save = db.insert_barang(nama_barang, harga_barang)
    print(save)

def check():
    item = db.fetch_barang()
    for item in item:
        nama_barang = item[1]
        harga_barang = item[2]
        print(f'\nnama barang: {nama_barang}\nharga: {harga_barang}')

def start():
    while True:
        menu = int(input('menu:\n1. Tambah Barang\n2. Cek Barang\n3. Kembali\n\n '))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break

if __name__ == '__main__':
    start()
