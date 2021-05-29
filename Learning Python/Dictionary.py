#Dictionary
daftar_murid = {
    'absen1' : 'edward',
    'absen2' : 'maria',
    'absen3' : 'ignaz'
}

print (daftar_murid)


#Mengakses dictionary

#normal dict
print (daftar_murid['absen1'])

#complex
data_murid = {
    'absen1' : {
        'nama' : 'edward',
        'umur' : 17,
        'kelas' : 'XII IPA 2',
        'pintar' : False
    }
}

print (data_murid['absen1']['nama'])

#get() method
print (daftar_murid.get('absen2'))


#Looping dalam dict
for key, val in data_murid['absen1'].items():
    print (key, ':' , val)


#Mengubah isi dict

#normal
daftar_murid['absen1'] = 'Edi'

for key, val in daftar_murid.items():
    print (key, ':', val)

#Complex
data_murid['absen1']['pintar'] = True

for key, val in data_murid.items() :
    print (key, ':', val)


#Menghapus item dari dict

#method del
del data_murid['absen1']['umur']

#method pop()
data_murid['absen1'].pop('kelas')

for key, val in data_murid.items():
    print (key, ':', val)

#clear() method (menghapus semua)
daftar_murid.clear()


#menambahkan value kedalam dict
#menggunakan method update()
#bisa digunakan untuk mengganti value juga

data_murid.update({'excul' : 'futsal'})
data_murid['absen1'].update({'nama' : 'edi'})

for key, val in data_murid.items():
    print (key, ':', val)


#mengambil panjang dict
#menggunakan method len()

print (len(data_murid['absen1']))