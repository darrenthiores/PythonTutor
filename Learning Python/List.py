#List
Internet = ['Microsoft', 'Google', 'Apple', 'Linux']

#mengambil nilai list
print (Internet[1])

#Mengganti nilai list
Internet[2] = 'Raspberry pi'
print (Internet)

#Menampilkan jumlah list
print (len(Internet))

#Menambah nilai List

#dari belakang
Internet.append('Phyton')

#menggunakan indeks
Internet.insert(2, 'AOC')

print (Internet)

#mendelete list

#function del
del Internet[1]

#function remove
Internet.remove('AOC')

print (Internet)

#Memotong list
print (Internet[2:4])

#Operasi pada list
penemu = ['gudo van rossum', 'bill gates', 'steve jobs']
ditemukan = ['phyton', 'microsoft', 'apple']

#Penggabungan
print (penemu + ditemukan)

#Perkalian
print (penemu * 2)

#Multi-dimensional list
Makanan_perjenis = [
    ['kopi', 'teh', 'air'],
    ['pizza', 'burger', 'hotdog'],
    ['sayur', 'salad',]
]

print (Makanan_perjenis)

print (Makanan_perjenis[1])

print (Makanan_perjenis[1][0])