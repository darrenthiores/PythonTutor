#range() function
#fungsinya menghasilkan list dalam range tertentu

#parameter range (batas bawah, batas atas, interval)

#range menggunakan batas atas

range(10)
# --> akan menghasilkan [0, 1, 2, 3 ,4,5, 6 , 7, 8, 9]

#range dengan batas bawah dan batas atas

range(10,20)
# --> akan menghasilkan [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#range dengan batas bawah, batas atas dan interval

range(50, 100, 10)
# --> akan menghasilkan [50, 60, 70, 80, 90]


#range() function biasa nya digunakan pada looping for
for i in range(10, 110, 10) :
    print (i)

#contoh program

for x in range(0, 101) :
    if (x % 2 == 0 and x % 5 == 0) :
        print ('Python!!')
    elif (x % 5 == 0) :
        print ('java!!')
    elif (x % 2 == 0) :
        print ('HTML')
    else :
        print ('none')
