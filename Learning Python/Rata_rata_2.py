def rata_rata(*data) :
    jumlah_data = sum(data)
    banyak_data = len(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)

    return nilai_rata_rata

print (rata_rata(12, 4.3, 3.5, 12.4, 124))