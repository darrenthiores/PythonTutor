# Latihan menggunakan *Args

def rata_rata(*data) :
    jumlah_data = sum(data)
    banyak_data = len(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)

    return nilai_rata_rata

print (rata_rata(1, 2, 3.5, 7.5, 8.5))
print (rata_rata(1, 4, 2, 1, 2, 1.3, 4.7))