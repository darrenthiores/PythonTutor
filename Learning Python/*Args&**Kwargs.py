# *Args dan **Kwargs
"""
merupakan variable yg hanya bisa digunakan didalam sebuah function sbg parameter
fungsi keduanya, yaitu ketika suatu function membutuhkan banyak value (data) atau data nya 
bersifat tidak tetap, maka dengan menggunakan *Args dam **Kwargs parameter yang digunakan hanya 1 saja
perbedaan *Args dan **Kwargs, yaitu *Args merupakan tipe data tuple dan **Kwargs tipe datanya dictionary
*Args dan **Kwargs juga dapat membuat parameter suatu fungsi menjadi dinamis
"""

# *Args

def siswa(*nama) :
    print ('Nama siswa : ')
    for murid in nama :
        print (murid)

siswa('budi', 'joni', 'hotman')
siswa ('jovan', 'maria', 'marcell', 'julian')

#ketika tidak menggunakan *Args maka parameter yg diperlukan akan lebih banyak
"""

contoh :
def siswa(nama1, nama2) :
    print (nama)

nama ('siska', 'tono')

--> function dapat dijalankan, tetapi parameter yang diperlukan jadi bertambah

contoh :
def siswa(nama1, nama2) :
    print (nama)

nama ('siska')

--> function tsb akan error krn hanya memiliki 1 value tetapi parameter nya banyak
"""

# **Kwargs
# karena **Kwargs merupakan tipe data dictionary, maka memutuhkan value dan key

def nomor_telepon(**kontak) :
    print ('daftar kontak :')
    for x, y in kontak.items() :
        print (f'{x} : {y}')

nomor_telepon(maria='0822..', jovan='0821..', darren='082282512065') 
nomor_telepon(joni='0891...', devong='0832...', beki='o817...')

# Contoh penggunaan *Args dan *Kwargs pada dunia nyata, yaitu salah satunya mencari rata"

def rata_rata(*nilai) :
    jumlah_data = sum(nilai)
    banyak_data = len(nilai)
    rerata = float(jumlah_data) / float(banyak_data)

    return rerata

print (f'jumlah rata-rata : {rata_rata(2, 3, 5, 6, 7.5, 9.2)}')