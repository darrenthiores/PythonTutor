import time

def count (start_min, start_sec) :
    total_sec = start_min * 60 + start_sec

    while (total_sec) :
        mins, secs = divmod(total_sec, 60)
        print (f'{mins:02d}:{secs:02d}', end = '\r')
        time.sleep(1)
        total_sec -= 1
    print ('Done!!')

if __name__ == "__main__":
    count (00, 30)
