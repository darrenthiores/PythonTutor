# Max() function
# untuk mencari angka tertinggi

angka = [1, 2, 4, 5, 34, 45, 23, 31]

tertinggi = max(angka)
terendah = min(angka)

print (tertinggi)
print (terendah)

# Contoh programnya (mencari pendapatan tertinggi dan terendahdidalam suatu bulan)

bulan = {
    'januari' : 0,
    'februari' : 0,
    'maret' : 0,
    'april' : 0,
    'mei' : 0,
    'juni' : 0
}

#Input penghasilan

for i in bulan :
    bulan[i] = int(input(f'penghasilan pada bulan {i} : Rp. '))

#Mencari penghasilan tertinggi

penghasilan_tertinggi = max(bulan['januari'], bulan['februari'], bulan['maret'], bulan['april'], bulan['mei'], bulan['juni'])

#Mencari penghasilan terendah

penghasilan_terendah = min(bulan['januari'], bulan['februari'], bulan['maret'], bulan['april'], bulan['mei'], bulan['juni'])

#cari dan cetak bulan serta penghasilan tertinggi

for i in bulan :
    if (bulan[i] == penghasilan_tertinggi) :
        print (f'penghasilan tertinggi berada pada bulan : {i}, yaitu : {bulan[i]}')

#cari dan cetak bulan serta penghasilan terendah

for i in bulan :
    if (bulan[i] == penghasilan_terendah) :
        print (f'penghasilan terendah berada pada bulan : {i}, yaitu : {bulan[i]}')