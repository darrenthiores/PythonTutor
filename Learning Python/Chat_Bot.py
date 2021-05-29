import random

def founder() :
    print ('Guido Van Rossum')

def python() :
    print ("Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.")

def date() :
    print ('Python was conceived in the late 1980s[34] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands')

def menu() :
    print ('='*10,'MENU','='*10)
    print ('[1] Penemu python')
    print ('[2] Apa itu python?')
    print ('[3] Kapan python dibuat?')

    pilih_menu = int(input('Pilih menu : '))

    if (pilih_menu == 1) :
        founder()
    elif (pilih_menu == 2) :
        python()
    elif (pilih_menu == 3) :
        date()
    else :
        print ('Menu tidak tersedia')

if __name__ == "__main__":
    while (True) :
        menu()