# time.sleep() function
# fungsi time.sleep() yaitu adalah untuk menunda waktu eksekusi
# dengan ditundasnya waktu eksekusi maka function ini dapat digunakan untuk membuat animasi
# function time.sleep() dapat digunakan dengan mengimport time

import time

for i in range(10, 31, 2) :
    time.sleep(0.5)
    print (i)

print ('Hello World')

# contoh lain

print ('Apakah roket siap diluncurkan ?')
input('tekan [ENTER] jika roket siap diluncurkan')
print ('\n')
print ('Hitung mundur :')

for x in range(10, 0, -1) :
    time.sleep(1)
    print (f'hitungan ke-{x}')

print ('BUUUUUUZZZZZZZ')
print ('Roket diluncurkan')    