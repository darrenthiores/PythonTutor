#CRUD (4)

barang = []

def list_barang() :
    if (len(barang) <= 0) :
        print ('EMPTY!')
    else :
        for i in range(len(barang)) :
            print (i, barang[i])

def input_barang() :
    InputBarang = str(input('Masukkan Barang : '))
    barang.append(InputBarang)

def change_barang() :
    list_barang()
    i = int(input('Masukkan index barang yang mau diubah : '))
    if (i >= len(barang)) :
        print ('Barang tidak ditemukan!!')
    else :
        new_barang = str(input('Barang baru : '))
        barang[i] = new_barang

def delete_barang() :
    list_barang()
    i = int(input('Masukkan index barang yang mau dihapus: '))
    if (i >= len(barang)) :
        print ('Barang tidak ditemukan!!')
    else :
        del barang[i]

def show_menu() :
    print ('-'*10, 'MENU', '-'*10)
    print ('-'*30)
    print ('[1] Tampilkan list barang')
    print ('[2] Tambahkan barang')
    print ('[3] Ubah barang')
    print ('[4] Delete barang')
    print ('[5] EXIT')

    menu = int(input('Pilih menu : '))

    if (menu == 1) :
        list_barang()
    elif (menu == 2):
        input_barang()
    elif (menu == 3):
        change_barang()
    elif (menu == 4):
        delete_barang()
    elif (menu == 5):
        exit()
    else :
        print ('Menu tidak ditemukan!!')

if __name__ == "__main__":
    while (True) :
        show_menu()