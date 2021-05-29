#Tuple
fish = ('koi', 'gepi', 'cupang')

#Tuple kosong
name = ()

#Mengakses Tuple (menggunakan indeks) --> sama seperti list
print (fish[0])

#Tuple value gabisa diubah (constant)
"""
contoh --> fish[0] = hiu -->Error
"""

#Memotong Tuple --> sama seperti list
print (fish[1:3])

#Mengambil panjang tuple --> sama seperti list
print (len(fish))

#Nested tuple

#Tuple bisa berisi tuple
hewan = (
    ('ikan', 'paus', 'udang'),
    ('beruang', 'singa')
)

print (hewan)
print (hewan[1])
print (hewan[1][0])

#Tuple bisa berisi objek apapun
random = (1, 'ayam', True, (2,3,4), ['list1', 'list2'])

print (random)

#Sequence Tuple
"""
Tuple merupakan sebuah pack yg dapat di unpacking
dengan melakukan unpacking maka tuple akan dicopy ke variabel
"""

names = ('maria', 'fidelia', 17)

print (names)

firstName, lastName, age = names

print (firstName)
print (lastName)
print (age)