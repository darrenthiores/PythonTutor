# membuat app number guessing dengan level berbeda

import random

def low_level() :
    number = random.randint(1,10)
    chances = 3
    while (chances > 0) :
        guess = int(input('Your guess : '))
        if (guess == number) :
            print ('Congratss you win the game!!')
            break
        elif (guess > number) :
            print ('your guess is too high, go with a lower number')
        elif (guess < number) :
            print ('your guess is too low, go with a bigger number')
    
    if (chances <= 0) :
        print ('you lose the game!!')

def med_level() :
    number = random.randint(1,25)
    chances = 5
    while (chances > 0) :
        guess = int(input('Your guess : '))
        if (guess == number) :
            print ('Congratss you win the game!!')
            break
        elif (guess > number) :
            print ('your guess is too high, go with a lower number')
        elif (guess < number) :
            print ('your guess is too low, go with a bigger number')
    
    if (chances <= 0) :
        print ('you lose the game!!')

def high_level() :
    number = random.randint(1,50)
    chances = 8
    while (chances > 0) :
        guess = int(input('Your guess : '))
        if (guess == number) :
            print ('Congratss you win the game!!')
            break
        elif (guess > number) :
            print ('your guess is too high, go with a lower number')
        elif (guess < number) :
            print ('your guess is too low, go with a bigger number')
    
    if (chances <= 0) :
        print ('you lose the game!!')

def pick_level() :
    print ('='*10,'Number Guessing Game','='*10)
    print ('[1] Low Level (1 - 10, 3 chances)')
    print ('[2] Medium Level (1 - 25, 5 chances)')
    print ('[3] High Level (1 - 50, 8 chances)')
    print ('[4] EXIT')

    menu = int(input('Pick level (index) : '))

    if (menu == 1) :
        low_level()
    elif (menu == 2) :
        med_level()
    elif (menu == 3) :
        high_level()
    elif (menu == 4) :
        exit()
    else :
        print ('Which level did you picked?')

if __name__ == "__main__":
    while (True) :
        pick_level()