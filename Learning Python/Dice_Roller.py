# dice roller project
 
import random

dice = random.randint(1,6)
print (f'Roll the dice!! : {dice}')

def roller() :
     dice = random.randint(1,6)
     print (f'Roll the dice!! : {dice}')

def menu() :
    roll = str(input("enter 'yes' to roll the dice again : "))
    if (roll == 'yes' or roll == 'Yes') :
        roller()
    else :
        print ('Thank you for playing!!')
        exit()

if __name__ == "__main__":
    while (True) :
        menu()