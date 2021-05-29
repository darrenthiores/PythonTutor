#CRUD (3)

materi_bio = []

#function
def list_materi() :
    if (len(materi_bio) <= 0) :
        print ('MATERI KOSONG')
    else :
        for i in range(len(materi_bio)) :
            print (i,'.', materi_bio[i])

def input_materi() :
    materi = str(input('Materi Bio : '))
    materi_bio.append(materi)

def ralat_materi() :
    list_materi()
    index = int(input('Masukkan index yang mau diubah : '))
    if (index >= len(materi_bio)) :
        print ('MATERI TIDAK DITEMUKAN!!')
    else :
        ralat = str(input('Materi baru : '))
        materi_bio[index] = ralat

def delete_materi() :
    list_materi()
    index = int(input('Masukkan index yang mau dihapus : '))
    if (index >= len(materi_bio)) :
        print ('MATERI TIDAK DITEMUKAN!!')
    else :
        del materi_bio[index]

#UI
def show_menu() :
    print ('-'*10, 'MENU', '-'*10)
    print ('-'*30)
    print ('[1] LIST MATERI')
    print ('[2] TAMBAH MATERI')
    print ('[3] UBAH MATERI')
    print ('[4] HAPUS MATERI')
    print ('[5] EXIT')

    menu = int(input('Pilih menu : '))

    if (menu == 1) :
        list_materi()
    elif (menu == 2) :
        input_materi()
    elif (menu == 3) :
        ralat_materi()
    elif (menu == 4) :
        delete_materi()
    elif (menu == 5) :
        exit()
    else :
        print ('MENU TIDAK DITEMUKAN!!')

#main looping

if __name__ == "__main__":
    while (True) :
        show_menu()