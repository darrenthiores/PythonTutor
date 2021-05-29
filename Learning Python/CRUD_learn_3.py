#CRUD (3)

todo_list = []

def show_list() :
    if (len(todo_list) <= 0) :
        print ('TODO LIST IS EMPTY!!')
    else :
        for i in range(len(todo_list)) :
            print (i, todo_list[i])

def input_todo() :
    todo = str(input('Input todo : '))
    todo_list.append(todo)

def change_todo() :
    show_list()
    index = int(input('Masukkan index todo yang ingin diubah : '))
    if (index >= len(todo_list)) :
        print ('Todo NOT FOUND!!')
    else :
        change = str(input('Todo baru : '))
        todo_list[index] = change

def delete_todo() :
    show_list()
    index = int(input('Masukkan index todo yang ingin dihapus : '))
    if (index >= len(todo_list)) :
        print ('Todo NOT FOUND!!')
    else :
        del todo_list[index]

def show_menu() :
    print ('-'*10, 'MENU', '-'*10)
    print ('-'*30)
    print ('[1] SHOW TODO LISTS')
    print ('[2] ADD TODO LIST')
    print ('[3] CHANGE TODO LIST')
    print ('[4] DELETE TODO LIST')
    print ('[5] EXIT')

    menu = int(input('Pilih index menu : '))

    if (menu == 1) :
        show_list()
    elif (menu == 2) :
        input_todo()
    elif (menu == 3) :
        change_todo()
    elif (menu == 4) :
        delete_todo()
    elif (menu == 5) :
        exit()
    else :
        print ('MENU NOT FOUND!!')

#Main looping

if __name__ == "__main__":
    while (True) :
        show_menu()