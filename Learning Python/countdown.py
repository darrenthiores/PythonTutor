# latihan menggunakan time.sleep() dengan mermbuat countdown

import time

def count_down(minutes, seconds) :

    # menghitung total detik
    total_second = minutes * 60 + seconds
    
    #total detik dihitung untuk melakukan perulangan sebanyak detiknya
    while (total_second) :
        mins, secs = divmod(total_second, 60)
        print (f'{mins:02d}:{secs:02d}', end = '\r')
        time.sleep(1)
        total_second -= 1

"""
pada function diatas, divmod berguna untuk membagi total detik dengan 60 dan hasilnya
disimpan di variabel mins dan sisanya di variabel secs
pada print didalam perulangan while, 02d befungsi untuk mencetak angka dalam dua digit
dan \r berfungsi untuk teks yg dicetak akan ditindih atau ditulis ulang
"""


# main looping

if __name__ == "__main__":
    count_down(00, 30)