# membuat app countdown

import time

print ('Count down')
input('tekan [ENTER] untuk memulai countdown ')

def timer(start_min, start_sec) :

    total_secs = start_min * 60 + start_sec

    while (total_secs) :
        mins, secs = divmod (total_secs, 60)

        print (f'{mins:02d}:{secs:02d}', end = '\r')

        time.sleep(1)
        total_secs -= 1
    
    print ('Selesai!!')

if __name__ == "__main__":
    timer(1, 00)