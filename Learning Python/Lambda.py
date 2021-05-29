#Lambda
#disebut sbg anonymus function, dimana bisa dijadikan variable
#bisa memiliki lebih dari 1 parameter tetapi hanya bisa memiliki 1 expression

#membuat lambda
#lambda tidak memiliki nama (anonymus) sehingga memerlukan variable untuk menyimpannya
luas = lambda p,l : print (p*l)

luas (2,5)

#memasukkan lambda kedalam variable
persegi = luas

persegi (3, 3)
luas (2, 2)

#kelebihan lambda --> eksekusi langsung
execution = (lambda x, y : ((x+2)-(y+3))) (3, 3)

print (execution)

"""
lambda digunakan ketika ingin membuat function 1 baris atau
untuk function" yang membutuhkan parameter function
"""

#Contoh lambda sebagai parameter function

#map() function
bilangan = [2, 5, 7, 3]
double = lambda x : (x * x)

result = map (double, bilangan)

print (list(result))

#atau bisa dengan cara langsung
result_2 = map (lambda x : x + x, bilangan)

print (list(result_2))

#Contoih ke-2
#filter() function

genap = lambda x : x % 2 == 0
bil_genap = list(filter(genap, range(13)))

print (bil_genap)

bil_ganjil = list(filter(lambda x : x % 2 != 0, range(13)))

print (bil_ganjil)

#Contoh ke-3 (normal)
nama = lambda name : print (f'nama : {name}')
name = nama

nama ('Guido van rossum')
name ('linus')