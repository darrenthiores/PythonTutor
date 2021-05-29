#CRUD (2)
#CRUD daftar alamat

daftar_alamat = []

#function
def list_alamat() :
    if (len(daftar_alamat) <= 0) :
        print ('LIST IS BLANK!!')
    else :
        for i in range(len(daftar_alamat)) :
            print (i, daftar_alamat[i])

def input_alamat() :
    alamat = str(input('Alamat : '))
    daftar_alamat.append(alamat)

def ralat_alamat() :
    list_alamat()
    index = int(input('Masukkan index : '))
    if (index > len(daftar_alamat)) :
        print ('ALAMAT TIDAK DITEMUKAN!!')
    else :
        ralat = str(input('Alamat baru : '))
        daftar_alamat[index] = ralat

def hapus_alamat() :
    list_alamat()
    index = int(input('Masukkan index : '))
    if (index > len(daftar_alamat)) :
        print ('ALAMAT TIDAK DITEMUKAN!!')
    else :
        del daftar_alamat[index]

#UI
def show_menu() :
    print ('-'*10, 'MENU', '-'*10)
    print ('-'*30)
    print ('[1] DAFTAR ALAMAT')
    print ('[2] INPUT ALAMAT')
    print ('[3] RALAT ALAMAT')
    print ('[4] HAPUS ALAMAT')
    print ('[5] EXIT')

    menu = int(input('Pilih index menu : '))

    if (menu == 1) :
        list_alamat()
    elif (menu == 2) :
        input_alamat()
    elif (menu == 3) :
        ralat_alamat()
    elif (menu == 4) :
        hapus_alamat()
    elif (menu == 5) :
        exit()

#Main looping

if __name__ == "__main__":
    while (True) :
        show_menu()