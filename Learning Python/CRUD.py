#CRUD

daftar_siswa = []

#function

#untuk menampilkan daftar siswa
def list_siswa() :
    if (len(daftar_siswa) <= 0) :
        print ('DAFTAR KOSONG')
    else :
        for i in range(len(daftar_siswa)):
            print (i, daftar_siswa[i])

#untuk memasukkan nama siswa
def input_siswa() :
    nama_siswa = str(input('Nama siswa : '))
    daftar_siswa.append(nama_siswa)

#untuk meralat / mengganti nama siswa
def ralat_nama() :
    list_siswa()
    index = int(input('Input id siswa : '))
    if (index > len(daftar_siswa)) :
        print ('siswa tidak ditemukan')
    else :
        ralat = str(input('Nama siswa : '))
        daftar_siswa[index] = ralat

#untuk menghapus siswa
def delete_nama() :
    list_siswa()
    index = int(input('Input id siswa : '))
    if (index > len(daftar_siswa)) :
        print ('siswa tidak ditemukan')
    else :
        del daftar_siswa[index]

#UI
def show_menu() :
    print ('-'*10, 'DAFTAR SISWA', '-'*10)
    print ('-'*30)
    print ('[1] Tampilkan daftar')
    print ('[2] Masukkan siswa kedaftar')
    print ('[3] Ralat nama siswa')
    print ('[4] Hapus nama siswa')
    print ('[5] EXIT')

    menu = int(input('Pilih menu : '))

    if (menu == 1) :
        list_siswa()
    elif (menu == 2) :
        input_siswa()
    elif (menu == 3) :
        ralat_nama()
    elif (menu == 4) :
        delete_nama()
    elif (menu == 5) :
        exit()
    else :
        print ('Pilihan tidak ditemukan!!')


#main loop program

if __name__ == "__main__":
    while (True) :
        show_menu()