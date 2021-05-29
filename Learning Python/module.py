class saham :
    def __init__(self, nama_saham, harga_saham) :
        self.nama = nama_saham
        self.harga = harga_saham
    
    def total(self) :
        print (f'Nama saham : {self.nama}')
        print (f'Harga : {self.harga}')
        print ('---')