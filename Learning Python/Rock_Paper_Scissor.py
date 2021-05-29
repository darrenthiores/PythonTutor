# rock paper scissor project

import random

print ('\n')
print ('Rock Paper Scissor Games!!')
print ('\n')

choices = ['rock', 'paper', 'scissor']

def game() :

    player = str(input("enter 'rock' / 'paper' / 'scissor' : "))
    comp_random = random.randint(0,2)
    computer = choices[comp_random]

    print ('\n')
    print ('Computer is choosing...')
    print ('\n')
    print (f'Computer choices is {computer}')

    if (player == 'rock' or player == 'Rock') :
        if (computer == 'rock') :
            print ("It's a draw!!")
        elif (computer == 'scissor') :
            print ("Congratss youu win the game!!")
        elif (computer == 'paper') :
            print ("Loser!!")
    elif (player == 'paper' or player == 'Paper') :
        if (computer == 'rock') :
            print ("Congratss youu win the game!!")
        elif (computer == 'scissor') :
            print ("Loser!!")
        elif (computer == 'paper') :
            print ("It's a draw!!")
    elif (player == 'scissor' or player == 'Scissor') :
        if (computer == 'rock') :
            print ("Loser!!")
        elif (computer == 'scissor') :
            print ("It's a draw!!")
        elif (computer == 'paper') :
            print ("Congratss youu win the game!!")
    else :
        print ('enter the right choices!!')

if __name__ == "__main__":
    while(True) :
        game()