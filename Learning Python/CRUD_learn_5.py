#CRUD (5)

ulangan = []

def show_ulangan() :
    if (len(ulangan) <= 0) :
        print ('EMPTY')
    else :
        for i in range(len(ulangan)) :
            print (i, ulangan[i])

def add_ulangan() :
    ul = str(input('Ulangan : '))
    ulangan.append(ul)

def change_ulangan() :
    show_ulangan()
    i = int(input('Index ulangan yang ingin diubah : '))
    if (i >= len(ulangan)) :
        print ('Ulangan tidak ditemukan!!')
    else :
        new_ulangan = str(input('Ulangan baru : '))
        ulangan[i] = new_ulangan

def delete_ulangan() :
    show_ulangan()
    i = int(input('Index ulangan yang ingin dihapus : '))
    if (i >= len(ulangan)) :
        print ('Ulangan tidak ditemukan!!')
    else :
        del ulangan[i]

def show_menu() :
    print ('MENU')
    print ('-'*20)
    print ('[1] LIST ULANGAN')
    print ('[2] ADD ULANGAN')
    print ('[3] CHANGE ULANGAN')
    print ('[4] DELETE ULANGAN')
    print ('[5] EXIT')

    menu = int(input('Menu : '))

    if (menu == 1) :
        show_ulangan()
    elif (menu == 2) :
        add_ulangan()
    elif (menu == 3) :
        change_ulangan()
    elif (menu == 4) :
        delete_ulangan()
    elif (menu == 5) :
        exit()
    else :
        print ('Menu tidak tersedia!!')

if __name__ == "__main__":
    while (True) :
        show_menu()