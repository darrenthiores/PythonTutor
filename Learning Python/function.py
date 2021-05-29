#function

#Normal function
def func() :
    print ("ini adalah sebuah function")

#memanggil function
func()

#function with parameter
#method retun berfungsi untuk mengembalikkan nilai sehingga bisa dipakai di luar function
def persegi_panjang(p, l) :
    luas = p * l
    return luas

print (persegi_panjang(5, 10))